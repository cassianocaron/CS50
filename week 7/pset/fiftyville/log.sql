-- Select the description from the date and place the theft took place
SELECT description FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND year = 2020 AND street = "Chamberlin Street";

-- Select the name and the transcript where there is mention of the courthouse
SELECT name, transcript FROM interviews
WHERE day = 28 AND month = 7 AND year = 2020 AND transcript LIKE "%courthouse%";

-- Select license plate and the activity in the courthouse parking lot within 10 minutes after the theft took place
SELECT license_plate, activity FROM courthouse_security_logs
WHERE minute >= 15 AND minute <= 25 AND hour = 10 AND day = 28 AND month = 7 AND year = 2020;

-- Select account number and amount withdrawed from the atm machine at Fifer Street at the day the theft took place
SELECT account_number, amount FROM atm_transactions
WHERE day = 28 AND month = 7 AND year = 2020 AND transaction_type = "withdraw" AND atm_location = "Fifer Street";

-- Get the calls from the day the theft took place that are less than a minute
SELECT * FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60;

-- Get the id and name of Fiftyville's airport
SELECT id, full_name FROM airports
WHERE city = "Fiftyville";

-- Get the origin and destination airports id from the day after the theft took place
SELECT origin_airport_id, destination_airport_id FROM flights
WHERE day = 29 AND month = 7 AND year = 2020;

-- Get the flight hours from the day after the theft took place
SELECT hour FROM flights
WHERE day = 29 AND month = 7 AND year = 2020;

-- Get the minute from the 8am flight 
SELECT minute FROM flights
WHERE hour = 8 AND day = 29 AND month = 7 AND year = 2020;

-- Get the earliest flight id
SELECT id FROM flights
WHERE minute = 20 AND hour = 8 AND day = 29 AND month = 7 AND year = 2020;

-- Get passport numbers from passengers
SELECT passport_number FROM passengers
WHERE flight_id = 36;



-- Get the name of the thief from people, which is Ernest
SELECT name FROM people
WHERE id =
-- Get the person id from bank_accounts (Returns only one match so we found the thief)
(SELECT person_id FROM bank_accounts
WHERE person_id IN
-- Get the id of the people where the license plate matches with the ones that were in the courthouse parking lot at the time the theft took place
(SELECT id FROM people
WHERE license_plate IN
    (SELECT license_plate FROM courthouse_security_logs
    WHERE activity = "exit" AND minute >= 15 AND minute <= 25 AND hour = 10 AND day = 28 AND month = 7 AND year = 2020)
INTERSECT
-- Get the id of the people where the passport number matches with the ones that were in the earliest flight in the day after the theft
SELECT id FROM people
WHERE passport_number IN
    (SELECT passport_number FROM passengers
    WHERE flight_id = 36)
INTERSECT
-- Get the id of the people where the phone number matches with the calls from the day the theft took place
SELECT id FROM people
WHERE phone_number IN
    (SELECT caller FROM phone_calls
    WHERE day = 28 AND month = 7 AND year = 2020 AND duration < 60)));


-- Get the name of the city where the thief and the accomplice escaped to (London)
SELECT city FROM airports
WHERE id IN
-- Get the destination airport id
(SELECT destination_airport_id FROM flights
WHERE id IN
-- Get the flight id
(SELECT flight_id FROM passengers
WHERE passport_number =
-- Get Ernest's passport number 
(SELECT passport_number FROM people
WHERE name = "Ernest")));


-- Get the name of the accomplice (Berthold)
SELECT name FROM people
WHERE phone_number =
(SELECT receiver FROM phone_calls
WHERE caller =
(SELECT phone_number FROM people
WHERE name = "Ernest")
AND day = 28 AND month = 7 AND year = 2020 AND duration < 60);