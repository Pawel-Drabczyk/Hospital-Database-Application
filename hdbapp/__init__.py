from flask import Flask
import hdbapp.views.viewsPatient
import hdbapp.views.viewsDisease
import hdbapp.views.viewsStay
import hdbapp.views.viewsDoctor
import hdbapp.views.viewsHospital
import hdbapp.views.viewsMedicalCondition
import hdbapp.views.viewsWard
import hdbapp.views.viewsStatistics




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

app.add_url_rule('/disease', view_func=hdbapp.views.viewsDisease.disease, methods=['Get', 'POST'])
app.add_url_rule('/disease/addDisease', view_func=hdbapp.views.viewsDisease.addDisease, methods=['Get', 'POST'])
app.add_url_rule('/disease/searchDisease', view_func=hdbapp.views.viewsDisease.searchDisease, methods=['Get', 'POST'])
app.add_url_rule('/disease/displayDisease', view_func=hdbapp.views.viewsDisease.displayDisease, methods=['Get', 'POST'])
app.add_url_rule('/disease/updateDisease', view_func=hdbapp.views.viewsDisease.updateDisease, methods=['Get', 'POST'])

app.add_url_rule('/stay', view_func=hdbapp.views.viewsStay.stay, methods=['Get', 'POST'])
app.add_url_rule('/stay/addStay', view_func=hdbapp.views.viewsStay.addStay, methods=['Get', 'POST'])
app.add_url_rule('/stay/searchStay', view_func=hdbapp.views.viewsStay.searchStay, methods=['Get', 'POST'])
app.add_url_rule('/stay/displayStay', view_func=hdbapp.views.viewsStay.displayStay, methods=['Get', 'POST'])
app.add_url_rule('/stay/updateStay', view_func=hdbapp.views.viewsStay.updateStay, methods=['Get', 'POST'])

app.add_url_rule('/Doctor', view_func=hdbapp.views.viewsDoctor.doctor, methods=['Get', 'POST'])
app.add_url_rule('/Doctor/addDoctor', view_func=hdbapp.views.viewsDoctor.addDoctor, methods=['Get', 'POST'])
app.add_url_rule('/Doctor/searchDoctor', view_func=hdbapp.views.viewsDoctor.searchDoctor, methods=['Get', 'POST'])
app.add_url_rule('/Doctor/displayDoctor', view_func=hdbapp.views.viewsDoctor.displayDoctor, methods=['Get', 'POST'])
app.add_url_rule('/Doctor/updateDoctor', view_func=hdbapp.views.viewsDoctor.updateDoctor, methods=['Get', 'POST'])

app.add_url_rule('/Hospital', view_func=hdbapp.views.viewsHospital.hospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/addHospital', view_func=hdbapp.views.viewsHospital.addHospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/searchHospital', view_func=hdbapp.views.viewsHospital.searchHospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/displayHospital', view_func=hdbapp.views.viewsHospital.displayHospital, methods=['Get', 'POST'])
app.add_url_rule('/Hospital/updateHospital', view_func=hdbapp.views.viewsHospital.updateHospital, methods=['Get', 'POST'])

app.add_url_rule('/medicalCondition', view_func=hdbapp.views.viewsMedicalCondition.medicalCondition, methods=['Get', 'POST'])
app.add_url_rule('/medicalCondition/addMedicalCondition', view_func=hdbapp.views.viewsMedicalCondition.addMedicalCondition, methods=['Get', 'POST'])
app.add_url_rule('/medicalCondition/searchMedicalCondition', view_func=hdbapp.views.viewsMedicalCondition.searchMedicalCondition, methods=['Get', 'POST'])
app.add_url_rule('/medicalCondition/displayMedicalCondition', view_func=hdbapp.views.viewsMedicalCondition.displayMedicalCondition, methods=['Get', 'POST'])
app.add_url_rule('/medicalCondition/updateMedicalCondition', view_func=hdbapp.views.viewsMedicalCondition.updateMedicalCondition, methods=['Get', 'POST'])

app.add_url_rule('/Ward', view_func=hdbapp.views.viewsWard.ward, methods=['Get', 'POST'])
app.add_url_rule('/Ward/addWard', view_func=hdbapp.views.viewsWard.addWard, methods=['Get', 'POST'])
app.add_url_rule('/Ward/searchHospital', view_func=hdbapp.views.viewsWard.searchWard, methods=['Get', 'POST'])
app.add_url_rule('/Ward/displayHospital', view_func=hdbapp.views.viewsWard.displayWard, methods=['Get', 'POST'])
app.add_url_rule('/Ward/updateHospital', view_func=hdbapp.views.viewsWard.updateWard, methods=['Get', 'POST'])

app.add_url_rule('/statistics', view_func=hdbapp.views.viewsStatistics.statistics, methods=['Get', 'POST'])
app.add_url_rule('/statistics/capacity', view_func=hdbapp.views.viewsStatistics.capacity, methods=['Get', 'POST'])
app.add_url_rule('/statistics/diseaseSum', view_func=hdbapp.views.viewsStatistics.diseaseSum, methods=['Get', 'POST'])
app.add_url_rule('/statistics/doctorOccupance', view_func=hdbapp.views.viewsStatistics.doctorOccupance, methods=['Get', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
