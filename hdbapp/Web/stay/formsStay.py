from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class addStayForm(FlaskForm):
    idStay = StringField('Stay number', validators=[DataRequired()])
    idPatient = StringField('Patient PESEL number', validators=[DataRequired()])
    startDate = StringField('Start Date')
    endDate = StringField('End Date')
    idWard = StringField('Ward number', validators=[DataRequired()])
    idDoctor = StringField('Doctor PESEL number', validators=[DataRequired()])
    idDisease = StringField('Disease number', validators=[DataRequired()])
    submit = SubmitField('Add stay')

class searchStayForm(FlaskForm):
    idStay = StringField('Stay number')
    idPatient = StringField('Patient PESEL number')
    startDate = StringField('Start Date')
    endDate = StringField('End Date')
    idWard = StringField('Ward number')
    idDoctor = StringField('Doctor PESEL number')
    submit = SubmitField('Search for stay')

class updateStayForm(FlaskForm):
    idStayOld = StringField('Old stay number', validators=[DataRequired()])
    idStay = StringField('Stay number', validators=[DataRequired()])
    idPatient = StringField('Patient PESEL number', validators=[DataRequired()])
    startDate = StringField('Start Date')
    endDate = StringField('End Date')
    idWard = StringField('Ward number', validators=[DataRequired()])
    idDoctor = StringField('Doctor PESEL number', validators=[DataRequired()])
    idDisease = StringField('Disease number', validators=[DataRequired()])
    submit = SubmitField('Update stay')
