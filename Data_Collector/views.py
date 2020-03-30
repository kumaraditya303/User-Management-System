from datetime import *
from random import *

from flask import *
from flask_mail import *
from werkzeug.security import *

from Data_Collector import app, db
from Data_Collector.models import User
mail = Mail(app)

tp = randint(000000, 999999)
@app.route('/')
def home():
    return render_template('datacollect.html')


@app.route('/otp')
def otp():
    return render_template('otp.html')


@app.route('/data', methods=["GET"])
def data():
    rows = User.query.all()
    return render_template("data.html", rows=rows)


@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    msg = Message('OTP', sender='siddhishanu97@gmail.com', recipients=[email])
    msg.body = 'Your OTP for logging is ' + str(tp)+"\nTime: "+str(datetime.now())
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
    id = request.form['id']
    row = User.query.filter_by(id=id).first()
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
        user = User(username=name, password=password,
                    email=email, phone=str(phone), gender=gender)
        db.session.add(user)
        db.session.commit()
        ids = User.query.filter_by(username=name, password=password,
                                   email=email, phone=str(phone), gender=gender).first().id

        msg = Message('Data Collected Successfully',
                      sender='Data Collector', recipients=[email])
        msg.html = render_template(
            'mail.html', name=name, password=password, email=email, phone=phone, gender=gender, id=ids, time=str(datetime.now()))
        mail.send(msg)

        return render_template("result.html", name=name, password=password, email=email, phone=phone, gender=gender)

