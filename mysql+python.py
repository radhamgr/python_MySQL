# python_MySQL

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="****",
  )
  
#create database

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE People")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

mydb = mysql.connector.connect(
host = "localhost",
user = "username",
passwd = "****",
database="People"
)

# create table
mycursor.execute("create table customer (ID int auto_increment primary key,name varchar(255), address varchar(255))")
mycursor.execute("show tables")
for i in mycursor:
    print(i)

#insert values
sql = "insert into customer(name,address) values (%s,%s)"
val = ("john","highway 21")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "insert into customer(name,address) values (%s,%s)"
val = [
 ('Peter', 'Lowstreet 4'),
 ('Amy', 'Apple st 652'),
 ('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
 ('Sandy', 'Ocean blvd 2'),
 ('Betty', 'Green Grass 1'),
 ('Richard', 'Sky st 331'),
 ('Susan', 'One way 98'),
 ('Vicky', 'Yellow Garden 2'),
 ('Ben', 'Park Lane 38'),
 ('William', 'Central st 954'),
 ('Chuck', 'Main Road 989'),
 ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql,val)
mydb.commit()
print("1 record inserted. ID:",mycursor.lastrowid)

#check the table
mycursor.execute("select * from customer")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

#delete command
sql = "DELETE FROM customer WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

#update command
sql = "UPDATE customer SET address = %s WHERE address = %s"
val = ("Canyon 123","Valley 345")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

mycursor.execute("select * from customer")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

