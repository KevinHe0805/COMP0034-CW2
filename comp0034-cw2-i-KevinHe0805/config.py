from pathlib import Path

# Sets the project root folder
PROJECT_ROOT = Path(__file__).parent


class Config:
    """Base configuration class."""

    SECRET_KEY = "MM6nFY1nZzY83cE3XdJk7w"
    # configure the SQLite database location

# configure the SQLite database location
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "oil_and_gas.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProdConfig(Config):
    """Production config.

    Not currently implemented.
    """

    pass


class DevConfig(Config):
    """Development config"""

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    """Testing config"""

    TESTING = True
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False
