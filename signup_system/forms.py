from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import datetime


####################
# //-- CONTENTS --\\
####################

# 1. CUSTOM VALIDATORS
# 2. USA APPLICANT SCREEN
# 3. CHINA EMPLOYER SCREEN
# 4. USA APPLICANT SIGNUP
# 5. CHINA EMPLOYER SIGNUP
# 6. USA AFFILIATE SIGNUP
# 7. CHINA AFFILIATE SIGNUP


#############################################################
# //////////---------- CUSTOM VALIDATORS ----------\\\\\\\\\\
#############################################################

#######################################
# //-- ENGLISH LANGUAGE VALIDATORS --\\
#######################################

def ENG_no_symbols(form, field):
    iffy = ['<','>','/',':', ';', '=', '"', '`', '(', ')', '!', '#', '*', '$', '%', '{', '}', '[', ']', '?', '~']
    for character in str(field.data):
        if character in iffy:
            raise ValidationError("Your response contains characters that are not allowed.")

def ENG_phone_check(form, field):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for character in str(field.data):
        if character == '-':
            raise ValidationError("We're expecting something like 1112223333, not 111-222-3333.")
        elif character not in numbers:
            raise ValidationError('Numbers only, please.')

def ENG_password_check(form, field):
    if form.password.data != form.verify_password.data:
        raise ValidationError('Passwords must match.')

def ENG_california_check(form, field):
    if form.home_state.data == '105000' and form.ca_county.data == 'NA':
        raise ValidationError('Two embassies service California, so we need to know what county you live in.')
    elif form.home_state.data != '105000' and form.ca_county.data != 'NA':
        raise ValidationError('County clarification is only required for California residents. If you are not from California, please select "Not Applicable".')

def ENG_dob_check(form, field):
    age = datetime.date.today() - field.data
    if age < datetime.timedelta(days=6570):
        raise ValidationError('You cannot work for us because you are not 18 years old.')

#######################################
# //-- CHINESE LANGUAGE VALIDATORS --\\
#######################################

def CHI_hanzi_only(form, field):
    '''
    FUNCTION:       Only Chinese characters are allowed. No English letters, no symbols, and no numbers.
    ERROR MESSAGE:  Only Chinese characters are allowed.
    '''
    iffy = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            '~','`','1','!','2','@','3','#','4','$','5','%','6','^','7','&','8','*','9','(','0',')','-','_','+','=','[','{',']','}',
            ':',';','"',"'",'|','<',',','.','>','?','/']
    for character in str(field.data):
        if character in iffy:
            raise ValidationError("仅输入中文字。")

def CHI_no_symbols(form, field):
    '''
    FUNCTION:       English letters and numbers are allowed, but no symbols.
    ERROR MESSAGE:  Sorry, your response contains symbols that are not allowed.
    '''
    iffy = ['<','>','/',':',';','=','"',"'",'`','(',')','!','#', '*', '$', '%', '{','}','[',']','?','~']
    for character in str(field.data):
        if character in iffy:
            raise ValidationError("抱歉，您的回复中包含不允许的符号。")

def CHI_password_check(form, field):
    '''
    FUNCTION:       EqualTo was displaying stdout errors in the browser, so I made my own.
    ERROR MESSAGE:  The two passwords do not match!
    '''
    if form.password.data != form.verify_password.data:
        raise ValidationError('两个密码不匹配!')

def CHI_phone_check(form, field):
    '''
    FUNCTION:       Numbers only.
    ERROR MESSAGE:  You are only allowed to enter numbers.
    '''
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for character in str(field.data):
        if character not in numbers:
            raise ValidationError('仅输入数字')

def CHI_province_check(form, field):
    '''
    IF FUNCTION:    Catches addresses in Hong Kong, Macau, and Taiwan.
    ERROR MESSAGE:  The visa process in your province is different from Mainland China. Therefore, we currently cannot accept your application. Thank you for your understanding.
    
    ELIF FUNCTION:  Catches addresses in Xinjiang and Tibet.
    ERROR MESSAGE:  Your area is currently very politically sensitive, so foreigners have a hard time applying for visas in your area. Therefore, we have chosen not to accept applications from schools in your area. Thank you for your understanding.
    '''
    if form.address_province.data == '113000' or form.address_province.data == '121000' or form.address_province.data == '129000':
        raise ValidationError('您所在省的簽證要求與中國大陸不同。因此，我們目前無法接受您的申請，感謝您的理解。')
    elif form.address_province.data == '131000' or form.address_province.data == '132000':
        raise ValidationError('因为您所在自治区目前政治敏感性非常高，所以我们的外教很难在您所在地区申请工作签证。因此，我们公司选择不接受您所在自治区的学校申请，感谢您的理解。')

def CHI_address_check(form, field):
    '''
    FUNCTION:       No English letters or symbols.
    ERROR MESSAGE:  You are only allowed to enter Chinese characters and numbers.
    '''
    iffy = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            '~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[','{',']','}',
            ':',';','"',"'",'|','<',',','.','>','?','/']
    for character in str(field.data):
        if character in iffy:
            raise ValidationError("仅输入中文字和数字。")

def CHI_exp_date_check(form, field):
    '''
    FUNCTION:       Checks to see if it's already expired.
    ERROR MESSAGE:  You cannot enter expired information.
    '''
    time_left = field.data - datetime.date.today()
    if time_left < datetime.timedelta(days=0):
        raise ValidationError('不能输入已过期的信息。')

def CHI_est_date_check(form, field):
    '''
    FUNCTION:       Checks to see if the establishment date is in the future.
    ERROR MESSAGE:  Companies that have not yet been founded cannot use our service.
    '''
    time_since = datetime.date.today() - field.data
    if time_since < datetime.timedelta(days=0):
        raise ValidationError('未成立的公司不能用我们的服务。')

def CHI_dob_check(form, field):
    '''
    FUNCTION:       Checks to see if affiliate is at least 18 years old.
    ERROR MESSAGE:  In accordance with Chinese laws, you must be at least 18 years old to work for us.
    '''
    age = datetime.date.today() - field.data
    if age < datetime.timedelta(days=6570):
        raise ValidationError('根据中国法律，您必须年满18岁才能为我们工作。')


################################################################
# //////////---------- USA APPLICANT SCREEN ----------\\\\\\\\\\
################################################################

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


#################################################################
# //////////---------- CHINA EMPLOYER SCREEN ----------\\\\\\\\\\
#################################################################

class China_EmployerScreen(FlaskForm):
    
    business_license = SelectField('您有营业执照吗？',
            choices=[('1', "有"), 
                ('0', "没有")],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    education_license = SelectField('您有民办学校办学许可证吗？',
            choices=[('1', '有'), 
                ('0', "没有")],
            validators = [DataRequired(message='抱歉，此字段不能为空。')])

    z_visa = SelectField('您是否同意向外教提供中国工作签证（Z 签证）？',
            choices=[('1', '同意，这是雇用外国人的唯一合法方法。'), 
                ('0', "Z 签证是什么东西？")],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])
    
    one_year = SelectField('您愿意签一年的合同吗？',
            choices=[('1', '愿意，我们想要长期合作。'), 
                ('0', '不愿意，我们要短期 / 兼职的外教。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    labor_law = SelectField("您的合同是否符合《中华人民共和国劳动法》？",
            choices=[('1', '是的，这是雇用外国人的唯一合法方法。'), 
                ('0', "中华人民共和国有劳动法吗？")],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    max_hours = SelectField('您的外籍老师每周工作时间不会超过44小时。您可以接受吗？',
            choices=[('1', '接受，我们的外籍老师每周工作时间不会超过44小时。'), 
                ('0', '不接受，我们的外籍老师每周工作时间肯定会超过44小时。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    min_salary = SelectField('如果您位于一线城市，您是否同意每月向您的外籍教师支付至少15,000人民币的薪水？ 如果您不在一线城市，您是否同意每月向您的外籍教师支付至少8,000人民币的薪水？ （此数字不包括诸如租金、水电费、机票等福利。）',
            choices=[('1', '我们同意至少付给我们的外籍老师那么多。'), 
                ('0', '我们不能同意向我们的外国老师支付那么多钱。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    payment_time = SelectField('您是否同意在每个月的第一天及时向您的外籍教师付款？ （即，10月完成的工作将在10月1日支付。）',
            choices=[('1', '同意，我们会在每月的第一天付钱给我们的外籍老师。'), 
                ('0', '我们不能保证我们会准时向员工付款。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    direct_deposit = SelectField('您会将外籍教师的工资存入银行帐户吗？',
            choices=[('1', '当然！'), 
                ('0', '不，我们将用现金支付外籍老师。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    housing = SelectField('您是否同意为您的外籍老师提供住房？',
            choices=[('1', '是的，我们将为外教提供住房。'), 
                ('0', '不同意。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    medical_insurance = SelectField('您是否同意为外籍老师提供医疗保险？',
            choices=[('1', '根据中国法律，我们将提供医疗保险。'), 
                ('0', '不同意。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    airfare = SelectField("您是否同意在合同开始和结束时为您的外籍老师来往中国的机票付款？",
            choices=[('1', '同意。'), 
                ('0', '不同意。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    vacation = SelectField('您是否同意每年给您的外籍教师至少5天的带薪假期（不包括中国假期）？',
            choices=[('1', '同意，外籍老师将获得至少5天的带薪假期。'), 
                ('0', '不同意。')],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    language = SelectField('合同必须使用英文和中文。 英文文本必须与中文文本匹配。 您了解并接受吗？',
            choices=[('1', '接受，外籍老师应该能够阅读和理解他们所签署的内容。'),
                ('0', "No, we don't think this is important enough to find a translator for.")],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    service_fee = SelectField("我们会尽力筛选申请人，并确保他们符合我们的要求。要联系我们的一位申请人，您先必须向我们付款。这笔费用包括签证费用、推荐费、服务费。如果申请人被拒绝签证，我们将退还签证费和推荐费给您。但是，服务费不予退还。您了解并接受吗？",
            choices=[('1', '了解并接受。'), 
                ('0', "我们不再对您的服务感兴趣。")],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    terms = SelectField("对于我们的许多申请人来说，这是他们第一次离开自己的国家。为了确保他们有愉快的初国外工作体验，我们为潜在的雇主制定了一些标准。这些标准已经非常清楚地列出，如果您要使用我们的服务，则将接受所有这些标准。我们非常重视违反这些条款的行为。如果我们发现您提出的合同违反了我们的任何条款，我们有权终止本协议。我们会将您从系统中删除，我们会将您添加到我们的黑名单中，并且您不会收到任何报销。您了解并接受吗？",
            choices=[('1', '了解并接受。'), 
                ('0', "我们不再对您的服务感兴趣。")],
            validators=[DataRequired(message='抱歉，此字段不能为空。')])

    #recaptcha = RecaptchaField()

    submit = SubmitField('下一步 >>')


################################################################
# //////////---------- USA APPLICANT SIGNUP ----------\\\\\\\\\\
################################################################

class USA_ApplicantSignup(FlaskForm):
    
    first_name = StringField('First name', 
            validators=[DataRequired(), 
                Length(min=2, max=35), 
                ENG_no_symbols])

    last_name = StringField('Last name',
            validators=[DataRequired(), 
                Length(min=2, max=35), 
                ENG_no_symbols])

    email = StringField('Email',
            validators=[DataRequired(), 
                Length(max=70), 
                Email()])

    cell_phone = StringField('Cell phone number',
            validators=[DataRequired(), 
                Length(min=10, max=10), 
                ENG_phone_check])

    password = PasswordField('Password (minimum of 8 characters)',
            validators=[DataRequired(), 
                Length(min=8)])

    verify_password = PasswordField('Verify your password',
            validators=[DataRequired(), 
                ENG_password_check])

    home_city = StringField('What city do you live in?',
            validators=[DataRequired(), 
                Length(min=3, max=22), 
                ENG_no_symbols])

    home_state = SelectField('What state do you live in?', choices=[
        ('101000', 'Alabama'),
        ('102000', 'Alaska'),
        ('103000', 'Arizona'),
        ('104000', 'Arkansas'),
        ('105000', 'California'),
        ('106000', 'Colorado'),
        ('107000', 'Connecticut'),
        ('108000', 'Delaware'),
        ('109000', 'District of Columbia'),
        ('110000', 'Florida'),
        ('111000', 'Georgia'),
        ('112000', 'Hawaii'),
        ('113000', 'Idaho'),
        ('114000', 'Illinois'),
        ('115000', 'Indiana'),
        ('116000', 'Iowa'),
        ('117000', 'Kansas'),
        ('118000', 'Kentucky'),
        ('119000', 'Lousiana'),
        ('120000', 'Maine'),
        ('121000', 'Maryland'),
        ('122000', 'Massachusetts'),
        ('123000', 'Michigan'),
        ('124000', 'Minnesota'),
        ('125000', 'Mississippi'),
        ('126000', 'Missouri'),
        ('127000', 'Montana'),
        ('128000', 'Nebraska'),
        ('129000', 'Nevada'),
        ('130000', 'New Hampshire'),
        ('131000', 'New Jersey'),
        ('132000', 'New Mexico'),
        ('133000', 'New York'),
        ('134000', 'North Carolina'),
        ('135000', 'North Dakota'),
        ('136000', 'Ohio'),
        ('137000', 'Oklahoma'),
        ('138000', 'Oregon'),
        ('139000', 'Pennsylvania'),
        ('140000', 'Rhode Island'),
        ('141000', 'South Carolina'),
        ('142000', 'South Dakota'),
        ('143000', 'Tennessee'),
        ('144000', 'Texas'),
        ('145000', 'Utah'),
        ('146000', 'Vermont'),
        ('147000', 'Virginia'),
        ('148000', 'Washington'),
        ('149000', 'West Virginia'),
        ('150000', 'Wisconsin'),
        ('151000', 'Wyoming')],
        validators=[DataRequired()])

    ca_county = SelectField('California residents: What county do you live in? (If you do not live in California, choose "Not applicable -- I do not live in California."', choices=[
        ('NA', 'Not applicable -- I do not live in California.'),
        ('105001', 'Alameda'),
        ('105002', 'Alpine'),
        ('105003', 'Amador'),
        ('105004', 'Butte'),
        ('105005', 'Calaveras'),
        ('105006', 'Colusa'),
        ('105007', 'Contra Costa'),
        ('105008', 'Del Norte'),
        ('105009', 'El Dorado'),
        ('105010', 'Fresno'),
        ('105011', 'Glenn'),
        ('105012', 'Humboldt'),
        ('105013', 'Imperial'),
        ('105014', 'Inyo'),
        ('105015', 'Kern'),
        ('105016', 'Kings'),
        ('105017', 'Lake'),
        ('105018', 'Lassen'),
        ('105019', 'Los Angeles'),
        ('105020', 'Madera'),
        ('105021', 'Marin'),
        ('105022', 'Mariposa'),
        ('105023', 'Mendocino'),
        ('105024', 'Merced'),
        ('105025', 'Modoc'),
        ('105026', 'Mono'),
        ('105027', 'Monterey'),
        ('105028', 'Napa'),
        ('105029', 'Nevada'),
        ('105030', 'Orange'),
        ('105031', 'Placer'),
        ('105032', 'Plumas'),
        ('105033', 'Riverside'),
        ('105034', 'Sacramento'),
        ('105035', 'San Benito'),
        ('105036', 'San Bernardino'),
        ('105037', 'San Diego'),
        ('105038', 'San Francisco'),
        ('105039', 'San Joaquin'),
        ('105040', 'San Luis Obispo'),
        ('105041', 'San Mateo'),
        ('105042', 'Santa Barbara'),
        ('105043', 'Santa Clara'),
        ('105044', 'Santa Cruz'),
        ('105045', 'Shasta'),
        ('105046', 'Sierra'),
        ('105047', 'Siskiyou'),
        ('105048', 'Solano'),
        ('105049', 'Sonoma'),
        ('105050', 'Stanislaus'),
        ('105051', 'Sutter'),
        ('105052', 'Tehama'),
        ('105053', 'Trinity'),
        ('105054', 'Tulare'),
        ('105055', 'Tuolumne'),
        ('105056', 'Ventura'),
        ('105057', 'Yolo'),
        ('105058', 'Yuba')],
        validators=[DataRequired(), 
                ENG_california_check])

    home_zip = StringField('ZIP code',
            validators=[DataRequired(), 
                Length(min=5, max=5), 
                ENG_phone_check])

    submit = SubmitField('Sign up')


#################################################################
# //////////---------- CHINA EMPLOYER SIGNUP ----------\\\\\\\\\\
#################################################################

class China_EmployerSignup(FlaskForm):

    school_name_chi = StringField('学校名称（中文）',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=5, max=30, message='抱歉，您的回复必须在5和30个字符之间。'),
                CHI_hanzi_only])

    school_name_eng = StringField('学校名称（英文）',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=10, max=100, message='抱歉，您的回复必须在10和100个字符之间。'),
                CHI_no_symbols])

    email = StringField('邮箱',
            validators=[DataRequired(message='抱歉，此字段不能为空。'), 
                Length(max=70, message='抱歉，您的回复太长。'), 
                Email(message='抱歉，您没有输入有效的电子邮件地址。')])

    password = PasswordField('密码（至少8字符）',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=8, message='抱歉，您的密码必须至少8个字符长。')])

    verify_password = PasswordField('确认密码',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                CHI_password_check])

    cell_phone = StringField('代表人手机号码',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=11, max=11, message='抱歉，您的回复必须为11个字符长。'),
                CHI_phone_check])

    landline_phone = StringField('座机电话号码',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=11, max=11, message='抱歉，您的回复必须为11个字符长。'),
                CHI_phone_check])

    representative_name = StringField('代表人姓名',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=2, max=70, message='抱歉，您的回复必须在2和70个字符之间。'),
                CHI_no_symbols])

    edu_jurisdiction = StringField('教育主管部门',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=2, max=10, message='抱歉，您的回复必须在2和10个字符之间。'),
                CHI_hanzi_only])

    edu_license_number = StringField('中华人民共和国民办学校办学许可证教民号',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=15, max=15, message='抱歉，您的回复必须为15个字符长。'),
                CHI_no_symbols])

    edu_license_exp_date = DateField('办学许可证失效日期 (yyyy-mm-dd)',
            validators=[DataRequired(message='请确保您输入的日期是用【年年年年－月月－日日】格式。'),
                CHI_exp_date_check])

    business_type = SelectField('营业类型', choices=[
        ('01', '有限责任公司'),     # Limited liability company
        ('02', '股份有限公司'),     # Joint-stock company
        ('03', '有限合伙企业'),     # Limited partnership
        ('04', '外商独资公司'),     # Wholly foreign owned company
        ('05', '个人独资企业'),     # Individual proprietorship
        ('06', '国有独资公司'),     # Wholly state-owned company
        ('07', '其他')],            # Other
        validators=[DataRequired(message='抱歉，此字段不能为空。')])

    established_date = DateField('成立日期 (yyyy-mm-dd)',
            validators=[DataRequired(message='请确保您输入的日期是用【年年年年－月月－日日】格式。'),
                CHI_est_date_check])

    address_province = SelectField('地址（省）', choices=[
        ('101000', '安徽省'),           # Anhui
        ('102000', '北京市'),           # Beijing
        ('103000', '重庆市'),           # Chongqing
        ('104000', '福建省'),           # Fujian
        ('105000', '甘肃省'),           # Gansu
        ('106000', '广东省'),           # Guangdong
        ('107000', '广西壮族自治区'),   # Guangxi 
        ('108000', '贵州省'),           # Guizhou
        ('109000', '海南省'),           # Hainan
        ('110000', '河北省'),           # Hebei
        ('111000', '黑龙江省'),         # Heilongjiang
        ('112000', '河南省'),           # Henan
        ('113000', '香港特别行政区'),   # Hong Kong -- throws "different visa system" error
        ('114000', '湖北省'),           # Hubei
        ('115000', '湖南省'),           # Hunan
        ('116000', '內蒙古自治区'),     # Inner Mongolia
        ('117000', '江苏省'),           # Jiangsu
        ('118000', '江西省'),           # Jiangxi
        ('119000', '吉林省'),           # Jilin
        ('120000', '辽宁省'),           # Liaoning
        ('121000', '澳门特别行政区'),   # Macau -- throws "different visa system" error
        ('122000', '宁夏回族自治区'),   # Ningxia
        ('123000', '青海省'),           # Qinghai
        ('124000', '陕西省'),           # Shaanxi
        ('125000', '山东省'),           # Shandong
        ('126000', '上海市'),           # Shanghai
        ('127000', '山西省'),           # Shandong
        ('128000', '四川省'),           # Sichuan
        ('129000', '台湾省'),           # Taiwan -- throws "different visa system" error
        ('130000', '天津市'),           # Tianjin
        ('131000', '西藏自治区'),       # Tibet -- throws "politically sensitive" error
        ('132000', '新疆维吾尔自治区'), # Xinjiang -- throws "politically sensitive" error
        ('133000', '云南省'),           # Yunnan
        ('134000', '浙江省')],          # Zhejiang
        validators=[DataRequired(message='抱歉，此字段不能为空。'), 
            CHI_province_check])

    address_city = StringField('地址（市）',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=2, max=10, message='抱歉，您的回复必须在2和10个字符之间。'),
                CHI_hanzi_only])

    address_street = StringField('地址',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=5, max=30, message='抱歉，您的回复必须在5和30个字符之间。'),
                CHI_address_check])

    social_credit_number = StringField('统一社会信用代码',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=18, max=18, message='抱歉，您的回复必须为18个字符长。'),
                CHI_no_symbols])

    business_license_exp_date = DateField('营业执照失效日期 (yyyy-mm-dd)',
            validators=[DataRequired(message='请确保您输入的日期是用【年年年年－月月－日日】格式。'),
                CHI_exp_date_check])

    submit = SubmitField('注册')


################################################################
# //////////---------- USA AFFILIATE SIGNUP ----------\\\\\\\\\\
################################################################

class USA_AffiliateSignup(FlaskForm):
    
    first_name = StringField('First name',
            validators=[DataRequired(), 
                Length(min=2,max=35), 
                ENG_no_symbols])
    
    last_name = StringField('Last name',
            validators=[DataRequired(), 
                Length(min=2,max=35), 
                ENG_no_symbols])
    
    dob = DateField('Date of birth (yyyy-mm-dd)',
            validators=[DataRequired(message='Make sure your response is in yyyy-mm-dd format.'),
                ENG_dob_check])
    
    email = StringField('Email',
            validators=[DataRequired(), 
                Email(), 
                Length(max=70)])
    
    password = PasswordField('Password (minimum of 8 characters)',
            validators=[DataRequired(), 
                Length(min=8)])
    
    verify_password = PasswordField('Verify password',
            validators=[DataRequired(),
                ENG_password_check])
    
    cell_phone = StringField('Cell phone number',
            validators=[DataRequired(), 
                Length(min=10, max=10), 
                ENG_phone_check])
    
    skype_id = StringField('Skype ID',
            validators=[DataRequired(), 
                Length(max=70), 
                ENG_no_symbols])
    
    paypal_email = StringField('PayPal email',
            validators=[DataRequired(), 
                Email(), 
                Length(max=70)])
    
    home_street = StringField('Street address',
            validators=[DataRequired(), 
                Length(min=7, max=35), 
                ENG_no_symbols])
    
    home_city = StringField('City',
            validators=[DataRequired(), 
                Length(min=3, max=22), 
                ENG_no_symbols])
    
    home_state = SelectField('State', choices=[
        ('101000', 'Alabama'),
        ('102000', 'Alaska'),
        ('103000', 'Arizona'),
        ('104000', 'Arkansas'),
        ('105000', 'California'),
        ('106000', 'Colorado'),
        ('107000', 'Connecticut'),
        ('108000', 'Delaware'),
        ('109000', 'District of Columbia'),
        ('110000', 'Florida'),
        ('111000', 'Georgia'),
        ('112000', 'Hawaii'),
        ('113000', 'Idaho'),
        ('114000', 'Illinois'),
        ('115000', 'Indiana'),
        ('116000', 'Iowa'),
        ('117000', 'Kansas'),
        ('118000', 'Kentucky'),
        ('119000', 'Lousiana'),
        ('120000', 'Maine'),
        ('121000', 'Maryland'),
        ('122000', 'Massachusetts'),
        ('123000', 'Michigan'),
        ('124000', 'Minnesota'),
        ('125000', 'Mississippi'),
        ('126000', 'Missouri'),
        ('127000', 'Montana'),
        ('128000', 'Nebraska'),
        ('129000', 'Nevada'),
        ('130000', 'New Hampshire'),
        ('131000', 'New Jersey'),
        ('132000', 'New Mexico'),
        ('133000', 'New York'),
        ('134000', 'North Carolina'),
        ('135000', 'North Dakota'),
        ('136000', 'Ohio'),
        ('137000', 'Oklahoma'),
        ('138000', 'Oregon'),
        ('139000', 'Pennsylvania'),
        ('140000', 'Rhode Island'),
        ('141000', 'South Carolina'),
        ('142000', 'South Dakota'),
        ('143000', 'Tennessee'),
        ('144000', 'Texas'),
        ('145000', 'Utah'),
        ('146000', 'Vermont'),
        ('147000', 'Virginia'),
        ('148000', 'Washington'),
        ('149000', 'West Virginia'),
        ('150000', 'Wisconsin'),
        ('151000', 'Wyoming')],
        validators=[DataRequired()])
    
    ca_county = SelectField('California residents: What county do you live in? (If you do not live in California, choose "Not applicable -- I do not live in California."', choices=[
        ('NA', 'Not applicable -- I do not live in California.'),
        ('105001', 'Alameda'),
        ('105002', 'Alpine'),
        ('105003', 'Amador'),
        ('105004', 'Butte'),
        ('105005', 'Calaveras'),
        ('105006', 'Colusa'),
        ('105007', 'Contra Costa'),
        ('105008', 'Del Norte'),
        ('105009', 'El Dorado'),
        ('105010', 'Fresno'),
        ('105011', 'Glenn'),
        ('105012', 'Humboldt'),
        ('105013', 'Imperial'),
        ('105014', 'Inyo'),
        ('105015', 'Kern'),
        ('105016', 'Kings'),
        ('105017', 'Lake'),
        ('105018', 'Lassen'),
        ('105019', 'Los Angeles'),
        ('105020', 'Madera'),
        ('105021', 'Marin'),
        ('105022', 'Mariposa'),
        ('105023', 'Mendocino'),
        ('105024', 'Merced'),
        ('105025', 'Modoc'),
        ('105026', 'Mono'),
        ('105027', 'Monterey'),
        ('105028', 'Napa'),
        ('105029', 'Nevada'),
        ('105030', 'Orange'),
        ('105031', 'Placer'),
        ('105032', 'Plumas'),
        ('105033', 'Riverside'),
        ('105034', 'Sacramento'),
        ('105035', 'San Benito'),
        ('105036', 'San Bernardino'),
        ('105037', 'San Diego'),
        ('105038', 'San Francisco'),
        ('105039', 'San Joaquin'),
        ('105040', 'San Luis Obispo'),
        ('105041', 'San Mateo'),
        ('105042', 'Santa Barbara'),
        ('105043', 'Santa Clara'),
        ('105044', 'Santa Cruz'),
        ('105045', 'Shasta'),
        ('105046', 'Sierra'),
        ('105047', 'Siskiyou'),
        ('105048', 'Solano'),
        ('105049', 'Sonoma'),
        ('105050', 'Stanislaus'),
        ('105051', 'Sutter'),
        ('105052', 'Tehama'),
        ('105053', 'Trinity'),
        ('105054', 'Tulare'),
        ('105055', 'Tuolumne'),
        ('105056', 'Ventura'),
        ('105057', 'Yolo'),
        ('105058', 'Yuba')],
        validators=[DataRequired(), 
                ENG_california_check])

    home_zip = StringField('ZIP code',
            validators=[DataRequired(),
                Length(min=5,max=5),
                ENG_phone_check])
    
    # recaptcha
    
    submit = SubmitField('Sign up')


##################################################################
# //////////---------- CHINA AFFILIATE SIGNUP ----------\\\\\\\\\\
##################################################################

class China_AffiliateSignup(FlaskForm):

    last_name = StringField('姓',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(max=35, message='抱歉，您的回复必须在1和35个字符之间。'),
                CHI_no_symbols])

    given_name = StringField('名',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(max=35, message='抱歉，您的回复必须在1和35个字符之间。'),
                CHI_no_symbols])

    dob = DateField('出生日期 (yyyy-mm-dd)',
            validators=[DataRequired(message='请确保您输入的日期是用【年年年年－月月－日日】格式。'),
                CHI_dob_check])

    email = StringField('邮箱',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(max=70, message='抱歉，您的回复太长。'),
                Email(message='抱歉，您没有输入有效的电子邮件地址。')])

    cell_phone = StringField('手机号',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=11, max=11, message='抱歉，您的回复必须为11个字符长。'),
                CHI_phone_check])

    password = PasswordField('密码（至少8字符）',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=8, message='抱歉，您的密码必须至少8个字符长。')])

    verify_password = PasswordField('确认密码',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                CHI_password_check])

    address_province = SelectField('地址（省）', choices=[
        ('101000', '安徽省'),           # Anhui
        ('102000', '北京市'),           # Beijing
        ('103000', '重庆市'),           # Chongqing
        ('104000', '福建省'),           # Fujian
        ('105000', '甘肃省'),           # Gansu
        ('106000', '广东省'),           # Guangdong
        ('107000', '广西壮族自治区'),   # Guangxi
        ('108000', '贵州省'),           # Guizhou
        ('109000', '海南省'),           # Hainan
        ('110000', '河北省'),           # Hebei
        ('111000', '黑龙江省'),         # Heilongjiang
        ('112000', '河南省'),           # Henan
        ('113000', '香港特别行政区'),   # Hong Kong -- throws "different visa system" error
        ('114000', '湖北省'),           # Hubei
        ('115000', '湖南省'),           # Hunan
        ('116000', '內蒙古自治区'),     # Inner Mongolia
        ('117000', '江苏省'),           # Jiangsu
        ('118000', '江西省'),           # Jiangxi
        ('119000', '吉林省'),           # Jilin
        ('120000', '辽宁省'),           # Liaoning
        ('121000', '澳门特别行政区'),   # Macau -- throws "different visa system" error
        ('122000', '宁夏回族自治区'),   # Ningxia
        ('123000', '青海省'),           # Qinghai
        ('124000', '陕西省'),           # Shaanxi
        ('125000', '山东省'),           # Shandong
        ('126000', '上海市'),           # Shanghai
        ('127000', '山西省'),           # Shandong
        ('128000', '四川省'),           # Sichuan
        ('129000', '台湾省'),           # Taiwan -- throws "different visa system" error
        ('130000', '天津市'),           # Tianjin
        ('131000', '西藏自治区'),       # Tibet -- throws "politically sensitive" error
        ('132000', '新疆维吾尔自治区'), # Xinjiang -- throws "politically sensitive" error
        ('133000', '云南省'),           # Yunnan
        ('134000', '浙江省')],          # Zhejiang
        validators=[DataRequired(message='抱歉，此字段不能为空。'),
            CHI_province_check])

    address_city = StringField('地址（市）',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=2, max=10, message='抱歉，您的回复必须在2和10个字符之间。'),
                CHI_hanzi_only])

    address_street = StringField('地址',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(min=5, max=30, message='抱歉，您的回复必须在5和30个字符之间。'),
                CHI_address_check])

    wechat_id = StringField('微信用户名',
            validators=[DataRequired(message='抱歉，此字段不能为空。'),
                Length(max=70, message='太长了！'),
                CHI_no_symbols])

    # recaptcha

    submit = SubmitField('注册')
