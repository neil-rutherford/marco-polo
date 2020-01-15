from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class USA_ApplicantScreen(FlaskForm):
        
    us_citizen = SelectField('Are you a citizen of the United States?', 
            choices=[('1', "Yes, I am an American citizen."), ('0', "No, I'm not from the U.S.")], 
            validators=[DataRequired()])

    college = SelectField('Do you have a 4-year college degree?', 
            choices=[('1', "Yes, I'm a college graduate."), ('0', "No, I don't have a college degree.")], 
            validators=[DataRequired()])

    criminal = SelectField('Do you have a criminal record?', 
            choices=[('0', "Yes, I have a criminal record."), ('1', "No, I don't have a criminal record.")], 
            validators=[DataRequired()])
    
    medical = SelectField('Are you aware of any medical issues that may raise concerns in a physical exam?', 
            choices=[('0', 'I have a medical condition that is contagious and/or could endanger others.'), 
                ('1', "I'm in good health.")], 
            validators=[DataRequired()])
    
    work_experience = SelectField('Do you have at least 2 years of work experience after graduation?', 
            choices=[('1', 'Yes, I have two years of work experience.'), 
                ('0', "No, I don't have two years of work experience.")], 
            validators=[DataRequired()])
    
    one_year = SelectField('Can you commit to a 1-year contract?', 
            choices=[('1', "Yes, I can commit to a 1-year contract."), ('0', "I'm not sure.")], 
            validators=[DataRequired()])

    other = SelectField('Is there anything else you feel may affect your ability to legally enter and work in China?',
            choices=[('0', "I'm not certain I can get a visa."), ('1', "Let's get started with the application process!")],
            validators=[DataRequired()])

    terms = SelectField('If your visa application is denied, we will not reimburse your application costs. Do you understand and accept this?',
            choices=[('1', "I understand and accept."), ('0', "I am no longer interested in your program.")], 
            validators=[DataRequired()])

    #recaptcha = RecaptchaField()

    submit = SubmitField('Next >>')


class China_EmployerScreen(FlaskForm):
    
    business_license = SelectField('Do you have a business license?',
            choices=[('1', "Yes, we do."), 
                ('0', "No, we don't.")],
            validators=[DataRequired()])

    education_license = SelectField('Do you have an education license?',
            choices=[('1', 'Yes, we do.'), 
                ('0', "No, we don't.")],
            validators = [DataRequired()])

    z_visa = SelectField('Do you agree to provide the foreign teacher a Chinese work visa (Z visa)?',
            choices=[('1', 'Yes, that is the only legal way to employ a foreigner.'), 
                ('0', "What's a Z visa?")],
            validators=[DataRequired()])
    
    one_year = SelectField('Are you willing to sign a 1-year contract?',
            choices=[('1', 'Yes, we want long-term cooperation.'), 
                ('0', 'No, we are looking for a short-term and/or part-time foreign teacher.')],
            validators=[DataRequired()])

    labor_law = SelectField("Will your contract be in accordance with the Labor Law of the People's Repbulic of China?",
            choices=[('1', 'Yes, that is the only legal way to employ a foreigner.'), 
                ('0', "China has labor laws?")],
            validators=[DataRequired()])

    max_hours = SelectField('Your foreign teacher will not work more than 44 hours per week. Is this acceptable for you?',
            choices=[('1', 'Yes, our foreign teacher will not work more than 44 hours per week.'), 
                ('0', 'No, our foreign teacher must work more than 44 hours per week.')],
            validators=[DataRequired()])

    min_salary = SelectField('If you are located in a first tier city, do you agree to pay your foreign teacher at least 15,000 RMB per month? If you are not located in a first tier city, do you agree to pay your foreign teacher at least 8,000 RMB per month? (This figure does not include benefits, such as rent, utilities, or airfare.)',
            choices=[('1', 'Yes, we agree to pay our foreign teacher at least that much.'), 
                ('0', 'No, we cannot agree to pay our foreign teacher that much.')],
            validators=[DataRequired()])

    payment_time = SelectField('Do you agree to pay your foreign teacher promptly on the first day of each month? (i.e. Payment for work done in October will be paid on October 1.)',
            choices=[('1', 'Yes, we will pay our foreign teacher on the first of the month.'), 
                ('0', 'No, we cannot guarantee that we can pay our employees on time.')],
            validators=[DataRequired()])

    direct_deposit = SelectField('Will you pay your foreign teacher by direct deposit?',
            choices=[('1', 'Yes, we will pay our foreign teacher by direct deposit.'), 
                ('0', 'No, we will pay our foreign teacher in cash.')],
            validators=[DataRequired()])

    housing = SelectField('Do you agree to provide housing for your foreign teacher?',
            choices=[('1', 'Yes, we will provide housing for our foreign teacher.'), 
                ('0', 'No, we cannot agree to do that.')],
            validators=[DataRequired()])

    medical_insurance = SelectField('Do you agree to provide medical insurance to your foreign teacher?',
            choices=[('1', 'Yes, in accordance with Chinese law, we will provide medical insurance.'), 
                ('0', 'No, we cannot agree to do that.')],
            validators=[DataRequired()])

    airfare = SelectField("Do you agree to pay for your foreign teacher's airfare to and from China at the beginning and end of their contract?",
            choices=[('1', 'Yes, we agree to pay airfare to and from China.'), 
                ('0', 'No, we cannot agree to that.')],
            validators=[DataRequired()])

    vacation = SelectField('Do you agree to give your foreign teacher at least 5 days of paid vacation per year (not including Chinese holidays)?',
            choices=[('1', 'Yes, the foreign teacher will get at least 5 days of paid vacation.'), 
                ('0', 'No, we cannot agree to that.')],
            validators=[DataRequired()])

    language = SelectField('The contract must be in both English and Chinese. The English text must match the Chinese text. Do you understand and accept this?',
            choices=[('1', 'Yes, the foreign teacher should be able to read and understand what they are signing.'),
                ('0', "No, we don't think this is important enough to find a translator for.")],
            validators=[DataRequired()])

    service_fee = SelectField("We do our best to screen applicants and ensure they meet our requirements. To contact one of our applicants, you must first pay us. This payment consists of visa reimbursement fees, a finder's fee, and a service fee. In the event that the applicant is denied a visa, we will refund the visa fees and the finder's fee. However, the service fee is non-refundable. Do you understand and accept this?",
            choices=[('1', 'Yes, we understand and accept.'), 
                ('0', "No, we are no longer interested in your service.")],
            validators=[DataRequired()])

    terms = SelectField("For many of our applicants, this is their first time leaving their home country. We want to make sure that they have a pleasant first experience working abroad, so we have certain expectations for our prospective employers. These expectations have been laid out very clearly, and you will accept all of them if you are to use our service. We take violations of these terms very seriously. If we find that you have proposed a contract that violates any of these terms, such as offering to pay 7,500 RMB per month, we have the right to terminate this agreement. We will remove you from our system, add you to our blacklist, and you will not receive any reimbursement. Do you understand and accept this?",
            choices=[('1', 'Yes, we understand and accept.'), 
                ('0', "No, we are no longer interested in your service.")],
            validators=[DataRequired()])

    #recaptcha = RecaptchaField()

    submit = SubmitField('Next >>')


#class USA_ApplicantSignup(FlaskForm):
    #dfsdfs

#class USA_AffiliateSignup(FlaskForm):
    #dfsdfs

#class China_EmployerSignup(FlaskForm):
    #dfsfds

#class China_AffiliateSignup(FlaskForm):
    #dfsdfs
