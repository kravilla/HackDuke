from flask import Blueprint, request, flash, url_for, redirect, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

from . import db
from .models import User, Preferences

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('/login.html')


@auth.route('/signup0')
def signup0():
    return render_template('/signup0.html')


@auth.route('/prefs')
def preferences():
    return render_template('/prefs.html')


@auth.route('/prefs', methods=['POST'])
def addPreferences():
    username = request.form.get('username')
    user = Preferences.query.filter_by(username=username).first()
    user.pref1 = request.form.get('pref1')
    user.pref2 = request.form.get('pref2')
    user.pref3 = request.form.get('pref3')
    user.pref4 = request.form.get('pref4')
    user.pref5 = request.form.get('pref5')
    return redirect(url_for('main.profile'))


@auth.route('/signup-student')
def signupStudent():
    return render_template('/signup-student.html')


@auth.route('/signup-mentor')
def signupMentor():
    return render_template('/signup-mentor.html')


@auth.route('/signup-student', methods=['POST'])
def signupStudent_post():
    name = request.form.get('name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signupStudent'))

    new_user = User(name=name, email=email, username=username,
                    password=generate_password_hash(password, method='sha256'), isMentor=False)

    user_prefs = Preferences(username=username)
    db.session.add(new_user)
    db.session.add(user_prefs)
    db.session.commit()

    return redirect(url_for('auth.preferences'))


@auth.route('/signup-mentor', methods=['POST'])
def signupMentor_post():
    name = request.form.get('name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('email')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signupMentor'))

    new_user = User(name=name, email=email, username=username,
                    password=password, isMentor=True)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.preferences'), username)


@auth.route('/login', methods=['POST', 'GET'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user:
        flash('Login credentials not valid.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))
