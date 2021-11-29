"""
Factory file for create app 
"""

from constants import db, migrate
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret string'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:new_password@localhost/conference'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    return app