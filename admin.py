import sys, os
import sqlite3

conn = sqlite3.connect('Lego.db')
c = conn.cursor()

class Admin:
    def __init__():
        pass

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

        if option == "1":
            if level == "admin":
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
                c.execute('INSERT INTO Employee (EmployeeID, Last, First, Password, StoreNum, Level) Values (?, ?, ?, ?, ?, ?)', (add_id, add_last, add_first, add_passw, add_store, add_level))
            else:
                print("Access Denied")
                admin.admin_menu()
    def order_menu():
        pass
    def report_menu():
        pass
