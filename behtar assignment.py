#aditya kumar singh
# behtar assignment
#executing db
# import database_formation  use this to import database program and get all the prerequisites
import mysql.connector
#please enter your credentials
db= mysql.connector.connect(host='localhost',username='urusername',password='urpass',database='Behtar')
mycursor=db.cursor()

p1='Netbanking'
p2='Wallet'
p3='Cash on Delivery'
p4='payment failed'
s1='Processing'
s2='dispatched'
s3='Delivered'

def update():
    oid=input("Order ID: ")
    y=int(input('\n\nOrder received at: \n1.Seller \n2.Courier \n3.Customer'))
    sql = "UPDATE Behtardata2 SET ORDERSTATUS = %s where ID=%s"
    if y==1:
        status=s1
    elif y==2:
        status=s2
    else:
        status=s3
    updated=(status,oid)
    mycursor.execute(sql,updated);
    db.commit()

def status():
    a=int(input('1.New order? \n2.Update \n3. Customer- Want to track order status'))
    if a==1:
       x=int(input('\nPayment Type: \n1.Netbanking\n2. Wallet \n3. Cash on Delivery \n4. Failed'))
       #execute sql command for new order
       oid=input('Enter orderId')
       name=input('Item: ')
       eta=input("ETA= ")
       sql='insert into Behtardata2 values (%s,%s,%s,%s,%s)'
       if x==1:
           z=p1
       elif x==2:
           z=p2
       elif x==3:
           z=p3
       else:
           z=p4
       values= (oid,name,z,"Waiting for seller to verify",eta)
       mycursor.execute(sql,values)
       db.commit()
    elif a==2:
        update()
    elif a==3:
        oid=input('Enter order id: ')
        c=(oid,)
        sql= 'select * from Behtardata2 where ID=%s'
        mycursor.execute(sql,c)
        b=mycursor.fetchall()
        for x in b:
            print(x)
    else:
        print("Wrong choice, Try again")
        return status()

status()

i=int(input('Another order? \n1.Yes \n2. No'))
if i==1:
    status()
else:
    pass

# just a try for generating ids
'''mycursor.execute('select count(*) from Behtardata2')
a=mycursor.fetchall()
print(type(a))
#i = ''.join(map(str, a))
print(i)
#print(t)'''


