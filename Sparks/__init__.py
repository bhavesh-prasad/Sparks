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

@app.route('/users',methods=['GET','POST'])
def users():
   if request.method== 'POST':
      con=sql.connect('Database.db')
      cur=con.cursor()
      reciever_id = request.form.get("Reciever_id")
      credit = request.form.get("Credit")
      if reciever_id==request.args.get('uid'):
         flash("You cannot send money to yourself")
         return render_template('TransferCredit.html')      
      cur.execute("update users set credit_number =credit_number +(?) where uid=(?)",(credit,reciever_id))
      cur.execute("update users set credit_number =credit_number -(?) where uid=(?)",(credit,request.args.get('uid')))
      cur.execute('insert into logs(sender,reciever,credit_number) values(?,?,?) ',(request.args.get('uid'),reciever_id,credit))
      con.commit()
      return redirect(url_for('Home'))
   return render_template('TransferCredit.html')


if __name__ == "__main__":
   os.system('python3 DBHandler.py')
   app.run()