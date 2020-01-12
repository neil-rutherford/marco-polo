from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Screening form that allows us to make assumptions about American applicants and save everyone money
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
    
    work_experience = SelectField('Do you have at least 2 years of experience working in an educational role and/or with children?', 
            choices=[('1', 'Yes, I have two years of relevant work experience.'), 
                ('0', "No, I don't have two years of relevant work experience.")], 
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

#class China_EmployerScreen(FlaskForm):
    #sdffd

#class USA_ApplicantSignup(FlaskForm):
    #dfsdfs

#class USA_AffiliateSignup(FlaskForm):
    #dfsdfs

#class China_EmployerSignup(FlaskForm):
    #dfsfds

#class China_AffiliateSignup(FlaskForm):
    #dfsdfs
