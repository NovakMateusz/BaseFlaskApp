from Code.app import app
import os
import glob


def clear_photos_folder(app):
    path = os.path.join(
        app.config['UPLOAD_FOLDER_PREFIX'],
        app.config['STATIC_UPLOAD_FOLDER'],
        '*')
    files = glob.glob(path)
    for file in files:
        os.remove(file)


def create_app():
    clear_photos_folder(app)
    return app
