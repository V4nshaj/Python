
# ----Example Python Program to create tables in-memory databases----

 

# Import the sqlite3 module

import sqlite3

 

# Create database connection to an in-memory database

connectionObject    = sqlite3.connect(":memory:")

 

# Obtain a cursor object

cursorObject        = connectionObject.cursor()

 

# Create a table in the in-memory database

createTable = "CREATE TABLE EMP(id int, FirstName varchar(32), LastName varchar(32), dept int)"

cursorObject.execute(createTable)

 

# Print the tables 

 

# .tables command will not work as it is not SQL...hence querying the SQLite_master

cursorObject.execute("select * from SQLite_master where type=\"table\"")

 

print("Tables available in the in-memory database(main):")

tables = cursorObject.fetchall()

 

print("Listing tables from SQLite_master:")

for table in tables:

    print("------------------------------------------------------")

    print("DB Object Name: %s"%(table[0]))

    print("Name of the database object: %s"%(table[1]))

    print("Table Name: %s"%(table[2]))

    print("Root page: %s"%(table[3]))

    print("SQL statement: %s"%(table[4]))

    print("------------------------------------------------------")

connectionObject.close()