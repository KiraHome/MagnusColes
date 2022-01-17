import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DevConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'login'

    with app.app_context():
        from . import views, models
        app.register_blueprint(views.bp)

    @app.route('/hello')
    def hello():
        return "kurva anyadat"
    
    return app
