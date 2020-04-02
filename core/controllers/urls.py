from flask import render_template
from core import app


@app.route('/')
@app.route('/login/')
def index():
    return render_template('login.html')


@app.route('/cadastro/')
def signup():
    return render_template('signup.html')


@app.route('/home/')
def home():
    return render_template('home.html')
