from flask import Flask,request, render_template,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(_name_)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "ccc"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "Venmathi@0706"
app.secret_key="myapp"

conn = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def login():
    
    if request.method  == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
        con=conn.connection.cursor()
        sql = "select uname, pwd from login WHERE uname= %s and  pwd=%s"
        result=con.execute(sql,(uname,pwd))
        if result:
            return render_template('sameer.html')
        else:
            return render_template('login.html')
            
        
    return render_template('login.html')