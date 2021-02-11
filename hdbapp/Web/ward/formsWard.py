from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addWardForm(FlaskForm):
    idWard = StringField('Ward number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    capacity = StringField('Capacity', validators=[DataRequired()])
    idHospital = StringField('Hospital number', validators=[DataRequired()])
    submit = SubmitField('Add Ward')

class searchWardForm(FlaskForm):
    idWard = StringField('Ward number')
    name = StringField('Name')
    capacity = StringField('Capacity')
    idHospital = StringField('Hospital number')
    submit = SubmitField('Search for Hospital')

class updateWardForm(FlaskForm):
    idWardOld = StringField('Old Ward number', validators=[DataRequired()])
    idWard = StringField('Ward number')
    name = StringField('Name')
    capacity = StringField('Capacity')
    idHospital = StringField('Hospital number')
    submit = SubmitField('Search for Hospital')
