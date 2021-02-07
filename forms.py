"""Forms for adopt app."""
#Imports for forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

##Step 1: Create Database & Model
class AddPetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )
    
   
    