import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from operator import itemgetter
from math import modf

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Query database for all stocks the current user owns
    stocks = db.execute(
        "SELECT stock, SUM(shares) FROM transactions WHERE user_id = ? GROUP BY stock HAVING SUM(shares) > 0", session["user_id"]
    )

    # Get how much cash current user has in account
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    current_cash = cash[0]["cash"]

    total_cash = current_cash

    updated_stocks = []

    # Lookup each stock for current price and update the values
    for stock in stocks:
        stock_details = {}
        quote = lookup(stock["stock"])
        stock_details['symbol'] = quote["symbol"]
        stock_details['name'] = quote["name"]
        stock_details['price'] = quote["price"]
        stock_details['shares'] = stock["SUM(shares)"]
        total_per_share = stock_details["price"] * stock_details["shares"]
        stock_details['total_per_share'] = total_per_share
        updated_stocks.append(stock_details)
        total_cash += total_per_share

    return render_template("index.html", stocks=updated_stocks, cash=current_cash, total=total_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        # Lookup stock symbol
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)

        # Check for invalid symbol
        if not stock:
            return apology("Invalid Symbol", 400)

        # Check if shares is an integer
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Can't buy fractional shares")

        # Check if shares is a negative number
        if shares <= 0:
            return apology("Value must be greater than or equal to 1")

        # Get current cash from the user
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        current_cash = cash[0]["cash"]

        # Cost of the current purchase
        transaction_cost = round((shares * stock["price"]), 2)

        # Check if the user can afford the purchase
        if current_cash < transaction_cost:
            return apology("Cannot afford", 400)

        # Subtract the purchase from the current cash
        current_cash -= transaction_cost

        # Round the cash to two decimal places
        current_cash = round(current_cash, 2)

        # Get current date and time
        date_time = datetime.now()

        # Update users' cash in the database
        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash, session["user_id"])

        # Insert the details of the transaction into the database
        db.execute("INSERT INTO transactions (stock, price, shares, total, date, user_id) VALUES (?, ?, ?, ?, ?, ?)",
                   stock["symbol"], stock["price"], shares, transaction_cost, date_time, session["user_id"])

        # Display the user a success message
        if shares > 1:
            flash(f"Bought {shares} shares of {symbol}!")
        else:
            flash(f"Bought {shares} share of {symbol}!")

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Query database for history of transactions
    history = db.execute("SELECT stock, price, shares, total, date FROM transactions WHERE user_id = ?", session["user_id"])

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        # Get the name, symbol and price
        stock = lookup(request.form.get("symbol"))

        # Check if it's a valid symbol
        if stock is not None:
            return render_template("quoted.html", stock=stock)
        return apology("Invalid Symbol", 400)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 400)

        # Ensure username isn't already taken
        elif db.execute("SELECT username FROM users WHERE username = ?", request.form.get("username")):
            return apology("Username is already taken", 400)

        # Add user to database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password")))

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Query database for all stocks owned
    stocks = db.execute(
        "SELECT stock FROM transactions WHERE user_id = ? GROUP BY stock HAVING SUM(shares) > 0", session["user_id"]
    )

    if request.method == "POST":

        stock = request.form.get("symbol")
        quote = lookup(stock)

        # Check for invalid symbol
        if not stock:
            return apology("Please select a stock")

        # Check for invalid shares
        try:
            shares = int(request.form.get("shares"))
            if shares <= 0:
                return apology("Shares must be a positive integer")
        except:
            return apology("Enter the amount of shares to sell")

        # Check if stock is in the database
        if stock not in map(itemgetter("stock"), stocks):
            return apology("Stock is not in portfolio")

        # Query database for the amount of shares for each stock
        shares_query = db.execute("SELECT SUM(shares) from transactions WHERE stock = ? AND user_id = ?", stock, session["user_id"])

        # Check if shares entered aren't great than the amount owned
        if shares > shares_query[0]["SUM(shares)"]:
            return apology("Too many shares")

        transaction_value = quote["price"] * shares

        date_time = datetime.now()

        # Insert transaction into database
        db.execute("INSERT INTO transactions (stock, price, shares, total, date, user_id) VALUES (?, ?, ?, ?, ?, ?)",
                   stock, quote["price"], shares * -1, transaction_value, date_time, session["user_id"])

        cash = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])
        cash = cash[0]["cash"] + transaction_value

        # Update user's cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        # Display the user a success message
        if shares > 1:
            flash(f"Sold {shares} shares of {stock}!")
        else:
            flash(f"Sold {shares} share of {stock}!")

        return redirect("/")

    else:
        return render_template("sell.html", stocks=stocks)


@app.route("/wallet", methods=["GET", "POST"])
@login_required
def wallet():
    """Allow users to add aditional cash to their account"""

    # Select current cash owned from database
    current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    current_cash = current_cash[0]["cash"]

    if request.method == "POST":

        # Check for invalid input
        try:
            deposit = float(request.form.get("cash"))
            deposit = float(f"{deposit:0.2f}")
        except:
            return apology("Invalid amount")

        # Add the amount entered to the account
        cash = current_cash + deposit

        # Update cash in the database
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        # Display a success message
        flash(f"Added {usd(deposit)} to account!")

        return redirect("/")

    else:
        return render_template("wallet.html", cash=current_cash)
