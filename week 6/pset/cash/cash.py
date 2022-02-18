def main():
    # Prompts user for a positive number
    while True:
        try:
            change = float(input("Change owed: "))
            if change >= 0:
                break
        # If the input is not a number, prints an error message
        except ValueError:
            print("Invalid input")

    # Multiplies the input by 100 and rounds it to the nearest integer
    cents = int(round(change * 100))
    coins = 0

    # Keep subtracting the change by the value of each coin and incrementing the counter
    while cents >= 25:
        cents -= 25
        coins += 1

    while cents >= 10:
        cents -= 10
        coins += 1

    while cents >= 5:
        cents -= 5
        coins += 1

    if cents == 1:
        coins += 1

    # Prints the amount of coins needed
    print(f"Coins: {coins}")


if __name__ == '__main__':
    main()