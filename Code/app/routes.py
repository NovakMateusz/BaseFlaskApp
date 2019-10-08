from app import app, errors
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, PhotoForm
from flask_login import current_user, login_user, logout_user, login_required
from app.model import User
from werkzeug.utils import secure_filename
import os


def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() \
        in app.config['ALLOWED_PHOTO_EXTENSIONS']


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


def create_paths(filename):
    filepath = os.path.join(
        app.config['STATIC_UPLOAD_FOLDER'],
        filename)
    full_filepath = os.path.join(
        app.config['UPLOAD_FOLDER_PREFIX'],
        filepath)
    return filepath, full_filepath


@app.route('/images', methods=['POST', 'GET'])
@login_required
def images():
    form = PhotoForm()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            filepath, full_filepath = create_paths(filename)
            file.save(full_filepath)
            flash('File successfully uploaded')
            return render_template(
                "file.html", form=form,
                render_image=True, filepath=filepath)
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
    return render_template("file.html", form=form, render_image=False)
