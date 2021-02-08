from flask import Flask, render_template, url_for, flash, redirect
from Web.forms import RegistrationForm, LoginForm, addPatientForm, searchPatientForm
from Web.connect import insertPatient, selectPatient
import psycopg2.errors


app = Flask(__name__)
app.config['SECRET_KEY'] = 'da73c0b0468da6b34c3ed3042c833b22a9981a2e80549059a0b2dc243ad0fc7db03d433988729d0148964816254b8823f29589f03332'

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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['Get', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return  redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            flash('You have benn logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Plese check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/addPatient', methods=['Get', 'POST'])
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
        exception = insertPatient(patientDict, 'postgres')
        if exception == psycopg2.errors.IntegrityError:
            flash('Patient already exists!', 'danger')
        else:
            flash('Added Patient!', 'success')
        return redirect(url_for('addPatient'))
    return render_template('addPatient.html', title='Add Patient', form=form)

@app.route('/searchPatient', methods=['Get', 'POST'])
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

        patientResultList = selectPatient(patientDict, 'postgres')

        return redirect(url_for('displayPatient'))
    return render_template('searchPatient.html', title='Search For Patient', form=form)

@app.route('/displayPatient', methods=['Get', 'POST'])
def displayPatient():


if __name__ == '__main__':
    app.run(debug=True)