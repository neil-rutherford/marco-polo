from flask import Flask

#Blueprint imports
from usa_applicant_system import routes as usa_applicant

#Register blueprints
def get_app():
    app = Flask(__name__)
    #app.config_from_object('config.Config')
    app.register_blueprint(usa_applicant.app)
    return app

app = get_app()

@app.route('/')

@app.route('/index')
def index():
    return "Hello world!"
