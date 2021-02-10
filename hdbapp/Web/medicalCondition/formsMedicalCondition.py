from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class addMedicalConditionForm(FlaskForm):
    idMedicalCondition = StringField('Medical Condition number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    isInfectious = BooleanField('Is infectious?')
    submit = SubmitField('Add Medical Condition')

class searchMedicalConditionForm(FlaskForm):
    idMedicalCondition = StringField('Medical Condition number')
    name = StringField('Name')
    isInfectious = SelectField('Is infectious?', choices=[('B', 'Both'), ('Y', 'Yes'), ('N', 'NO')])
    submit = SubmitField('Search for Medical Condition')

class updateMedicalConditionForm(FlaskForm):
    idMedicalConditionOld = StringField('Old Medical Condition number', validators=[DataRequired()])
    idMedicalCondition = StringField('Medical Condition number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    isInfectious = BooleanField('Is infectious?')
    submit = SubmitField('Update Medical Condition')
