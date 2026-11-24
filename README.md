
# Campus Lost & Found – Smart Item Matcher

## Project Overview
Campus Lost & Found is a web-based application developed to help students report, search and recover lost or found items within a university campus.

The system also includes a Smart Item Matching feature that compares lost and found item details to identify possible matches.

## Objectives
- Provide a platform to report lost items.
- Allow users to report found items.
- Make searching for items easier.
- Identify possible matches between lost and found items.
- Maintain item records using CSV files.

## Key Features
1. Report Lost Items
2. Report Found Items
3. Browse All Items
4. Search Items
5. Smart Item Matching
6. Mark Items as Returned
7. Dashboard Statistics

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Pandas
- CSV

## Project Structure
- app.py – Main Flask application
- database.py – CSV database management
- registration.py – Item registration
- search.py – Item searching
- matching.py – Smart matching algorithm
- records.py – Record management
- templates/ – HTML pages
- static/css/ – CSS styling
- data/ – CSV data files
- requirements.txt – Project dependencies

## How to Run the Project

1. Open the project folder in VS Code.
2. Activate the virtual environment.
3. Install the required libraries:

   pip install -r requirements.txt

4. Run the application:

   python app.py

5. Open the following address in your browser:

   http://127.0.0.1:5000

## Smart Matching Algorithm
The system compares five item attributes:

- Name – 30 points
- Category – 20 points
- Colour – 20 points
- Location – 20 points
- Date – 10 points

A match score of 40% or above is displayed as a possible match.

The matching system uses a rule-based comparison algorithm and does not use machine learning.

## Data Storage
Lost and found item records are stored separately in CSV files:
- lost_items.csv
- found_items.csv

Pandas is used to read, manage and update these records.

## Project Purpose
This project demonstrates computational thinking, problem decomposition, conditional statements, loops, functions, data handling and basic web development.
