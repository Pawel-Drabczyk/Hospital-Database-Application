from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addHospitalForm(FlaskForm):
    idHospital = StringField('Hospital number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Hospital')

class searchHospitalForm(FlaskForm):
    idHospital = StringField('Hospital number')
    name = StringField('Name')
    submit = SubmitField('Search for Hospital')

class updateHospitalForm(FlaskForm):
    idHospitalOld = StringField('Old Hospital number', validators=[DataRequired()])
    idHospital = StringField('Hospital number')
    name = StringField('Name')
    submit = SubmitField('Update Hospital Informations')
