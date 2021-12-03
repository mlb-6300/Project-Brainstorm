from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
import database_mangement as dbm


class login_form(FlaskForm):
    username = StringField(label="Enter Your Username:", validators=[DataRequired(), Length(max=40)])
    password = PasswordField(label="Enter a Password:", validators=[DataRequired(), Length(max=40)], id='password')
    toggle_pw = BooleanField(label="Show Password", id='check')
    submit = SubmitField(label="Submit")
