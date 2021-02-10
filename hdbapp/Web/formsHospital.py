from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class addHospitalForm(FlaskForm):
    idHospital = StringField('Hospital number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Hospital')

class searchPatientForm(FlaskForm):
    idPatient = StringField('PESEL number')
    name = StringField('Name')
    surname = StringField('Surname')
    gender = SelectField('Gender', choices=[('B', 'Both'), ('M', 'Male'), ('F', 'Female')])
    postalCode = StringField('Postal Code')
    city = StringField('City')
    street = StringField('Street')
    houseNumber = StringField('House Number')
    apartmentNumber = StringField('Apartment Number')
    tel = StringField('Telephone Number')
    email = StringField('Email')
    isAlive = SelectField('Alive', choices=[('B', 'Both'), ('A', 'Alive'), ('D', 'Dead')])
    submit = SubmitField('Search for Patient')

class updatePatientForm(FlaskForm):
    idPatientOld = StringField('Old PESEL number', validators=[DataRequired()])
    idPatient = StringField('PESEL number')
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
    submit = SubmitField('Update Patient Informations')

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