Budget Tracker (Python + MySQL)

A command-line based budget and expense tracking system built with Python and MySQL.
This application allows users to add expenses, set monthly budgets, calculate monthly
totals, and check remaining budget amounts.

Features:
- Add new expenses
- View all expenses
- Calculate current month’s total spending
- Add monthly budget
- Check remaining budget
- MySQL-backed persistent storage
- Simple interactive CLI menu

Requirements:
pip install mysql-connector-python

Database Setup:
CREATE DATABASE budget_tracker;
USE budget_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    amount FLOAT,
    date DATE
);

CREATE TABLE budget (
    mon VARCHAR(20),
    limit FLOAT
);

How to Run:
1. Update MySQL connection details inside main.py.
2. Run: python main.py
3. Use the menu to interact with the program.

Notes:
- Monthly totals are calculated based on the current system month.
- The program handles empty budgets/expenses safely.
- Pure CLI-based system.
