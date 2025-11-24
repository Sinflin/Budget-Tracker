import mysql.connector as mycon#Importing Mysql.connector module for Functions to connect Mysql

db = mycon.connect(
    host="localhost",
    user="root",
    password="tiger",
    database='budget_tracker'
)#Real connection between Mysql and python

cursor = db.cursor()#Creating a cursor to move in MySql
#------------------------------------
#    All function required
#------------------------------------
def add_expense():#Function for adding the expense in the database
    name = input("Enter the name for the expense: ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD): ")

    query = "INSERT INTO expenses(name, category, amount, date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, category, amount, date))#Executing the Function in Mysql
    db.commit()
    print("Expense added to database successfully")


def view_expense():#Formation of function for viewing the Expenses from MySQL
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()#Fetching the data from MySQL
    if not rows:
        print("No expenses found.")
    for row in rows:
        print(row)


def monthly_total():#Creating function for Monthly Total    
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE MONTH(date) = MONTH(CURDATE())")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("Total Monthly Expense:", total)


def remaining_budget():#Creating a function for showing the reamaining budget
    cursor.execute("SELECT limit FROM budget WHERE mon='November'")
    row = cursor.fetchone()#Fetching a specific value from the database

    if row is None:
        print("No budget set for November.")
        return

    limit_amt = row[0]

    cursor.execute("SELECT SUM(amount) FROM expenses")
    spent = cursor.fetchone()[0]

    if spent is None:
        spent = 0

    print("Remaining:", limit_amt - spent)


def add_budget():# Creating a function for showing the add budget
    mon = input("Enter the Name of the month: ")
    limit = float(input("Enter the monthly limit: "))

    # FIX: correct SQL syntax, correct execute usage
    query = "INSERT INTO budget(mon, limit) VALUES (%s, %s)"
    cursor.execute(query, (mon, limit))
    db.commit()

    print("Budget Added successfully")


# MAIN MENU LOOP
while True:
    print("\n 1.Add Expense")
    print("2.View Expense")
    print("3.View Monthly Total")
    print("4.View Remaining Budget")
    print("5.Add Budget")
    print("6.Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        monthly_total()
    elif choice == 4:
        remaining_budget()
    elif choice == 5:
        add_budget()
    elif choice == 6:
        break
    else:
        print("Type the correct choice")
