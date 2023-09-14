# Python code for creating Table in the Database 
# Host: It is the server name. It will be "localhost" 
# if you are using localhost database 

import sqlite3


conn = sqlite3.connect('mytest.db')
c = conn.cursor()

def executeScriptsFromFile(filename):
	fd = open(filename, 'r')
	sqlFile = fd.read()
	c.executescript(sqlFile)
	fd.close()

def test():
	pass

 
executeScriptsFromFile('test.sql')
c.close()
conn.close()

print("Completed.")
