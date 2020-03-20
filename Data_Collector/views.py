import os
import sqlite3 as sql
from datetime import *
from random import *

from flask import *
from flask_mail import *
from werkzeug.security import *

# os.system('clear')
app = Flask(__name__) 
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'siddhishanu97@gmail.com'
app.config['MAIL_PASSWORD'] = 'siddhi-12345'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db = sql.connect("data.db")
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS data ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT , username VARCHAR(255) NOT NULL , password VARCHAR(255) NOT NULL , gender VARCHAR(1) NOT NULL , phone VARCHAR(10) NOT NULL , email VARCHAR(255) NOT NULL )')
cursor.close()
db.commit()
db.close()
tp = randint(000000, 999999)
@app.route('/')
def student():
    return render_template('datacollect.html')


@app.route('/otp')
def otp():
    return render_template('otp.html')


@app.route('/data', methods=["GET"])
def data():
    db = sql.connect("data.db")
    db.row_factory = sql.Row
    cursor = db.cursor()
    cursor.execute("select * from data")
    rows = cursor.fetchall()
    cursor.close()
    db.commit()

    return render_template("data.html", rows=rows)


@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    msg = Message('OTP', sender='siddhishanu97@gmail.com', recipients=[email])
    msg.body = 'Your OTP for logging is ' + \
        str(tp)+"\nTime: "+str(datetime.now())
    mail.send(msg)
    return render_template('verify.html')


@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form['top']

    if tp == int(user_otp):
        return redirect(url_for('data'))
    else:
        return render_template('reverify.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/searchresult', methods=['POST'])
def searchresult():
    ids = request.form['id']
    db = sql.connect("data.db")
    db.row_factory = sql.Row
    cursor = db.cursor()
    cursor.execute("select * from data")
    row = cursor.fetchone()
    cursor.close()
    db.commit()
    while(row != None):
        return render_template('searchresult.html', row=row, t='F')
    return render_template('searchresult.html', row=row, t='T')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        # password=generate_password_hash(password,method='sha256')
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        db = sql.connect("data.db")
        cursor = db.cursor()
        proj = (name, password, email, str(phone), gender)
        cursor.execute(
            "INSERT INTO data (username,password,email,phone,gender) VALUES (?,?,?,?,?)", proj)
        db.commit()
        cursor.execute("SELECT id FROM data ORDER BY id DESC LIMIT 1;")
        ids = cursor.lastrowid
        msg = Message('Data Collected Successfully',
                      sender='Data Collector', recipients=[email])
        msg.html = render_template(
            'mail.html', name=name, password=password, email=email, phone=phone, gender=gender, id=ids, time=str(datetime.now()))
        mail.send(msg)
        db.commit()
        return render_template("result.html", name=name, password=password, email=email, phone=phone, gender=gender)
app.run(debug=True)
