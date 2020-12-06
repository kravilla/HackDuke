from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String(), unique=False)
    name = db.Column(db.String(), unique=False)
    isMentor = db.Column(db.Boolean(), default=False)
    location = db.Column(db.String(), unique=False)
    pref1 = db.Column(db.String(), unique=False)
    pref2 = db.Column(db.String(), unique=False)
    pref3 = db.Column(db.String(), unique=False)
    pref4 = db.Column(db.String(), unique=False)
    pref5 = db.Column(db.String(), unique=False)

    def __init__(self, email, username, password, name, isMentor, location, pref1, pref2, pref3, pref4, pref5):
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.isMentor = isMentor
        self.location = location
        self.pref1 = pref1
        self.pref2 = pref2
        self.pref3 = pref3
        self.pref4 = pref4
        self.pref5 = pref5

    def __repr__(self):
        return ""


class Preferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    pref1 = db.Column(db.String(), unique=False)
    pref2 = db.Column(db.String(), unique=False)
    pref3 = db.Column(db.String(), unique=False)
    pref4 = db.Column(db.String(), unique=False)
    pref5 = db.Column(db.String(), unique=False)

    def __init__(self, username):
        self.username = username
