from flask import Flask, render_template, url_for, flash, redirect, session
from hdbapp.Web.formsHospital import addHospitalForm#, searchPatientForm, updatePatientForm
from hdbapp.Web.connectHospital import insertHospitalSQL#, selectHospitalSQL, updateHospitalSQL
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

def searchPatient():
    form = searchPatientForm()
    if form.validate_on_submit():
        patientDict = {
            'idPatient': form.idPatient.data,
            'name': form.name.data,
            'surname': form.surname.data,
            'gender': form.gender.data,
            'postalCode': form.postalCode.data,
            'city': form.city.data,
            'street': form.street.data,
            'houseNumber': form.houseNumber.data,
            'apartmentNumber': form.apartmentNumber.data,
            'tel': form.tel.data,
            'email': form.email.data,
            'isAlive': None
        }
        if form.isAlive.data == 'A':
            patientDict['isAlive'] = True
        elif form.isAlive.data == 'D':
            patientDict['isAlive'] = False
        if patientDict['idPatient'] == '': patientDict['idPatient'] = None
        if patientDict['name'] == '': patientDict['name'] = None
        if patientDict['surname'] == '': patientDict['surname'] = None
        if patientDict['postalCode'] == '': patientDict['postalCode'] = None
        if patientDict['city'] == '': patientDict['city'] = None
        if patientDict['street'] == '': patientDict['street'] = None
        if patientDict['houseNumber'] == '': patientDict['houseNumber'] = None
        if patientDict['apartmentNumber'] == '': patientDict['apartmentNumber'] = None
        if patientDict['tel'] == '': patientDict['tel'] = None
        if patientDict['email'] == '': patientDict['email'] = None

        patientTupleList = selectPatientSQL(patientDict, 'postgres')
        #converting list of tuples to list of dictionaries
        patientDictList = []
        i = 1
        for tuple in patientTupleList:
            temp = {
                'listNumber': i,
                'idPatient': tuple[0],
                'name': tuple[1],
                'surname': tuple[2],
                'gender': tuple[3],
                'postalCode': tuple[4],
                'city': tuple[5],
                'street': tuple[6],
                'houseNumber': tuple[7],
                'apartmentNumber': tuple[8],
                'tel': tuple[9],
                'email': tuple[10],
                'additionalDescription': tuple[11],
                'isAlive': tuple[12]
            }
            i = i+1
            patientDictList.append(temp)

        session['patientDictList'] = patientDictList
        return redirect(url_for('displayPatient', patientDictList=patientDictList))
    return render_template('patient/searchPatient.html', title='Search For Patient', form=form)

def displayPatient():
    patientDictList = session.get('patientDictList', None)
    return render_template('patient/displayPatient.html', title='Display Patient', patientDictList=patientDictList)

def updatePatient():
    form = updatePatientForm()
    if form.validate_on_submit():
        patientDict = {
            'idPatientOld': form.idPatientOld.data,
            'idPatient': form.idPatient.data,
            'name': form.name.data,
            'surname': form.surname.data,
            'gender': form.gender.data,
            'postalCode': form.postalCode.data,
            'city': form.city.data,
            'street': form.street.data,
            'houseNumber': form.houseNumber.data,
            'apartmentNumber': form.apartmentNumber.data,
            'tel': form.tel.data,
            'email': form.email.data,
            'additionalDescription': form.additionalDescription.data,
            'isAlive': form.isAlive.data
        }
        if patientDict['idPatient'] == '':
            patientDict['idPatient'] = patientDict['idPatientOld']

        exception = updatePatientSQL(patientDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Wrong PESEL number!', 'danger')
        else:
            flash('Updated Patient!', 'success')
        return redirect(url_for('updatePatient'))
    return render_template('patient/updatePatient.html', title='Update Patient', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)