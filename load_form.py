from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length

# flask wtf form for loading a whiteboard based on uuid
class load_form(FlaskForm):
    uuid = StringField(label="Enter the UUID: ", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField(label="Load")