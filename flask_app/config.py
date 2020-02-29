import os

path = os.path.dirname(os.path.realpath(__file__) )

FLASK_APP = 'smog_monitor'
DATABASE_URI = f'sqlite:////{os.path.join(path, "db.sqlite3")}'


class Config:
    FLASK_APP = FLASK_APP
    FLASK_ENV = True # os.environ.get('FLASK_ENV')
    FLASK_DEBUG = True # os.environ.get('FLASK_DEBUG')
    SECRET_KEY = 'sadgfjnkl9q2348hiur92inlsadfkjf' # os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False # os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
