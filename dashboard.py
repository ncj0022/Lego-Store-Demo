import sys, os
import sqlite3

conn = sqlite3.connect('Lego.db')
c = conn.cursor()

#Cart that holds all things you wish to order
cart = []
class Dashboard:
    def __init__():
        pass

    #Dashboard that has main options available
    #This includes searching, browsing, ordering, and checking out
    #Can also logout
    def dashboard_menu():
        print("Options: ")
        print("=========")
        print("1. Browse Lego Store")
        print("2. Search Lego Store")
        print("3. Order")
        print("4. Checkout")
        print("5. Logout")
        option = input(" >> ")

        if option == "1":
            c.execute('SELECT BrickNum, Name, Price FROM Bricks')
            browse = c.fetchall()
            for x in browse:
                print(x)
            Dashboard.select_menu()
        elif option == "2":
            print("Search: ")
            criteria = input(" >> ")
            c.execute("Select BrickNum, Name, Price FROM Bricks WHERE Description Like ?", ('%'+criteria+'%',))
            search = c.fetchall()
            for x in search:
                print(x)
            Dashboard.select_menu()
        elif option == "3":
            print("Enter the Brick or Set ID number you wish to order: ")
            id_num = input(" >> ")
            c.execute('Select BrickNum, Name, Price FROM Bricks WHERE BrickNum = ?', (id_num))
            order = c.fetchone()
            print("How many do you wish to order?")
            num = int(input(" >> "))
            for num in order:
                cart.append(order)
            Dashboard.dashboard_menu()
        elif option == "4":
            quit()
        elif option == "5":
            quit()
        else:
            print("Option not available.")
            Dashboard.dashboard_menu();

    #Function that lets you select
    #Certain item for more info
    #or to add to order cart.
    def select_menu():
        print("Would you like to view anything from the results? Yes or No.")
        choice = input(" >> ")
        if choice == "Yes" or choice == "yes":
            print("Enter the id number: ")
            num = input(" >> ")
            c.execute('Select * FROM Bricks WHERE BrickNum = ?',(num,))
            select = c.fetchone()
            print(select)
            Dashboard.dashboard_menu()
        elif choice == "No" or choice == "no":
            Dashboard.dashboard_menu()

