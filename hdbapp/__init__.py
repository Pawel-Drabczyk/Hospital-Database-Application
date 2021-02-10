from flask import Flask
import hdbapp.viewsPatient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'da73c0b0468da6b34c3ed3042c833b22a9981a2e80549059a0b2dc243ad0fc7db03d433988729d0148964816254b8823f29589f03332'


app.add_url_rule('/', view_func=hdbapp.viewsPatient.home, methods=['Get', 'POST'])
app.add_url_rule('/about', view_func=hdbapp.viewsPatient.about, methods=['Get', 'POST'])
app.add_url_rule('/register', view_func=hdbapp.viewsPatient.register, methods=['Get', 'POST'])
app.add_url_rule('/login', view_func=hdbapp.viewsPatient.login)
app.add_url_rule('/Patient', view_func=hdbapp.viewsPatient.patient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/addPatient', view_func=hdbapp.viewsPatient.addPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/searchPatient', view_func=hdbapp.viewsPatient.searchPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/displayPatient', view_func=hdbapp.viewsPatient.displayPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/updatePatient', view_func=hdbapp.viewsPatient.updatePatient, methods=['Get', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
