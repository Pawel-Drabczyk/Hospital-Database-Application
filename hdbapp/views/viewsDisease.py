from flask import render_template, url_for, flash, redirect, session
from hdbapp.Web.disease.formsDisease import addDiseaseForm, searchDiseaseForm, updateDiseaseForm
from hdbapp.Web.disease.connectDisease import insertDiseaseSQL, selectDiseaseSQL, updateDiseaseSQL
import psycopg2.errors

def disease():
    return render_template('disease/disease.html', title='Disease')

def addDisease():
    form = addDiseaseForm()
    if form.validate_on_submit():
        diseaseDict = {
            'idDisease': form.idDisease.data,
            'idPatient': form.idPatient.data,
            'startDate': form.startDate.data,
            'endDate': form.endDate.data,
            'idMedicalCondition': form.idMedicalCondition.data,
            'idDoctor': form.idDoctor.data,
        }
        exception = insertDiseaseSQL(diseaseDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Disease already exists!', 'danger')
        else:
            flash('Added Disease!', 'success')
        return redirect(url_for('addDisease'))
    return render_template('disease/addDisease.html', title='Add Disease', form=form)

def searchDisease():
    form = searchDiseaseForm()
    if form.validate_on_submit():
        diseaseDict = {
            'idDisease': form.idDisease.data,
            'idPatient': form.idPatient.data,
            'startDate': form.startDate.data,
            'endDate': form.endDate.data,
            'idMedicalCondition': form.idMedicalCondition.data,
            'idDoctor': form.idDoctor.data,
        }
        if diseaseDict['idDisease'] == '' : diseaseDict['idDisease'] = None
        if diseaseDict['idPatient'] == '' : diseaseDict['idPatient'] = None
        if diseaseDict['startDate'] == '': diseaseDict['startDate'] = None
        if diseaseDict['endDate'] == '': diseaseDict['endDate'] = None
        if diseaseDict['idMedicalCondition'] == '': diseaseDict['idMedicalCondition'] = None
        if diseaseDict['idDoctor'] == '': diseaseDict['idDoctor'] = None

        diseaseTupleList = selectDiseaseSQL(diseaseDict, 'postgres')
        #converting list of tuples to list of dictionaries
        diseaseDictList = []
        i = 1
        for tuple in diseaseTupleList:
            temp = {
                'listNumber': i,
                'idDisease': tuple[0],
                'idPatient': tuple[1],
                'startDate': tuple[2],
                'endDate': tuple[3],
                'idMedicalCondition': tuple[4],
                'idDoctor': tuple[5],
            }
            i = i+1
            diseaseDictList.append(temp)

        session['diseaseDictList'] = diseaseDictList
        return redirect(url_for('displayDisease'))
    return render_template('disease/searchDisease.html', title='Search For Disease', form=form)

def displayDisease():
    diseaseDictList = session.get('diseaseDictList', None)
    return render_template('disease/displayDisease.html', title='Display Disease', diseaseDictList=diseaseDictList)

def updateDisease():
    form = updateDiseaseForm()
    if form.validate_on_submit():
        diseaseDict = {
            'idDiseaseOld': form.idDiseaseOld.data,
            'idDisease': form.idDisease.data,
            'idPatient': form.idPatient.data,
            'startDate': form.startDate.data,
            'endDate': form.endDate.data,
            'idMedicalCondition': form.idMedicalCondition.data,
            'idDoctor': form.idDoctor.data,
        }
        if diseaseDict['idDisease'] == '':
            diseaseDict['idDisease'] = diseaseDict['idDiseaseOld']

        exception = updateDiseaseSQL(diseaseDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Wrong disease number!', 'danger')
        else:
            flash('Updated disease!', 'success')
        return redirect(url_for('updateDisease'))
    return render_template('disease/updateDisease.html', title='Update disease', form=form)

