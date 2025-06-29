from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    app.config['SECRET_KEY'] = 'uma-chave-secreta-supersegura'

    csrf.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app