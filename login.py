import sys, os
import sqlite3

from create import Create
from dashboard import Dashboard

conn = sqlite3.connect('Lego.db')
c = conn.cursor()

class Login:
    global level
    def __init__():
        pass

    #Perform login function
    #Checks to make sure username
    #and password are in database
    def login_menu():
        print("Username: ")
        user = input(" >> ")
        print("Password: ")
        passw = input(" >> ")
        c.execute('SELECT * FROM Customers WHERE Username = ? AND Password = ?', (user, passw))
        account = c.fetchone()
        c.execute('SELECT * FROM Employee WHERE EmployeeID = ? AND Password = ?', (user,passw))
        store = c.fetchone()

        if account:
            print("Logged in Successfully")
            print("Welcome: ", user)
            Dashboard.dashboard_menu()
        elif store:
            print("Entering store mode.")
            print("Logged in successfully.")
            c.execute('Select Level FROM Employee WHERE EmployeeID = ? AND Password = ?', (user, passw))
            result = c.fetchone()
            for Login.level in result:
                print(Login.level)
            Admin.admin_menu()
        else:
            print("Invalid username/password")
            Login.login_menu()

#Class that is used when operating
#in store mode. This mode is only
#used for employees with limited
#access for normal workers.
class Admin:
    def __init__():
        pass
    #Displays admin menu
    def admin_menu():
        print("Menu")
        print("======")
        print("1. Add, change, or delete employee info.")
        print("2. Order, reorder, or stop orders")
        print("3. View Reports ")
        print("4. Logout")
        option = input(" >> ")

        if option == "1":
            Admin.info_menu()
        elif option == "2":
            order.menu()
        elif option == "3":
            report_menu()
        elif option == "4":
            quit()
        else:
            print("Option not available")
            Admin.admin_menu()

    def info_menu():
        print("What would you like to do?")
        print("1. Add Employee")
        print("2. Change Employee info")
        print("3. Delete Employee")
        print("4. Go back")
        option = input(" >> ")
        #Checks to make sure if the current user is an admin
        if option == "1":
            if Login.level == "admin":
                print("Input new employee information.")
                print("Employee ID: ")
                add_id = input(" >> ")
                print("Last Name: ")
                add_last = input(" >> ")
                print("First Name: ")
                add_first = input(" >> ")
                print("Password: ")
                add_passw = input(" >> ")
                print("Store: ")
                add_store = input(" >> ")
                print("Level: ")
                add_level = input(" >> ")
                sql = '''INSERT INTO Employee (EmployeeID, Last, First, Password, StoreNum, Level)
                        VALUES(?,?,?,?,?,?)'''
                c.execute(sql, (add_id, add_last, add_first, add_passw, add_store, add_level))
                conn.commit()
            else:
                print("Access Denied")
                Admin.admin_menu()
    def order_menu():
        pass
    def report_menu():
        pass
