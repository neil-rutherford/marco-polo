from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from signup_system.forms import USA_ApplicantScreen, China_EmployerScreen#, USA_ApplicantSignup
import uuid


app = Blueprint('signup', __name__,
        template_folder = 'templates',
        static_folder = 'static')


# Pre-qualifies US applicants and generates the client_id needed to sign up
@app.route('/screen/usa-applicant', methods=['GET', 'POST'])
def screen_usa_applicant():
    form = USA_ApplicantScreen()
    client_id = 'USA_APP_' + str(uuid.uuid4())
    if form.validate_on_submit():
        if form.us_citizen.data == '1' and form.college.data == '1' and form.criminal.data == '1' and form.medical.data == '1' and form.work_experience.data == '1' and form.one_year.data == '1' and form.other.data == '1' and form.terms.data == '1':
            return redirect(url_for('signup.signup_usa_applicant', client_id = client_id))
        else:
            return redirect(url_for('signup.screen_eng_nope'))
    return render_template('screen_usa_applicant.html', form=form)


# Pre-qualifies Chinese employers and generates the client_id needed to sign up
@app.route('/screen/china-employer', methods=['GET', 'POST'])
def screen_china_employer():
    form = China_EmployerScreen()
    client_id = 'CHI_EMP_' + str(uuid.uuid4())
    if form.validate_on_submit():
        if form.business_license.data == '1' and form.education_license.data == '1' and form.z_visa.data == '1' and form.one_year.data == '1' and form.labor_law.data == '1' and form.max_hours.data == '1' and form.min_salary.data == '1' and form.payment_time.data == '1' and form.direct_deposit.data == '1' and form.housing.data == '1' and form.medical_insurance.data == '1' and form.airfare.data == '1' and form.vacation.data == '1' and form.language.data == '1' and form.service_fee.data == '1' and form.terms.data == '1':
            return redirect(url_for('signup.signup_china_employer', client_id = client_id))
        else:
            return redirect(url_for('signup.screen_chi_nope'))
    return render_template('screen_china_employer.html', form=form)


# Failed pre-qualification (English)
@app.route('/screen/eng/nope', methods=['GET'])
def screen_eng_nope():
    return render_template('screen_eng_nope.html')


# Failed pre-qualification (Chinese)
@app.route('/screen/chi/nope', methods=['GET'])
def screen_chi_nope():
    return render_template('screen_chi_nope.html')


# No client_id was provided, so redirect back to the screening page
@app.route('/signup/usa-applicant', methods=['GET'])
def redirect_screen_usa_applicant():
    return redirect(url_for('signup.screen_usa_applicant'))


# Client_id was provided, so start the signup process
@app.route('/signup/usa-applicant/id=<client_id>', methods=['GET', 'POST'])
def signup_usa_applicant(client_id):
    #form = USA_ApplicantSignup()
    if client_id:
        #if form.validate_on_submit():
            #return "Yeehaw bitch"
        #return render_template('signup_usa_applicant.html', form=form)
        return "{}".format(client_id)
    else:
        return redirect(url_for('signup.screen_usa_applicant'))
    return redirect(url_for('signup.screen_usa_applicant'))


# No client_id was provided, so redirect back to the screening page
@app.route('/signup/china-employer', methods=['GET'])
def redirect_screen_china_employer():
    return redirect(url_for('signup.screen_china_employer'))


# Client_id was provided, so start the sign up process
@app.route('/signup/china-employer/id=<client_id>', methods=['GET', 'POST'])
def signup_china_employer(client_id):
    if client_id:
        return "{}".format(client_id)
    else:
        return redirect(url_for('signup.screen_china_employer'))
    return redirect(url_for('signup.screen_china_employer'))


#@app.route('/signup/usa-affiliate')
#def signup_usa_affiliate():
#    return '/////////////////////////////////////////////////'

#@app.route('/signup/china-employer')
#def signup_china_employer():
#    return '/////////////////////////////////////////////////////'

#@app.route('/signup/china-affiliate')
#def signup_china_affiliate():
#    return '/////////////////////////////////////////////////////'
