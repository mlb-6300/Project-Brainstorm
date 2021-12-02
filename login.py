from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import database_mangement as dbm


class login_form(FlaskForm):
    username = StringField(label="Enter Your Username:", validators=[DataRequired(), Length(max=40)])
    password = PasswordField(label="Enter a Password:", validators=[DataRequired(), Length(max=40)], id='password')
    submit = SubmitField(label="Submit")

    def validate_username(self, username):
        user = dbm.get_unique_user(username=username.data)
        if len(user) == 0:
            raise ValidationError("Username or Password invalid, please try again.")
