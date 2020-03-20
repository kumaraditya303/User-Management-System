import os
from datetime import *
from functools import wraps

from flask import *
from flask_login import current_user, login_required, login_user, logout_user

from main import app, db, login_manager
from main.models import User


def requires_admin(roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not current_user.role == roles:

                return unauthorized()
            return f(*args, **kwargs)
        return wrapped

    return wrapper


def write_photo(image, name):
    with open('main/static/'+name, 'wb') as file:
        file.write(image)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('about.html')


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_user():
    name = request.form['name']
    fname = request.form['fname']
    mname = request.form['mname']
    dob = request.form['dob']
    email = request.form['email']
    password = request.form['password']
    gender = request.form['gender']
    phone = request.form['phone']
    photo = request.files['photo']
    chkusr = User.query.filter_by(email=email).first()
    if not chkusr is None:
        flash(f'User with email {email} already exists!')
        return redirect(url_for('register'))
    else:
        user = User(name=name, fname=fname, mname=mname, dob=dob,
                    email=email, password=password, phone=phone, gender=gender, active=datetime.now(), role='user', photo=photo.read())
        db.session.add(user)
        db.session.commit()
        login_user(user)
    return redirect(f'/dashboard/{email}')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/admin', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
        user = User.query.filter_by(role='admin').first()
        login_user(user)
        return redirect('/admin_dashboard')
    else:
        flash("Incorrect Credentials")
    return redirect(url_for('admin'))


@app.route('/admin_dashboard')
@login_required
@requires_admin('admin')
def admin_dashboard():
    users = User.query.filter_by(role='user').all()
    for user in users:
        if user.role == 'user':
            write_photo(user.photo, user.email+'.jpg')
            user.photo = user.email+'.jpg'

    return render_template('admin_dashboard.html', users=users)


@app.route('/logout_admin', methods=['GET'])
@login_required
@requires_admin('admin')
def logout_admin():
    logout_user()
    os.system('rm main/static/*.jpg')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def loginuser():
    email = request.form['email']
    password = request.form['password']
    chkusr = User.query.filter_by(email=email).first()
    if chkusr is None or not chkusr.password == password:
        flash('Incorrect Credentials')
        return render_template('login.html')
    else:
        user = User.query.filter_by(email=email).first()
        login_user(user)
    return redirect(f'/dashboard/{email}')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    os.remove('main/static/'+current_user.email+'.jpg')
    user = User.query.filter_by(email=current_user.email).first()
    user.active = datetime.now()
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))


@app.route('/dashboard/<email>')
@login_required
def dashboard_user(email):
    user = User.query.filter_by(email=email).first()
    write_photo(user.photo, user.email+'.jpg')
    return render_template('dashboard.html', user=user, photo=user.email+'.jpg')


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauth.html')


@app.route('/logs')
def log():
    return send_file('logs.log', 'text/plain', as_attachment=False)
