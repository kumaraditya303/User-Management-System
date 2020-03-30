from Data_Collector import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    password = db.Column(db.String(128))
    phone=db.Column(db.String(10))
    gender=db.Column(db.String(1))
