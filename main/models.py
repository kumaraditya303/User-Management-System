from main import UserMixin, db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    fname = db.Column(db.String(64))
    mname = db.Column(db.String(64))
    dob = db.Column(db.String(12))
    email = db.Column(db.String(120))
    password = db.Column(db.String(128))
    phone = db.Column(db.String(10))
    gender = db.Column(db.String(1))
    active = db.Column(db.DateTime())
    photo = db.Column(db.LargeBinary)
    role = db.Column(db.String(5))
