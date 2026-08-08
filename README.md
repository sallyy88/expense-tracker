# Expense Tracker (SQLite Version)

A command-line expense tracker built in Python, using a SQLite database for storage. This is an upgraded version of an earlier expense tracker that originally used a JSON file — rebuilt to use a real database instead.

## Features

- Add expenses with amount, category, and date
- View all expenses with a running total and per-category breakdown
- Filter expenses by category using SQL queries
- Delete expenses by their database ID
- Data is stored in a SQLite database (`expenses.db`), using parameterized queries to prevent SQL injection

## How to run

1. Make sure you have Python installed
2. Clone this repo or download the files
3. Run:

```
python tracker_db.py
```

4. Follow the on-screen menu to add, view, filter, or delete expenses

## Why I rebuilt this with a database

The JSON version had to rewrite the entire file every time a single expense was added or deleted, and any filtering had to be done manually in Python by looping through all the data. Using SQLite lets the database handle filtering directly (e.g. WHERE category = ?), and updates only affect the specific row that changed, which is far more efficient.

## What I learned

I learned the basics of SQL — creating tables, inserting, selecting, and deleting data — along with why parameterized queries (? placeholders) are important for preventing SQL injection. I also learned to work with tuples instead of dictionaries, since database query results come back as tuples indexed by position rather than by key name.

## Possible future improvements

- Edit existing expenses
- Filter by date range
- Sort expenses by amount or date
