===============================================================
                        PROJECT DOCUMENTATION
===============================================================

NAME                : ADITYA VISHWAKARMA
REGISTRATION NUMBER : 25BCY10123
COLLEGE             : VIT BHOPAL UNIVERSITY

===============================================================
                   B U D G E T   T R A C K E R
                 Python + MySQL Complete Project
===============================================================

INTRODUCTION
------------
Managing personal finances is a critical life skill. This project provides
a clean, interactive, and beginner‑friendly **Budget Tracking System** using
Python and MySQL. It allows users to store expenses, categorize them,
calculate monthly spending, set budgets, and view the remaining balance.
The system is built with simple functions, making it easy to understand,
modify, and extend.

This project demonstrates:
- Database connectivity in Python
- CRUD operations using MySQL
- Function‑based modular programming
- Menu‑driven CLI interface
- Real‑world problem solving with Python

===============================================================
                        PROJECT FEATURES
===============================================================

1. ADD EXPENSE
   - Adds a new expense into the database.
   - Inputs: name, category, amount, date.
   - Automatically stores data into the *expenses* table.

2. VIEW EXPENSES
   - Displays all stored expenses.
   - Shows every row directly from MySQL.
   - Useful for reviewing all past spending.

3. MONTHLY TOTAL
   - Calculates how much money is spent in the current month.
   - Uses MySQL’s *MONTH()* function.
   - Helps track monthly financial discipline.

4. REMAINING BUDGET
   - Retrieves set monthly budget from the *budget* table.
   - Subtracts total expenses to show how much is left.
   - Prevents overspending and improves financial awareness.

5. ADD BUDGET
   - Allows the user to set a budget limit for any month.
   - Input: month name, monthly amount.
   - Stores the budget into MySQL.

6. EXIT
   - Ends the program safely.

===============================================================
                    DATABASE REQUIREMENTS
===============================================================

The project requires a MySQL database named **budget_tracker**.

TABLE 1: expenses
-----------------
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    amount FLOAT,
    date DATE
);

TABLE 2: budget
---------------
CREATE TABLE budget (
    mon VARCHAR(20),
    `limit` FLOAT
);

===============================================================
                   HOW THE PROGRAM WORKS
===============================================================

1. The system connects to MySQL using:
       mysql.connector

2. When the user selects a menu option, the corresponding function runs.

3. Each function:
   - Sends SQL queries to the database.
   - Performs INSERT, SELECT, or SUM operations.
   - Displays meaningful results.

4. Data is committed using:
       db.commit()

5. The menu runs in an infinite loop until the user chooses Exit.

===============================================================
                  PROGRAM FLOW (STEP BY STEP)
===============================================================

1. Display menu options.
2. User selects an option (1‑6).
3. Input is taken when necessary.
4. SQL queries execute via cursor object.
5. Program prints results:
   - Added expense
   - Table records
   - Monthly total
   - Remaining budget
6. Loop repeats.

===============================================================
                    EXAMPLE USER SESSION
===============================================================

User selects: Add Expense  
Input:  
    Name     -> Coffee  
    Category -> Food  
    Amount   -> 120  
    Date     -> 2025‑10‑21  

Output:  
    Expense added successfully.

User selects: View Expenses  
Output:  
    (1, 'Coffee', 'Food', 120, '2025‑10‑21')

User selects: Monthly Total  
Output:  
    Total Monthly Expense: 120

User selects: Remaining Budget  
Output:  
    Remaining: (Budget Limit - Total Spent)

===============================================================
                  HOW TO SETUP & RUN THE PROJECT
===============================================================

1. Install MySQL Server.
2. Create the database using:
       CREATE DATABASE budget_tracker;

3. Create the tables mentioned above.
4. Install the required Python package:
       pip install mysql-connector-python

5. Save the Python program as:
       budget_tracker.py

6. Run the program using:
       python budget_tracker.py

===============================================================
                     SUGGESTED IMPROVEMENTS
===============================================================

You can extend the project further by adding:
- Category‑wise monthly report
- Pie charts using matplotlib
- Export expenses to CSV
- GUI interface using Tkinter or PyQt
- Login system for multiple users
- Alerts if budget limit is crossed

===============================================================
                      PROJECT SUMMARY
===============================================================

This Budget Tracking System is a practical and beginner-friendly project
that demonstrates real database usage with Python. It teaches CRUD operations,
SQL handling, financial logic, and Modular Programming.  
Perfect for college submissions, practice, or personal improvement.

===============================================================
                        END OF DOCUMENT
===============================================================
