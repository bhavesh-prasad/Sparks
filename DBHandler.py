
import sqlite3 as sql
con=sql.connect('Database.db')
cur=con.cursor()
cur.execute('Create table if not exists USERS ( uid integer primary key AUTOINCREMENT, fname text , lname text , credit_number number ) ')
cur.execute('Create table if not exists LOGS (  TRANSACTION_ID integer primary key AUTOINCREMENT, Sender text  , Reciever text ,credit_number number)')
if cur.execute('Select count(*) from Users').fetchall()[0][0]==0:    
    cur.execute('Insert into users(fname,lname,credit_number) values("Bhavesh" , "Prasad", 1000 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Aditya" , "Akash", 500 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Alex" , "Roy", 5200 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Frank" , "Borne", 1500 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Summer" , "Stay", 5300 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("John" , "Doe", 7500 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Alex" , "Teidmann", 4500 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Regina" , "Filangae",2500 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Joey" , "Tribi", 3500 )') 
    cur.execute('Insert into users(fname,lname,credit_number) values("Ash" , "Bourne", 2500 )') 
    con.commit()

# def insertTransaction(from_user,to_user,amount):
#     cur.execute('Insert into logs(sender,reciever,credit) values(?,?,?)',(from_user,to_user,amount))
#     con.commit 