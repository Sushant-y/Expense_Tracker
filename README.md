# CLI Expense Tracker (Python)

This is a simple command-line expense tracker built using Python.  
This project was created to practice core Python fundamentals by solving a small but realistic problem.

The application allows users to record expenses, store them locally, and generate basic reports using the command line.

-------------

## What the Application Does

- Records expenses with amount and category
- Automatically stores the date and time of each entry
- Displays total expenses
- Filters and displays expenses for a specific date
- Handles invalid input and missing data safely
- Persists data using a local file (no database at this stage)

-------------

## Data Storage

Expenses are stored locally in a text file (ignored via `.gitignore`) using the following format:

```
YYYY-MM-DD HH:MM:SS,amount,category
```

Example:
```
2025-12-18 14:01:22,250.0,Food
2025-12-18 18:40:10,120.0,Travel
```

