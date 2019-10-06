from app import app
from flask import render_template, url_for


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')
