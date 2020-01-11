from flask import Blueprint, render_template
from flask import current_app as app

app = Blueprint('usa_applicant', __name__,
        template_folder = 'templates',
        static_folder = 'static')

# NEED A DASHBOARD HERE

# APPLICATION PROCESS INFORMATION PAGES

@app.route('/usa-applicant/info/teaching-credential', methods=['GET'])
def info_teaching_credential():
    return render_template('info_teaching_credential.html')

@app.route('/usa-applicant/info/college-diploma', methods=['GET'])
def info_college_diploma():
    return render_template('info_college_diploma.html')

@app.route('/usa-applicant/info/police-clearance', methods=['GET'])
def info_police_clearance():
    return render_template('info_police_clearance.html')

@app.route('/usa-applicant/info/medical-check', methods=['GET'])
def info_medical_check():
    return render_template('info_medical_check.html')

@app.route('/usa-applicant/info/passport', methods=['GET'])
def info_passport():
    return render_template('info_passport.html')

@app.route('/usa-applicant/info/resume', methods=['GET'])
def info_resume():
    return render_template('info_resume.html')

@app.route('/usa-applicant/info/letters-of-recommendation', methods=['GET'])
def info_letters_of_recommendation():
    return render_template('info_letters_of_recommendation.html')

@app.route('/usa-applicant/info/contract', methods=['GET'])
def info_contract():
    return render_template('info_contract.html')

@app.route('/usa-applicant/info/china-flight', methods=['GET'])
def info_china_flight():
    return render_template('info_china_flight.html')

@app.route('/usa-applicant/info/vpn', methods=['GET'])
def info_vpn():
    return render_template('info_vpn.html')

@app.route('/usa-applicant/info/work-visa', methods=['GET'])
def info_work_visa():
    return render_template('info_work_visa.html')

@app.route('/usa-applicant/info/affiliate-disclosure', methods=['GET'])
def info_affiliate_disclosure():
    return render_template('info_affiliate_disclosure.html')

# EMPLOYER REPORTING

# Report a low-ball contract while still in the system
#app.route('/usa-applicant/report/contract#<grievance>')
#def report_contract(grievance):
#    ///////////////////////////////////////

# Report a POS company as an alumnus
#app.route('/report')
#def report_company():
#    ///////////////////////////////////////

# TAKE ACTION

#@app.route('/usa-applicant/get/teaching-credential')
#@app.route('/usa-applicant/get/forms') #diploma, fbi, toefl, medical check
#@app.route('/usa-applicant/download-packet/police-clearance')
#@app.route('/usa-applicant/download-packet/authentications')
#@app.route('/usa-applicant/download-packet/medical-check')
#@app.route('/usa-applicant/get/police-station')
#@app.route('/usa-applicant/get/clinic')
#@app.route('/usa-applicant/get/resume')
#@app.route('/usa-applicant/get/letters-of-recommendation')
#@app.route('/usa-applicant/get/contract')
#@app.route('/usa-applicant/get/china-flight')
#@app.route('/usa-applicant/get/vpn')
#@app.route('/usa-applicant/get/work-visa')

# Receipt uploads

#@app.route('/usa-applicant/upload/teaching-credential', methods=['GET', 'POST'])
#@app.route('/usa-applicant/upload/authentications', methods=['GET', 'POST'])
#@app.route('/usa-applicant/upload/police-clearance', methods=['GET', 'POST'])
#@app.route('/usa-applicant/upload/medical-check', methods=['GET', 'POST'])
#@app.route('/usa-applicant/upload/china-flight', methods=['GET', 'POST'])
#@app.route('/usa-applicant/upload/work-visa', methods=['GET', 'POST'])
