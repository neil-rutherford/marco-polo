from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from signup_system.forms import USA_ApplicantScreen, China_EmployerScreen, USA_ApplicantSignup, China_EmployerSignup, USA_AffiliateSignup, China_AffiliateSignup
import uuid


app = Blueprint('signup', __name__,
        template_folder = 'templates',
        static_folder = 'static')

###################################################
# //////////---------- SCREENS ----------\\\\\\\\\\
###################################################

# SCREEN: USA APPLICANT

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

# SCREEN: CHINA EMPLOYER

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


######################################################
# //////////---------- FAIL PAGES ----------\\\\\\\\\\
######################################################


# ENGLISH LANGUAGE NOPE
@app.route('/screen/eng/nope', methods=['GET'])
def screen_eng_nope():
    return render_template('screen_eng_nope.html')

# CHINESE LANGUAGE NOPE
@app.route('/screen/chi/nope', methods=['GET'])
def screen_chi_nope():
    return render_template('screen_chi_nope.html')


################################################################
# //////////---------- USA APPLICANT SIGNUP ----------\\\\\\\\\\
################################################################


# NO CLIENT ID?
@app.route('/signup/usa-applicant', methods=['GET'])
def redirect_screen_usa_applicant():
    return redirect(url_for('signup.screen_usa_applicant'))

# USA APPLICANT SIGN UP PAGE
@app.route('/signup/usa-applicant/id=<client_id>', methods=['GET', 'POST'])
def signup_usa_applicant(client_id):
    form = USA_ApplicantSignup()
    if client_id:
        if form.validate_on_submit():
            return "{}".format(form.first_name.data)
        return render_template('signup_usa_applicant.html', form=form)
        #return "{}".format(client_id)
    else:
        return redirect(url_for('signup.screen_usa_applicant'))
    return redirect(url_for('signup.screen_usa_applicant'))

# USA APPLICANT TERMS
@app.route('/terms/usa-applicant/', methods=['GET'])
def terms_usa_applicant():
    return render_template('terms_usa_applicant.html')


#################################################################
# //////////---------- CHINA EMPLOYER SIGNUP ----------\\\\\\\\\\
#################################################################


# NO CLIENT ID?

@app.route('/signup/china-employer', methods=['GET'])
def redirect_screen_china_employer():
    return redirect(url_for('signup.screen_china_employer'))

# CHINA EMPLOYER SIGN UP PAGE

@app.route('/signup/china-employer/id=<client_id>', methods=['GET', 'POST'])
def signup_china_employer(client_id):
    form = China_EmployerSignup()
    if client_id:
        if form.validate_on_submit():
            return ":)"
        return render_template('signup_china_employer.html', form=form)
        #return "{}".format(client_id)
    else:
        return redirect(url_for('signup.screen_china_employer'))
    return redirect(url_for('signup.screen_china_employer'))

# CHINA EMPLOYER TERMS
#///////////////////////////////////////////////////////////////////////////////
@app.route('/terms/china-employer', methods=['GET'])
def terms_china_employer():
    return render_template('terms_china_employer.html')


#################################################################
# //////////---------- USA AFFILIATE SIGN UP ----------\\\\\\\\\\
#################################################################

@app.route('/signup/usa-affiliate', methods=['GET', 'POST'])
def signup_usa_affiliate():
    form = USA_AffiliateSignup()
    client_id = 'USA_AFF_' + str(uuid.uuid4())
    if form.validate_on_submit():
        return client_id
    return render_template('signup_usa_affiliate.html', form=form)

#//////////////////////////////////////////////////////////////////////////////////////
@app.route('/terms/usa-affiliate', methods=['GET'])
def terms_usa_affiliate():
    return render_template('terms_usa_affiliate.html')


###################################################################
# //////////---------- CHINA AFFILIATE SIGN UP ----------\\\\\\\\\\
###################################################################

@app.route('/signup/china-affiliate', methods=['GET', 'POST'])
def signup_china_affiliate():
    form = China_AffiliateSignup()
    client_id = 'CHI_AFF_' + str(uuid.uuid4())
    if form.validate_on_submit():
        return client_id
    return render_template('signup_china_affiliate.html', form=form)

#//////////////////////////////////////////////////////////////////////////////////////
@app.route('/terms/china-affiliate', methods=['GET'])
def terms_china_affiliate():
    return render_template('terms_china_affiliate.html')
