from flask import render_template, url_for, flash, redirect, session
from hdbapp.Web.stay.formsStay import addStayForm, searchStayForm, updateStayForm
from hdbapp.Web.stay.connectStay import insertStaySQL, selectStaySQL, updateStaySQL
import psycopg2.errors

def stay():
    return render_template('stay/stay.html', title='Stay')

def addStay():
    form = addStayForm()
    if form.validate_on_submit():
        stayDict = {
            'idStay': form.idStay.data,
            'idPatient': form.idPatient.data,
            'startDate': form.startDate.data,
            'endDate': form.endDate.data,
            'idDoctor': form.idDoctor.data,
            'idWard': form.idWard.data,
            'idDisease': form.idDisease.data
        }
        exception = insertStaySQL(stayDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Stay data are wrong!', 'danger')
        else:
            flash('Added Stay!', 'success')
        return redirect(url_for('addStay'))
    return render_template('stay/addStay.html', title='Add Stay', form=form)

def searchStay():
    form = searchStayForm()
    if form.validate_on_submit():
        stayDict = {
            'idStay': form.idStay.data,
            'idPatient': form.idPatient.data,
            'startDate': form.startDate.data,
            'endDate': form.endDate.data,
            'idDoctor': form.idDoctor.data,
            'idWard': form.idWard.data
        }
        if stayDict['idStay'] == '' : stayDict['idStay'] = None
        if stayDict['idPatient'] == '' : stayDict['idPatient'] = None
        if stayDict['startDate'] == '': stayDict['startDate'] = None
        if stayDict['endDate'] == '': stayDict['endDate'] = None
        if stayDict['idDoctor'] == '': stayDict['idDoctor'] = None
        if stayDict['idWard'] == '': stayDict['idWard'] = None

        stayTupleList = selectStaySQL(stayDict, 'postgres')
        #converting list of tuples to list of dictionaries
        stayDictList = []
        i = 1
        for tuple in stayTupleList:
            temp = {
                'listNumber': i,
                'idStay': tuple[0],
                'idPatient':  tuple[1],
                'startDate': tuple[2],
                'endDate': tuple[3],
                'idDoctor': tuple[4],
                'idWard': tuple[5]
            }
            i = i+1
            stayDictList.append(temp)

        session['stayDictList'] = stayDictList
        return redirect(url_for('displayStay'))
    return render_template('stay/searchStay.html', title='Search For Stay', form=form)

def displayStay():
    stayDictList = session.get('stayDictList', None)
    return render_template('stay/displayStay.html', title='Display Stay', stayDictList=stayDictList)

def updateStay():
    form = updateStayForm()
    if form.validate_on_submit():
        stayDict = {
            'idStayOld': form.idStayOld.data,
            'idStay': form.idStay.data,
            'idPatient': form.idPatient.data,
            'startDate': form.startDate.data,
            'endDate': form.endDate.data,
            'idDoctor': form.idDoctor.data,
            'idWard': form.idWard.data,
            'idDisease': form.idDisease.data
        }
        if stayDict['idStay'] == '':
            stayDict['idStay'] = stayDict['idStayOld']

        exception = updateStaySQL(stayDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Wrong stay data!', 'danger')
        else:
            flash('Updated stay!', 'success')
        return redirect(url_for('updateStay'))
    return render_template('stay/updateStay.html', title='Update stay', form=form)

