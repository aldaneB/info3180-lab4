from flask_wtf import FlaskForm,Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from wtforms.fields import TextField,TextAreaField,SelectField
from wtforms import validators, ValidationError

class ProfileForm(Form):
    firstname = TextField('FirstName', [validators.Required("(Required)")])
    lastname = TextField('LastName', [validators.Required("(Required)")])
    gender = SelectField(label='Gender', choices=[("Male", "Male"), ("Female", "Female")])
    email = TextField('Email',[validators.Required("(Required)")])
    location = TextField('Location',[validators.Required("(Required)")])
    bio = TextAreaField('Biography',[validators.Required("(Required)")])
    photo= FileField('Profile Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','Images Only!'])])
    
