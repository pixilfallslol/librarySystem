# Step 1 import sqlite3 lib.

import sqlite3

# Step 2 

connection = sqlite3.connect("my_database.db")

# Step 3 cursor object is used to perform actions on the database.

cursor = connection.cursor()

# Step 4

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, DOB TEXT)")

# Step 5 insert data.

cursor.execute("INSERT INTO students VALUES (101, 'John', '1/1/2010')")

# Step 6 make a commit.

connection.commit()

# Running queries.

cursor.execute("SELECT * FROM students")

print(cursor.fetchall())

# Final step

connection.close()