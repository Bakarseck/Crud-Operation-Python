# install mysql-connector-python

import mysql.connector

# Define a variable mysqldb for connection
mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="crudPython")

# Connect for the cursor for the database
mysqlcursor = mysqldb.cursor()

# create a table
#mysqlcursor.execute("create table studentrecord(rollno INT, name varchar(30), marks int)")

# insert into table
mysqlcursor.execute("insert into studentrecord(rollno, name, marks) values(1, 'Bakar', 20)")
print("Record inserted into the table")
mysqldb.commit()

mysqldb.close()