from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String(), unique=False)
    name = db.Column(db.String(), unique=False)
    isMentor = db.Column(db.Boolean(), default=False)

    def __init__(self, email, username, password, name, isMentor):
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.isMentor = isMentor

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
