from flask import render_template, url_for, flash, redirect, session
from hdbapp.Web.doctor.formsDoctor import addDoctorForm, searchDoctorForm, updateDoctorForm
from hdbapp.Web.doctor.connectDoctor import insertDoctorSQL, selectDoctorSQL, updateDoctorSQL
import psycopg2.errors

def doctor():
    return render_template('doctor/doctor.html', title='Doctor')


def addDoctor():
    form = addDoctorForm()
    if form.validate_on_submit():
        doctorDict = {
            'idDoctor': form.idDoctor.data,
            'name': form.name.data,
            'surname': form.surname.data,
            'gender': form.gender.data,
            'tel': form.tel.data,
            'email': form.email.data,
            'specialisation': form.specialisation.data,
            'idWard': form.idWard.data
        }
        exception = insertDoctorSQL(doctorDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Doctor already exists!', 'danger')
        else:
            flash('Added doctor!', 'success')
        return redirect(url_for('addDoctor'))
    return render_template('doctor/addDoctor.html', title='Add Doctor', form=form)

def searchDoctor():
    form = searchDoctorForm()
    if form.validate_on_submit():
        doctorDict = {
            'idDoctor': form.idDoctor.data,
            'name': form.name.data,
            'surname': form.surname.data,
            'gender': form.gender.data,
            'tel': form.tel.data,
            'email': form.email.data,
            'specialisation': form.specialisation.data,
            'idWard': form.idWard.data
        }

        if doctorDict['idDoctor'] == '': doctorDict['idDoctor'] = None
        if doctorDict['name'] == '': doctorDict['name'] = None
        if doctorDict['surname'] == '': doctorDict['surname'] = None
        if doctorDict['tel'] == '': doctorDict['tel'] = None
        if doctorDict['email'] == '': doctorDict['email'] = None
        if doctorDict['specialisation'] == '': doctorDict['specialisation'] = None
        if doctorDict['idWard'] == '': doctorDict['idWard'] = None



        doctorTupleList = selectDoctorSQL(doctorDict, 'postgres')
        #converting list of tuples to list of dictionaries
        doctorDictList = []
        i = 1
        for tuple in doctorTupleList:
            temp = {
                'listNumber': i,
                'idDoctor': tuple[0],
                'name': tuple[1],
                'surname': tuple[2],
                'gender': tuple[3],
                'tel': tuple[4],
                'email': tuple[5],
                'specialisation': tuple[6],
                'idWard': tuple[7]
            }
            i = i+1
            doctorDictList.append(temp)

        session['doctorDictList'] = doctorDictList
        return redirect(url_for('displayDoctor', doctorDictList=doctorDictList))
    return render_template('doctor/searchDoctor.html', title='Search For Doctor', form=form)

def displayDoctor():
    doctorDictList = session.get('doctorDictList', None)
    return render_template('doctor/displayDoctor.html', title='Display Doctor', doctorDictList=doctorDictList)

def updateDoctor():
    form = updateDoctorForm()
    if form.validate_on_submit():
        doctorDict = {
            'idDoctorOld': form.idDoctorOld.data,
            'idDoctor': form.idDoctor.data,
            'name': form.name.data,
            'surname': form.surname.data,
            'gender': form.gender.data,
            'tel': form.tel.data,
            'email': form.email.data,
            'specialisation': form.specialisation.data,
            'idWard': form.idWard.data
        }
        if doctorDict['idDoctor'] == '':
            doctorDict['idDoctor'] = doctorDict['idDoctorOld']

        exception = updateDoctorSQL(doctorDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash("Wrong doctors' data!", 'danger')
        else:
            flash('Updated Doctor!', 'success')
        return redirect(url_for('updateDoctor'))
    return render_template('doctor/updateDoctor.html', title='Update Doctor', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)