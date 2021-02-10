from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class addDoctorForm(FlaskForm):
    idDoctor = StringField('PESEL number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    tel = StringField('Telephone Number')
    email = StringField('Email')
    specialisation = StringField('Specialisation')
    idWard = StringField('Ward number', validators=[DataRequired()])
    submit = SubmitField('Add Doctor')

class searchDoctorForm(FlaskForm):
    idDoctor = StringField('PESEL number')
    name = StringField('Name')
    surname = StringField('Surname')
    gender = SelectField('Gender', choices=[('B', 'Both'), ('M', 'Male'), ('F', 'Female')])
    tel = StringField('Telephone Number')
    email = StringField('Email')
    specialisation = StringField('Specialisation')
    idWard = StringField('Ward number')
    submit = SubmitField('Search fo Doctor')

class updateDoctorForm(FlaskForm):
    idDoctorOld = StringField('Old PESEL number', validators=[DataRequired()])
    idDoctor = StringField('PESEL number')
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    tel = StringField('Telephone Number')
    email = StringField('Email')
    specialisation = StringField('Specialisation')
    idWard = StringField('Ward number', validators=[DataRequired()])
    submit = SubmitField('Search fo Doctor')
