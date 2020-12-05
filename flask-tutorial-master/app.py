from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/students/')
def names():
    return render_template(
        'students.html', 
        students=[
            { "name": "Anna", "graduating_class": "2022" },
            { "name": "Lorne", "graduating_class": "2022" },
            { "name": "Maryam", "graduating_class": "2023" },
            { "name": "Vaishvi", "graduating_class": "2023" }])