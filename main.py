# Connect Python to MySQL using MySQL Connector

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Thor1225!"
)

print(mydb)

# Show databases on the MySQL Server

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# Drop menegarie database if it exists

mycursor.execute("DROP DATABASE IF EXISTS menagerie")

# Create menagerie database

mycursor.execute("CREATE DATABASE menagarie")
mycursor.execute("USE menagerie")

# Create pets table

mycursor.execute("CREATE TABLE pets (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death Date)")

# Show structure of pet table

mycursor.execute("DESCRIBE pets")

for x in mycursor:
    print(x)

# Insert records to table

sql = "INSERT INTO pets (name, owner, species, sex, birth, death) VALUES (%s,%s,%s,%s,%s,%s)"
val = [
    ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', None),
    ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', None),
    ('Buffy', 'Harold', 'dog', 'f', '1989-05-13', None),
    ('Fang', 'Benny', 'dog', 'm', '1990-08-27', None),
    ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29'),
    ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', None),
    ('Whistler', 'Gwen', 'cat', None, '1997-12-09', None),
    ('Slim', 'Benny', 'snake', 'm', '1996-04-29', None),
    ('Puffball', 'diane', 'hamster', 'f', '1998-03-30', None)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

# Display all records in pets table

mycursor.execute("SELECT * FROM pets")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Show records of female dogs in the pets table

mycursor = mydb.cursor()

sql = "SELECT * FROM pets WHERE sex ='f'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
   print(x)

# Show name and birth columns from the pets table

mycursor.execute("SELECT name, birth FROM pets")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Show how many pets each owner has

mycursor.execute("SELECT owner, COUNT(*) FROM pets GROUP BY owner")

for x in myresult:
    print (x)

# Show name, birth and month(birth) from pets table

mycursor.execute("SELECT name, birth, MONTH(birth) FROM pets ")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
