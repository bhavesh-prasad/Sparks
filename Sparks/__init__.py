from flask import Flask,flash,render_template,request,redirect,url_for
import sqlite3 as sql
app= Flask(__name__, template_folder='Templates')
import DBHandler as db
import os
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
@app.route('/home')
def Home():
   con=sql.connect('Database.db')
   cur=con.cursor()
   det=cur.execute('Select * from Users')
   return render_template('Home.html',users=det)

@app.route('/logs')
def logs():
   con=sql.connect('Database.db')
   cur=con.cursor()
   log=cur.execute('Select * from logs').fetchall()
   return render_template('Logs.html',user_logs=log)

@app.route('/users',methods=['GET','POST'])
def users():
   if request.method== 'POST':
      con=sql.connect('Database.db')
      cur=con.cursor()
      reciever_id = request.form.get("Reciever_id")
      credit = request.form.get("Credit")
      if credit=='' or reciever_id=='':
         flash("Please Enter complete information")
         return render_template('TransferCredit.html')
      if reciever_id==request.args.get('uid'):
         flash("You cannot send money to yourself")
         return render_template('TransferCredit.html')      
      if cur.execute("select credit_number from users where uid=(?)",(request.args.get('uid'))).fetchone()[0]<int(credit):
         flash("You don't have that much amount of credit to send")
         return render_template('TransferCredit.html')
      if int(credit)<=0:
         if int(credit)==0:
            flash("You cannot Send zero credit")
         else:
            flash("Please enter positive Credit Value")
         return render_template("TransferCredit.html")
      # temp= cur.execute('Select count(*) from users where uid =(?)',(reciever_id,)).fetchone()
      if cur.execute('Select count(*) from users where uid =(?)',(reciever_id,)).fetchone()[0]==0:
         flash("Please enter a valid uid")
         return render_template("TransferCredit.html")
      cur.execute("update users set credit_number =credit_number +(?) where uid=(?)",(credit,reciever_id))
      cur.execute("update users set credit_number =credit_number -(?) where uid=(?)",(credit,request.args.get('uid')))
      sender_name=cur.execute("Select fname,lname from users where uid=(?)",(request.args.get('uid'),)).fetchall()
      reciever_name=cur.execute("Select fname,lname from users where uid=(?)",(reciever_id,)).fetchall()
      cur.execute('insert into logs(sender,reciever,credit_number) values(?,?,?) ',(sender_name[0][0]+" "+sender_name[0][1],reciever_name[0][0]+" "+reciever_name[0][1],credit))
      try:
         con.commit()
      except e:
         flash("There was some error updating the Database")
         return render_template("TransferCredit.html")
      flash("Credit Transfer Successful")
      return redirect(url_for('Home'))
   return render_template('TransferCredit.html')

if __name__ == "__main__":
   os.system('python3 DBHandler.py')
   app.run()