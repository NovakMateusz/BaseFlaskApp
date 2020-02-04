from flask import Blueprint, render_template


page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
@page.route('/home')
def home():
    return render_template("page/home.html")


@page.route('/pricing')
def pricing():
    return render_template('page/pricing.html')
