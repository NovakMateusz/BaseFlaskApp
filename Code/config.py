import os
from uuid import uuid4


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(uuid4())
