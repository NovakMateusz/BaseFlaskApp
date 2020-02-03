from flask import Flask
from Code.config import Config
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'


from Code.app import routes
