from flask import render_template, url_for, flash, redirect, session
from hdbapp.Web.medicalCondition.formsMedicalCondition import addMedicalConditionForm, searchMedicalConditionForm, updateMedicalConditionForm
from hdbapp.Web.medicalCondition.connectMedicalCondition import insertMedicalConditionSQL, selectMedicalConditionSQL, updateMedicalConditionSQL
import psycopg2.errors


def medicalCondition():
    return render_template('medicalCondition/medicalCondition.html', title='Medical Condition')


def addMedicalCondition():
    form = addMedicalConditionForm()
    if form.validate_on_submit():
        medicalConditionDict = {
            'idMedicalCondition': form.idMedicalCondition.data,
            'name': form.name.data,
            'isInfectious': form.isInfectious.data
        }
        exception = insertMedicalConditionSQL(medicalConditionDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Medical Condition already exists!', 'danger')
        else:
            flash('Added Medical COndition!', 'success')
        return redirect(url_for('medicalCondition'))
    return render_template('medicalCondition/addMedicalCondition.html', title='Add Medical Condition', form=form)


def searchMedicalCondition():
    form = searchMedicalConditionForm()
    if form.validate_on_submit():
        medicalConditionDict = {
            'idMedicalCondition': form.idMedicalCondition.data,
            'name': form.name.data,
            'isInfectious': None
        }
        if medicalConditionDict['idMedicalCondition'] == '' : medicalConditionDict['idMedicalCondition'] = None
        if medicalConditionDict['name'] == '' : medicalConditionDict['name'] = None
        if form.isInfectious.data == 'Y':
            medicalConditionDict['isInfectious'] = True
        elif form.isInfectious.data == 'N':
            medicalConditionDict['isInfectious'] = False

        medicalConditionTupleList = selectMedicalConditionSQL(medicalConditionDict, 'postgres')
        medicalConditionDictList = []
        i = 1
        for tuple in medicalConditionTupleList:
            temp = {
                'listNumber': i,
                'idMedicalCondition': tuple[0],
                'name': tuple[1],
                'isInfectious': tuple[2]
            }
            i = i+1
            medicalConditionDictList.append(temp)
        session['medicalConditionDictList'] = medicalConditionDictList
        return redirect(url_for('displayMedicalCondition'))
    return render_template('medicalCondition/searchMedicalCondition.html', title='Search For Medical Condition', form=form)


def displayMedicalCondition():
    medicalConditionDictList = session.get('medicalConditionDictList', None)
    return render_template('medicalCondition/displayMedicalCondition.html', title='Display Medical Condition', medicalConditionDictList=medicalConditionDictList)


def updateMedicalCondition():
    form = updateMedicalConditionForm()
    if form.validate_on_submit():
        medicalConditionDict = {
            'idMedicalConditionOld': form.idMedicalConditionOld.data,
            'idMedicalCondition': form.idMedicalCondition.data,
            'name': form.name.data,
            'isInfectious': form.isInfectious.data
        }
        if medicalConditionDict['idMedicalCondition'] == '':
            medicalConditionDict['idMedicalCondition'] = medicalConditionDict['idMedicalConditionOld']
        exception = updateMedicalConditionSQL(medicalConditionDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Wrong medical condition data!', 'danger')
        else:
            flash('Updated Medical Condition!', 'success')
        return redirect(url_for('updateMedicalCondition'))
    return render_template('medicalCondition/updateMedicalCondition.html', title='Update Medical Condition', form=form)