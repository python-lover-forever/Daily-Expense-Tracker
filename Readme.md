# Daily Expense Tracker (Console-Based)

## Overview

The **Daily Expense Tracker** is a lightweight, console-based Python application designed to help users record, manage, and review their daily expenses. The project focuses on simplicity, clarity, and practicality, using core Python features without external dependencies or complex frameworks.

The application allows users to add expenses, view all recorded entries, edit or delete existing records, and generate basic summaries such as total spending, category-based aggregation, and monthly expense totals. All data is stored locally in a JSON file, making the tool easy to run and maintain.

## Key Features

### Add Expenses
- Record expense amount, category, and date
- Automatic fallback to today’s date if input is invalid or empty

### View All Expenses
- Display a numbered list of all stored expense records

### Edit Expenses
- Modify amount, category, or date of an existing entry
- Supports partial updates (skip fields if not needed)

### Delete Expenses
- Remove a specific expense by its index

### Expense Summaries
- Calculate total spending
- Aggregate expenses by category
- Calculate total expenses for a specific month

### Data Persistence
- Expenses are saved locally in a `data.json` file
- Data is automatically loaded on startup

### Reset Option
- Clear all stored data with a confirmation step

## Technical Details

- **Language:** Python 3  
- **Storage:** Local JSON file  
- **Interface:** Command Line Interface (CLI)  
- **Libraries Used:**
  - `json` for data storage
  - `datetime` for date handling

The project intentionally avoids advanced abstractions such as classes or external libraries, keeping the code accessible and easy to understand for beginners and intermediate learners.

## Project Goals

- Practice real-world Python fundamentals
- Work with file I/O and persistent data
- Handle user input and basic validation
- Build a functional application without overengineering
- Simulate a realistic development workflow for a small utility tool

## How to Run

1. Ensure Python 3 is installed.
2. Place the script in a directory of your choice.
3. Run the program:
   ```bash
   python main.py
