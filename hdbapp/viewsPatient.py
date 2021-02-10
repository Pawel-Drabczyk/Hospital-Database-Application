from flask import Flask, render_template, url_for, flash, redirect, session
from hdbapp.Web.forms import RegistrationForm, LoginForm, addPatientForm, searchPatientForm, updatePatientForm
from hdbapp.Web.connect import insertPatientSQL, selectPatientSQL, updatePatientSQL
import psycopg2.errors

posts = [
    {
        'author': 'Paweł Drabczyk',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'April 21, 2018'
    }
]

def home():
    return render_template('home.html', posts=posts)

def about():
    return render_template('about.html', title='About')

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return  redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            flash('You have benn logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Plese check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

def patient():
    return render_template('patient/patient.html', title='Patient')


def addPatient():
    form = addPatientForm()
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
            'additionalDescription': form.additionalDescription.data,
            'isAlive': form.isAlive.data
        }
        exception = insertPatientSQL(patientDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Patient already exists!', 'danger')
        else:
            flash('Added Patient!', 'success')
        return redirect(url_for('addPatient'))
    return render_template('patient/addPatient.html', title='Add Patient', form=form)

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