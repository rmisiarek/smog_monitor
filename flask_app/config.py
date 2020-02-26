import os

path = os.path.dirname(os.path.realpath(__file__) )
database_path = os.path.join(path, 'smog_db.sqlite3')

flask_app_name = 'smog_monitor'


class Config:
    FLASK_APP = flask_app_name
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = f'sqlite:////{database_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
