import sys, os
import sqlite3

from login import Login
from create import Create

#Connect and create Lego database
conn = sqlite3.connect('Lego.db')
c = conn.cursor()

#Function that executes sql scripts
def executeScriptsFromFile(filename):
        fd = open(filename, 'r')
        sqlFile = fd.read()
        c.executescript(sqlFile)
        fd.close()

executeScriptsFromFile('table.sql')
executeScriptsFromFile('data.sql')
c.close()
conn.close()



def main_menu():
	print(" Legos ")
	print("=========")
	print("1. Login")
	print("2. Create Account")
	print("3. Quit")
	choice = input(" >> ")
	exec_menu(choice)

	return

#Menu that displays options
#For the user to perform
def exec_menu(choice):
	if choice == "1":
		Login.login_menu()
	elif choice == "2":
		create_menu()
	elif choice == "3":
		quit()
	else:
		print("Choose a valid choice from the menu")
		choice = input(" >> ")
		exec_menu(choice)



#Executes main function
if __name__ == "__main__":
	main_menu()
	
