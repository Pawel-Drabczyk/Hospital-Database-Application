from flask import render_template, url_for, flash, redirect, session
from hdbapp.Web.hospital.formsHospital import addHospitalForm, searchHospitalForm, updateHospitalForm
from hdbapp.Web.hospital.connectHospital import insertHospitalSQL, selectHospitalSQL, updateHospitalSQL
import psycopg2.errors

def hospital():
    return render_template('hospital/hospital.html', title='Hospital')

def addHospital():
    form = addHospitalForm()
    if form.validate_on_submit():
        hospitalDict = {
            'idHospital': form.idHospital.data,
            'name': form.name.data
        }
        exception = insertHospitalSQL(hospitalDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Hospital already exists!', 'danger')
        else:
            flash('Added Hospital!', 'success')
        return redirect(url_for('addHospital'))
    return render_template('hospital/addHospital.html', title='Add Hospital', form=form)

def searchHospital():
    form = searchHospitalForm()
    if form.validate_on_submit():
        hospitalDict = {
            'idHospital': form.idHospital.data,
            'name': form.name.data
        }
        if hospitalDict['idHospital'] == '' : hospitalDict['idHospital'] = None
        if hospitalDict['name'] == '' : hospitalDict['name'] = None

        hospitalTupleList = selectHospitalSQL(hospitalDict, 'postgres')
        #converting list of tuples to list of dictionaries
        hospitalDictList = []
        i = 1
        for tuple in hospitalTupleList:
            temp = {
                'listNumber': i,
                'idHospital': tuple[0],
                'name': tuple[1],
            }
            i = i+1
            hospitalDictList.append(temp)

        session['hospitalDictList'] = hospitalDictList
        return redirect(url_for('displayHospital'))
    return render_template('hospital/searchHospital.html', title='Search For Hospital', form=form)

def displayHospital():
    hospitalDictList = session.get('hospitalDictList', None)
    return render_template('hospital/displayHospital.html', title='Display Hospital', hospitalDictList=hospitalDictList)

def updateHospital():
    form = updateHospitalForm()
    if form.validate_on_submit():
        hospitalDict = {
            'idHospitalOld': form.idHospitalOld.data,
            'idHospital': form.idHospital.data,
            'name': form.name.data
        }
        if hospitalDict['idHospital'] == '':
            hospitalDict['idHospital'] = hospitalDict['idHospitalOld']

        exception = updateHospitalSQL(hospitalDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Wrong hospital number!', 'danger')
        else:
            flash('Updated hospital!', 'success')
        return redirect(url_for('updateHospital'))
    return render_template('hospital/updateHospital.html', title='Update Hospital', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)