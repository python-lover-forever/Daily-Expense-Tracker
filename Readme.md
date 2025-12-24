# Daily Expenses Tracker (Using Console(java))

## Introduction

The **Daily Expense Tracker** is a light-weight, console-based application that is developed in Python. It intends to assist a user in recording his daily expenses. The project is based on simplicity. It does not require any additional libraries because it uses basic Python.

The app enables users to record expenditures, display all recorded data, alter or delete recorded data, as well as compile simple reports such as a total spent amount, grouped by categories, and monthly expenditures. The app uses a JSON file to store all data locally, hence making it easy to run and operate.

## Key Features

### Add Expenses
- Record expense amount, type, and date

- Automatic fallback to current date if date is not valid and/or empty

### View All Expenses
- Returns the list of all saved expense records as a list of lists containing the date, category,

### Edit Expenses

- Alter the amount, category, or date of an existing entry
- Handles partial update (can skip fields if not required)
### Delete Expenses

- Subtract a definite cost by index
### Expense Summaries

- Compute total expense.

- Group expenses by category

- Compute total cost incurred during a given month
### Data Persistence
- Costs are recorded in the local system in `data.json`
- Data is automatically loaded when starting up
### Reset Option

- Wipe all stored data with confirmation required

## Technical Details

- **Language:** Python 3
- *Storage*: Local JSON file
- **Interface Type**: Command Line Interface
- **Libraries Used:**

- `json` for storing the data

- `datetime` for working with dates
The project deliberately resists the use of high-level abstractions such as classes or third-party libraries, making it simple to understand even for novice and beginner programmers.
## Project Aims/Objectives
- Real World Python Essentials
- Handling file input/output and persistent data - User input handling and validation - Create working software with minimal overengineering - Simulate a realistic development workflow for a small utility tool. # How to Run 1. Make sure Python3 is installed. 2. The script should go to a directory of your choice. 3. Run the program: bash python main.py
