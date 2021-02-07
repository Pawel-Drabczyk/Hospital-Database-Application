from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class addPatientForm(FlaskForm):
    idPatient = StringField('PESEL number', validators=[DataRequired()])
    name = StringField('Name')
    surname = StringField('Surname')
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    postalCode = StringField('Postal Code')
    city = StringField('City')
    street = StringField('Street')
    houseNumber = StringField('House Number')
    apartmentNumber = StringField('Apartment Number')
    tel = StringField('Telephone Number')
    email = StringField('Email')
    additionalDescription = StringField('Additional Description')
    isAlive = BooleanField('Alive')
    submit = SubmitField('Add Patient')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')