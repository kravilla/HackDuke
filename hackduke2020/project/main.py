import csv
from _csv import reader

from flask import Blueprint, render_template
from flask_login import current_user, login_required
import os
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('/index.html')


@login_required
@main.route('/profile')
def profile():
    courses = []
    with open('Static/UCoursera_Courses.csv', 'r', errors='ignore') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            for s_norm in row:
                s_lower = s_norm.lower()
                if str(current_user.pref1).lower() in s_lower:
                    courses.append(s_norm)
                elif str(current_user.pref2).lower() in s_lower:
                    courses.append(s_norm)
                elif str(current_user.pref3).lower() in s_lower:
                    courses.append(s_norm)
                elif str(current_user.pref4).lower() in s_lower:
                    courses.append(s_norm)
                elif str(current_user.pref5).lower() in s_lower:
                    courses.append(s_norm)

    return render_template('/profile.html', name=current_user.name, courses=courses)
