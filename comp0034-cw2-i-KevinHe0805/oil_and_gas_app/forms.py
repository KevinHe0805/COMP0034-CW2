from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Optional, Length, EqualTo


class PredictionForm(FlaskForm):
    """Fields to a form to input the values required for a prediction"""

    # https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.DecimalField
    year = DecimalField(validators=[DataRequired()])
    month = DecimalField(validators=[DataRequired()])
    day = DecimalField(validators=[DataRequired()])
    type = DecimalField(validators=[Optional()])


class RegisterForm(FlaskForm):
    """Fields to a form to input the values required for new users"""

    email = EmailField("Email", validators=[DataRequired()])
    password = StringField(
        "Password", validators=[DataRequired(), Length(min=5, max=16)]
    )
    confirm_password = StringField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Signup")


class LoginForm(FlaskForm):
    """Fields to a form to input the values required for login"""

    email = EmailField("Email", validators=[DataRequired()])
    password = StringField(
        "Password", validators=[DataRequired(), Length(min=5, max=16)]
    )