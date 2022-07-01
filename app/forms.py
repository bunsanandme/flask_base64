from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Encode(FlaskForm):
    b64_input = StringField('Original')
    submit = SubmitField('-> Base64')