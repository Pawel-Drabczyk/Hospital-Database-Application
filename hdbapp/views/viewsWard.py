from flask import render_template, url_for, flash, redirect, session
from hdbapp.Web.ward.formsWard import addWardForm, searchWardForm, updateWardForm
from hdbapp.Web.ward.connectWard import insertWardSQL, selectWardSQL, updateWardSQL
import psycopg2.errors

def ward():
    return render_template('ward/ward.html', title='Ward')

def addWard():
    form = addWardForm()
    if form.validate_on_submit():
        wardDict = {
            'idWard': form.idWard.data,
            'name': form.name.data,
            'capacity': form.capacity.data,
            'idHospital': form.idHospital.data
        }
        exception = insertWardSQL(wardDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Ward already exists or hospital doesnt exists', 'danger')
        else:
            flash('Added Ward!', 'success')
        return redirect(url_for('addWard'))
    return render_template('ward/addWard.html', title='Add Ward', form=form)

def searchWard():
    form = searchWardForm()
    if form.validate_on_submit():
        wardDict = {
            'idWard': form.idWard.data,
            'name': form.name.data,
            'capacity': form.capacity.data,
            'idHospital': form.idHospital.data
        }
        if wardDict['idWard'] == '' : wardDict['idWard'] = None
        if wardDict['name'] == '' : wardDict['name'] = None
        if wardDict['capacity'] == '' : wardDict['capacity'] = None
        if wardDict['idHospital'] == '' : wardDict['idHospital'] = None

        wardTupleList = selectWardSQL(wardDict, 'postgres')
        wardDictList = []
        i = 1
        for tuple in wardTupleList:
            temp = {
                'listNumber': i,
                'idWard': tuple[0],
                'name': tuple[1],
                'capacity': tuple[2],
                'idHospital': tuple[3]
            }
            i = i+1
            wardDictList.append(temp)

        session['wardDictList'] = wardDictList
        return redirect(url_for('displayWard'))
    return render_template('ward/searchWard.html', title='Search For Ward', form=form)

def displayWard():
    wardDictList = session.get('wardDictList', None)
    return render_template('ward/displayWard.html', title='Display Ward', wardDictList=wardDictList)

def updateWard():
    form = updateWardForm()
    if form.validate_on_submit():
        wardDict = {
            'idWardOld': form.idWardOld.data,
            'idWard': form.idWard.data,
            'name': form.name.data,
            'capacity': form.capacity.data,
            'idHospital': form.idHospital.data
        }
        if wardDict['idWard'] == '':
            wardDict['idWard'] = wardDict['idWardOld']

        exception = updateWardSQL(wardDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Wrong ward or hospital number!', 'danger')
        else:
            flash('Updated ward!', 'success')
        return redirect(url_for('updateWard'))
    return render_template('ward/updateWard.html', title='Update Ward', form=form)

