from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from signup_system.forms import USA_ApplicantScreen

app = Blueprint('signup', __name__,
        template_folder = 'templates',
        static_folder = 'static')

@app.route('/screen/usa-applicant', methods=['GET', 'POST'])
def screen_usa_applicant():
    form = USA_ApplicantScreen()
    if form.validate_on_submit():
        if form.us_citizen.data == '1' and form.college.data == '1' and form.criminal.data == '1' and form.medical.data == '1' and form.work_experience.data == '1' and form.one_year.data == '1' and form.other.data == '1' and form.terms.data == '1':
            return redirect('/')
            #return redirect(url_for('signup_usa_applicant'))
        else:
            return redirect(url_for('signup.screen_nope'))
    return render_template('screen_usa_applicant.html', form=form)

@app.route('/screen/nope', methods=['GET'])
def screen_nope():
    #return render_template('screen_nope.html')
    return "Oh noooooOooooOOooOOOOOOOoooooo FUCKKKKKKKKK"

#@app.route('/signup/usa_applicant', methods=['GET', 'POST'])
#def signup_usa_applicant():
#    return '//////////////////////////////////////////////////'

#@app.route('/signup/usa_affiliate')
#def signup_usa_affiliate():
#    return '/////////////////////////////////////////////////'

#@app.route('/signup/china_employer')
#def signup_china_employer():
#    return '/////////////////////////////////////////////////////'

#@app.route('/signup/china_affiliate')
#def signup_china_affiliate():
#    return '/////////////////////////////////////////////////////'
