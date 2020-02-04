from flask import Flask

from base_app.blueprints.page import page
from base_app.extensions import debug_toolbar


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    """
    debug_toolbar.init_app(app)


def create_app():
    """
    Create a Flask app, using the application factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)
    extensions(app)
    return app

