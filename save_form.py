from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length

# flask wtf form for saving a board 
class save_form(FlaskForm):
    whiteboard_name = StringField(label="Enter Whiteboard Name", validators=[DataRequired(), Length(max=40)])
    submit = SubmitField(label="Save")
    data = HiddenField(label="data")
    image = HiddenField(label="image")
    UUID = HiddenField(label="UUID")