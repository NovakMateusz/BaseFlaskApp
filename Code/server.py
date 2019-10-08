from app import app
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


if __name__ == '__main__':
    clear_photos_folder(app)
    app.run(debug=True)
