from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class edit_profile_form(FlaskForm):
    password = PasswordField(label="Enter Your NEW Password:", validators=[Length(max=40)],
                             id='password')
    confirm_pw = PasswordField(label="Confirm your NEW Password:",
                               validators=[Length(max=40)])
    toggle_pw = BooleanField(label="Show Password", id='check')
    first_name = StringField(label="Enter your First Name:", validators=[DataRequired(), Length(max=30)], )
    last_name = StringField(label="Enter your Last Name:", validators=[DataRequired(), Length(max=30)], )
    gender = SelectField(label="Select your Gender:", choices=["Male", "Female", "Other"])
    dob = DateField(label="Enter your Date of Birth:", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

    def validate_password(self, password):
        if password.data != '':
            if self.confirm_pw.data == '':
                raise ValidationError("Confirm Password Field is Empty")
            elif self.confirm_pw.data != password.data:
                raise ValidationError("Passwords Do Not Match")