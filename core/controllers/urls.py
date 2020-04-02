from flask import render_template
from core import app


@app.route('/')
def index():
    return home()


@app.route('/home/')
def home():
    return render_template('home.html')
