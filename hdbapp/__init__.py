from flask import Flask
import hdbapp.views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'da73c0b0468da6b34c3ed3042c833b22a9981a2e80549059a0b2dc243ad0fc7db03d433988729d0148964816254b8823f29589f03332'


app.add_url_rule('/', view_func=hdbapp.views.home, methods=['Get', 'POST'])
app.add_url_rule('/about', view_func=hdbapp.views.about, methods=['Get', 'POST'])
app.add_url_rule('/register', view_func=hdbapp.views.register, methods=['Get', 'POST'])
app.add_url_rule('/login', view_func=hdbapp.views.login)
app.add_url_rule('/Patient/addPatient', view_func=hdbapp.views.addPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/searchPatient', view_func=hdbapp.views.searchPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/displayPatient', view_func=hdbapp.views.displayPatient, methods=['Get', 'POST'])
app.add_url_rule('/Patient/updatePatient', view_func=hdbapp.views.updatePatient, methods=['Get', 'POST'])

# @app.route('/about')
# @app.route('/register')
# @app.route('/login', methods=['Get', 'POST'])
# @app.route('/Patient/addPatient', methods=['Get', 'POST'])
# @app.route('/Patient/searchPatient', methods=['Get', 'POST'])
# @app.route('/Patient/displayPatient', methods=['Get', 'POST'])
# @app.route('/Patient/updatePatient', methods=['Get', 'POST'])



if __name__ == '__main__':
    app.run(debug=True)
