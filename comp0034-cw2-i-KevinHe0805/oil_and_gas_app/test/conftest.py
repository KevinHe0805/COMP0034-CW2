import sys

sys.path.append("oil_and_gas_app")
from oil_and_gas_app import create_app, db
import random
import secrets
import pytest
from oil_and_gas_app.models import User
import sys

sys.path.append("oil_and_gas_app")
import config


# Used for the Flask routes tests
@pytest.fixture(scope='module')
def app():
    """Create a Flask app configured for testing"""
    app = create_app(config.TestConfig)
    with app.app_context():
        db.create_all()
        # Add test data to the database
        user1 = User(email='test123@example.com', password='test456')
        db.session.add(user1)
        user2 = User(email='test321@example.com', password='test654')
        db.session.add(user2)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()


# Used for the Flask route tests
@pytest.fixture()
def test_client(app):
    """Create a Flask test test_client"""
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


# Data for any of the tests
@pytest.fixture()
def form_data():

    form_data_price = {
        "type": 3,
        "year": -1,
        "month": 5,
        "day": 6,
    }
    yield form_data_price


def generate_random_email():
    """Create random email addresses for testing with random domain names"""
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    valid_doms = "abcdefghijklmnopqrstuvwxyz"
    login = ""
    server = ""
    dom = ""
    login_len = random.randint(4, 15)
    server_len = random.randint(3, 9)
    dom_len = random.randint(2, 3)
    for i in range(login_len):
        pos = random.randint(0, len(valid_chars) - 1)
        login = login + valid_chars[pos]
    if login[0].isnumeric():
        pos = random.randint(0, len(valid_chars) - 10)
        login = valid_chars[pos] + login
    for i in range(server_len):
        pos = random.randint(0, len(valid_doms) - 1)
        server = server + valid_doms[pos]
    for i in range(dom_len):
        pos = random.randint(0, len(valid_doms) - 1)
        dom = dom + valid_doms[pos]
    email = login + "@" + server + "." + dom
    return email


def generate_random_password():
    """Generate random password using secrets"""
    password_len = random.randint(6, 15)
    password = secrets.token_urlsafe(password_len)
    return password


@pytest.fixture(scope="function")
def random_email():
    """returns a random email as a fixture"""
    return generate_random_email()


@pytest.fixture(scope="function")
def random_password():
    """returns a random password as a fixture"""
    return generate_random_password()
