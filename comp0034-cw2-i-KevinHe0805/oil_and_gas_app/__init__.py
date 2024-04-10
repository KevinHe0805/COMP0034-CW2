from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dash_app.src.gas_oil_dash_app import create_dash_app
from flask_login import LoginManager

# Iris app folder
PROJECT_ROOT = Path(__file__).parent

# Create a global SQLAlchemy object
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_object=None):
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config["SECRET_KEY"] = "MM6nFY1nZzY83cE3XdJk7w"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "oil_and_gas.db")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False

    # Bind the Flask-SQLAlchemy instance to the Flask app
    db.init_app(app)
    login_manager.init_app(app)
    create_dash_app(app)

    # Include the routes from routes.py
    with app.app_context():
        from . import routes
        # Create the tables in the database if they do not already exist
        from .models import Source, User
        from oil_and_gas_app.bp_error import error_bp

        db.create_all()
        app.register_blueprint(error_bp)
    return app
