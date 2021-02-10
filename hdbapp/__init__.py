from flask import Flask
import hdbapp.views.viewsPatient
import hdbapp.views.viewsHospital
import hdbapp.views.viewsWard



app = Flask(__name__)
app.config['SECRET_KEY'] = 'da73c0b0468da6b34c3ed3042c833b22a9981a2e80549059a0b2dc243ad0fc7db03d433988729d0148964816254b8823f29589f03332'


app.add_url_rule('/', view_func=hdbapp.views.viewsPatient.home, methods=['Get', 'POST'])
app.add_url_rule('/about', view_func=hdbapp.views.viewsPatient.about, methods=['Get', 'POST'])
app.add_url_rule('/register', view_func=hdbapp.views.viewsPatient.register, methods=['Get', 'POST'])
app.add_url_rule('/login', view_func=hdbapp.views.viewsPatient.login)

app.add_url_rule('/Patient', view_func=hdbapp.views.viewsPatient.patient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/addPatient', view_func=hdbapp.views.viewsPatient.addPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/searchPatient', view_func=hdbapp.views.viewsPatient.searchPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/displayPatient', view_func=hdbapp.views.viewsPatient.displayPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/updatePatient', view_func=hdbapp.views.viewsPatient.updatePatient, methods=['Get', 'POST'])

app.add_url_rule('/Hospital', view_func=hdbapp.views.viewsHospital.hospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/addHospital', view_func=hdbapp.views.viewsHospital.addHospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/searchHospital', view_func=hdbapp.views.viewsHospital.searchHospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/displayHospital', view_func=hdbapp.views.viewsHospital.displayHospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/updateHospital', view_func=hdbapp.views.viewsHospital.updateHospital, methods=['Get', 'POST'])

app.add_url_rule('/Ward', view_func=hdbapp.views.viewsWard.ward, methods=['Get', 'POST'])
app.add_url_rule('/Ward/addWard', view_func=hdbapp.views.viewsWard.addWard, methods=['Get', 'POST'])
app.add_url_rule('/Ward/searchHospital', view_func=hdbapp.views.viewsWard.searchWard, methods=['Get', 'POST'])
app.add_url_rule('/Ward/displayHospital', view_func=hdbapp.views.viewsWard.displayWard, methods=['Get', 'POST'])
app.add_url_rule('/Ward/updateHospital', view_func=hdbapp.views.viewsWard.updateWard, methods=['Get', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
