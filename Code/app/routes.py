from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.model import User


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        form_data = [form.username.data, form.password.data]
        if [user.username, user.password] != form_data:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/images')
@login_required
def images():
    return render_template('file.html')
