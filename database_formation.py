import mysql.connector

#please enter your credentials for login
db= mysql.connector.connect(host='localhost',username='yourusername',password='yourpass',database='Behtar')
mycursor=db.cursor()
#please execute these commands before going ahead
mycursor.execute('create database Behtar')
mycursor.execute('create table Behtardata2 (ID INT, NAME VARCHAR(255), PAYMENT VARCHAR(255), ORDERSTATUS VARCHAR(255), ETA INT)')

# to insert data into table BehtarData
sql = "INSERT INTO Behtardata2 VALUES (%s,%s,%s,%s,%s)"
val = ("1", "Highway 21","Wallet","Delivered","7")
val2 = ("2", "books","Netbanking","dispatched","8")
val3 = ("3", "Goods","Netbanking","Processing","2")
val4 = ("4", "biscuit","Wallet","Dispatched","3")
val5 = ("5", "orange","Cash on Delivery","Processing","4")
val6 = ("6", "Nailpolish","Wallet","Processing","1")
val7 = ("7", "hat","Netbanking","Delivered","2")
mycursor.execute(sql, val)
mycursor.execute(sql, val2)
mycursor.execute(sql, val3)
mycursor.execute(sql, val4)
mycursor.execute(sql, val5)
mycursor.execute(sql, val6)
mycursor.execute(sql, val7)
#just to check
db.commit()
