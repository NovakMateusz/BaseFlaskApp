import os
from uuid import uuid4


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(uuid4())
    UPLOAD_FOLDER_PREFIX = 'Code/app/static'
    STATIC_UPLOAD_FOLDER = 'uploads/images'
    ALLOWED_PHOTO_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
