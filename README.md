# Weather Prediction Application

## Overview
This program retrieves historical weather data from the Open-Meteo API, calculates statistics (average/sum, minimum, and maximum), 
and stores the results in a SQLite database using SQLAlchemy.

---

## Requirements

Install required packages before running the program:

pip install -r requirements.txt

---

## Files

- main.py: Runs the application
- weather.py: Retrieves and processes weather data from the API
- database.py: Defines the database schema and initializes the database
- test.py: Runs unit tests
- weather.db: SQLite database (created automatically)

---

## How to Run the Program

Run the main application:

python main.py

---

## Inputs

In this case, our inputs are chosen for Chattanooga, TN:

- Latitude: 35.0456
- Longitude: -85.3097
- Date: November 15, 2025

These values can be modified in main.py if needed. The user 
will need to obtain latitude, longitude, and date of desired
location.

---

## Outputs

The following occurs upon running the program:

1. Retrieve weather data from the Open-Meteo API
2. Calculate:
   - Average, minimum, and maximum temperature
   - Average, minimum, and maximum wind speed
   - Sum, minimum, and maximum precipitation
3. Store the results in an SQLite database (weather.db)
4. Display the results in the console

---

## Running Tests

To run unit tests:

python test.py

Expected output:

All unit tests passed successfully

---

## Notes

- The program retrieves data for the past 5 years based on the selected date.