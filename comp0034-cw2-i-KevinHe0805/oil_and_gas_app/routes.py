import pickle
from pathlib import Path
import numpy as np
from flask import (
    render_template,
    current_app as app,
    request, url_for, redirect, flash
)
from oil_and_gas_app.forms import PredictionForm, RegisterForm, LoginForm
from oil_and_gas_app import db
from oil_and_gas_app.models import Source, User
from flask_login import login_user, logout_user, current_user
from sqlalchemy import exc


pickle_file = Path(__file__).parent.joinpath("data", "ml_model.pkl")
MODEL = pickle.load(open(pickle_file, "rb"))


@app.route("/")
def index():
    """Generates the home page."""
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predicted():
    """Create the homepage"""
    form = PredictionForm()

    if form.validate_on_submit():

        # Get all values from the form
        features_from_form = [
            form.year.data,
            form.month.data,
            form.day.data,
            form.type.data,
        ]

        # Make the prediction
        prediction = make_prediction(features_from_form)

        prediction_text = f"Predicted price at selected day: {prediction}"

        return render_template(
            "predict.html", form=form, prediction_text=prediction_text
        )
    return render_template("predict.html", title='Oil and natural gas Prediction', form=form)


@app.get("/predicting")
def predicting():

    type = request.args.get("type")
    year = request.args.get("year")
    month = request.args.get("month")
    day = request.args.get("day")

    prediction = make_prediction(
        [year, month, day, type]
    )

    return prediction


def make_prediction(parameters):

    # Convert to a 2D numpy array with float values, needed as input to the model
    input_values = np.asarray([parameters], dtype=int)

    # Get a prediction from the model
    prediction_result = MODEL.predict(input_values)

    return prediction_result


@app.route("/oil and gas")
def price_list():
    # Render page
    data = db.session.execute(db.select(Source)).scalars()
    return render_template("oil_and_gas.html", price_list=data)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handles user registration form.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            email = request.form.get("email")
            password = request.form.get("password")
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash(f"You are registered! {repr(new_user)}", category='success')
            return redirect(url_for('login'))
        except exc.IntegrityError:
            flash(f"You already have an account.", category='danger')
            return redirect(url_for('login'))

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles user login form.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.password == form.password.data:
            flash("Wrong email or password! Please try again.", category='danger')
        else:
            login_user(user)
            flash("Login Successful.", category='success')
            return redirect(url_for('index'))

    return render_template("login.html", title="Login", form=form)


@app.context_processor
def inject_user():
    return dict(current_user=current_user)
# define the current_user variable for use in the HTML template


@app.route("/logout")
def logout():
    """
    Logs the user out.
    """
    logout_user()
    flash("You have been logged out.", category='success')
    return redirect(url_for('login'))

