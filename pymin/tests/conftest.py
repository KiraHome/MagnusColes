import os


class TestConfig(object):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'JustaSecret')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/FlaskTest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True