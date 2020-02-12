# Functional imports
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Blueprint imports
from usa_applicant_system import routes as usa_applicant
from signup_system import routes as signup

def get_app():
    # Initialize
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    # Register blueprints
    app.register_blueprint(usa_applicant.app)
    app.register_blueprint(signup.app)
    return app

app = get_app()

@app.route('/')

@app.route('/index')
def index():
    return "Hello world!"



if __name__ == '__main__':
    app.run(host ='0.0.0.0', port =5000, debug = True)
