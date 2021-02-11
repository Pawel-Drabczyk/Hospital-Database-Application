from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class addDiseaseForm(FlaskForm):
    idDisease = StringField('Disease number', validators=[DataRequired()])
    idPatient = StringField('Patient PESEL number', validators=[DataRequired()])
    startDate = StringField('Start Date')
    endDate = StringField('End Date')
    idMedicalCondition = StringField('MedicalCondition number', validators=[DataRequired()])
    idDoctor = StringField('Doctor PESEL number', validators=[DataRequired()])
    submit = SubmitField('Add disease')

class searchDiseaseForm(FlaskForm):
    idDisease = StringField('Disease number')
    idPatient = StringField('Patient PESEL number')
    startDate = StringField('Start Date')
    endDate = StringField('End Date')
    idMedicalCondition = StringField('MedicalCondition number')
    idDoctor = StringField('Doctor PESEL number')
    submit = SubmitField('Search for disease')

class updateDiseaseForm(FlaskForm):
    idDiseaseOld = StringField('Old Disease number', validators=[DataRequired()])
    idDisease = StringField('Disease number', validators=[DataRequired()])
    idPatient = StringField('Patient PESEL number', validators=[DataRequired()])
    startDate = StringField('Start Date')
    endDate = StringField('End Date')
    idMedicalCondition = StringField('MedicalCondition number', validators=[DataRequired()])
    idDoctor = StringField('Doctor PESEL number', validators=[DataRequired()])
    submit = SubmitField('Add disease')
