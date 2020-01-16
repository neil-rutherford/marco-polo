from . import db

'''
{GLOBAL DEFINITIONS:}
    IDENTIFYING INFORMATION     : Information used to identify and personalize accounts. Includes login information.
    BREADCRUMBS                 : Better-safe-than-sorry information for analytics and legal cases.
    FOREIGN KEYS                : Shows how this relates to other tables in the database.
    ACTION NEEDED               : Things we need to do on our end (e.g. punish, contact, pay...)
    PROGRESS TRACKING           : Booleans for applicants. False unless completed. Straightforward, so no explanations.
'''

###############################################################
# //////////---------- USA APPLICANT MODEL ----------\\\\\\\\\\
###############################################################

class USA_Applicant(db.Model):
    '''
    ID              : [int]         : Primary key for `usa_applicant` table.
    FIRST_NAME      : [str(35)]     : Applicant's first name.
    LAST_NAME       : [str(35)]     : Applicant's surname.
    EMAIL           : [str(70)      : Applicant's email address / username.
    CELL_PHONE      : [int]         : Applicant's cell number. (+1)
    PASSWORD_HASH   : [str(128)]    : Hashed version of the applicant's password.
    HOME_CITY       : [str(22)]     : City where the applicant lives.
    HOME_STATE      : [int]         : `xyyzzz`, where x is country code, yy is state code, and zzz is county code (CA only).
    HOME_ZIP        : [int]         : Applicant's ZIP code.
    TIMESTAMP       : [datetime]    : When the account was created (UTC).
    CLIENT_ID       : [str(44)]     : UUID starting with 'USA_APP_'. Indicates that they completed the screening form.
    AFFILIATE_ID    : [int]         : Name of `usa_affiliate`, if applicable.
    EMPLOYER_ID     : [int]         : If going to China, this is the employer's id. Otherwise, null.
    '''
    __tablename__ = 'usa_applicant'
    
    # IDENTIFYING INFORMATION
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(35), index = False, unique = False, nullable = False)
    last_name = db.Column(db.String(35), index = False, unique = False, nullable = False)
    email = db.Column(db.String(70), index = False, unique = True, nullable = False)
    cell_phone = db.Column(db.Integer, index = False, unique = True, nullable = False)
    password_hash = db.Column(db.String(128), index = False, unique = False, nullable = False)

    # BREADCRUMBS
    home_city = db.Column(db.String(22), index = False, unique = False, nullable = False)
    home_state = db.Column(db.Integer, index = False, unique = False, nullable = False)
    home_zip = db.Column(db.Integer, index = False, unique = False, nullable = False)
    timestamp = db.Column(db.DateTime, index = False, unique = False, nullable = False, default = datetime.utcnow)
    client_id = db.Column(db.String(44), index = False, unique = True, nullable = False)

    # FOREIGN KEYS
    affiliate_id = db.Column(db.Integer, db.ForeignKey('usa_affiliate.id'), nullable = True)
    employer_id = db.Column(db.Integer, db.ForeignKey('china_employer.id'), nullable = True)
    
    # PROGRESS TRACKING
    is_china_flight = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_college_diploma = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_contract = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_letters_of_recommendation = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_medical_check = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_passport = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_police_clearance = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_resume = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_teaching_credential = db.Column(db.Boolean, index = False, unique = False, nullable = False)
    is_work_visa = db.Column(db.Boolean, index = False, unique = False, nullable = False)

    def __repr__(self):
        return '<USA_Applicant {}>'.format(self.email)


################################################################
# //////////---------- CHINA EMPLOYER MODEL ----------\\\\\\\\\\
################################################################

class China_Employer(db.Model):
    '''
    ID                          : [int]         : `china_employer`表的主键
    SCHOOL_NAME                 : [str(30)]     : 学校名称
    EMAIL                       : [str(70)]     : 邮箱/用户名
    REPRESENTATIVE_NAME         : [str(70)]     : 代表人姓名
    LANDLINE_PHONE              : [int]         : 座机电话号码 (+86)
    CELL_PHONE                  : [int]         : 手机号码 (+86)
    PASSWORD_HASH               : [str(128)]    : 密码的哈希版本
    CLIENT_ID                   : [str(44)]     : 成功完成筛选表格时生成的UID, 'CHI_EMP_'开头
    EDU_JURISDICTION            : [str(10)]     : 教育主管部门
    EDU_LICENSE_NUMBER          : [str(15)]     : 中华人民共和国民办学校办学许可证教民号
    EDU_LICENSE_EXP_DATE        : [datetime]    : 办学许可证失效日期
    BUSINESS_TYPE               : [int]         : 营业类型
    ESTABLISHED_DATE            : [datetime]    : 成立日期
    ADDRESS_PROVINCE            : [int]         : xyyzzz, x=国家代码, yy=省代码, zzz=县代码（现在不支持县代码）
    ADDRESS_CITY                : [str(10)]     : 地址（市）
    ADDRESS_STREET              : [str(30)]     : 地址
    SOCIAL_CREDIT_NUMBER        : [str(18)]     : 统一社会信用代码
    BUSINESS_LICENSE_EXP_DATE   : [datetime]    : 营业执照失效日期
    TIMESTAMP                   : [datetime]    : 帐户创建时间戳(UTC)
    AFFILIATE_ID                : [int]         : 有没有伙伴推荐你使用我们的服务？
    EMPLOYEE_ID                 : [int]         : 有没有请外教为你工作？
    IS_BLACKLIST                : [bool]        : 是否加上黑名单
    '''
    __tablename__ = 'china_employer'

    # IDENTIFYING INFORMATION
    id = db.Column(db.Integer, primary_key = True)
    school_name = db.Column(db.String(30), index = False, unique = True, nullable = False)
    email =  db.Column(db.String(70),index = False,unique = True,nullable = False)
    representative_name = db.Column(db.String(70),index = False,unique = False,nullable = False)
    landline_phone = db.Column(db.Integer,index = False,unique = True,nullable = False)
    cell_phone = db.Column(db.Integer,index = False,unique = True,nullable = False)
    password_hash = db.Column(db.String(128),index = False,unique = False,nullable = False)

    # BREADCRUMBS
    client_id = db.Column(db.String(44), index = False, unique = True, nullable = False)
    edu_jurisdiction = db.Column(db.String(10),index = False,unique = False,nullable = False)
    edu_license_number = db.Column(db.String(15), index = False, unique = True, nullable = False)
    edu_license_exp_date = db.Column(db.DateTime,index = False,unique = False,nullable = False)
    business_type = db.Column(db.Integer,index = False,unique = False,nullable = False)
    established_date = db.Column(db.DateTime,index = False,unique = False,nullable = False)
    address_province = db.Column(db.Integer,index = False,unique = False,nullable = False)
    address_city = db.Column(db.String(10),index = False,unique = False,nullable = False)
    address_street = db.Column(db.String(30),index = False,unique = False,nullable = False)
    social_credit_number = db.Column(db.String(18),index = False,unique = True,nullable = False)
    business_license_exp_date = db.Column(db.DateTime,index = False,unique = False,nullable = False)
    timestamp = db.Column(db.DateTime,index = False,unique = False,nullable = False, default = datetime.utcnow)

    # FOREIGN KEYS
    affiliate_id = db.Column(db.Integer, db.ForeignKey('china_affiliate.id'), nullable = True)
    employee_id = db.relationship('USA_Applicant', backref='employer', lazy='dynamic')

    # ACTION NEEDED
    is_blacklist = db.Column(db.Boolean,index = False,unique = False,nullable = False)

    def __repr__(self):
        return '<China_Employer {}>'.format(self.email)


###############################################################
# //////////---------- USA AFFILIATE MODEL ----------\\\\\\\\\\
###############################################################

class USA_Affiliate(db.Model):
    '''
    ID              : [int]         : Primary key for `usa_affiliate` table.
    EMAIL           : [str(70)]     : Affiliate's email address / username.
    CELL_PHONE      : [int]         : Affiliate's cell phone number (+1).
    PASSWORD_HASH   : [str(128)]    : Hashed version of the affiliate's password.
    FIRST_NAME      : [str(35)]     : Affiliate's first name.
    LAST_NAME       : [str(35)]     : Affiliate's surname.
    CLIENT_ID       : [str(44)]     : UUID generated when screening form was successfully completed. Starts with 'USA_AFF_'.
    ADDRESS_STREET  : [str(35)]     : Affiliate's street address.
    ADDRESS_CITY    : [str(22)]     : What city does the affiliate live in?
    ADDRESS_STATE   : [int]         : xyyzzz, where x is country code, yy is state code, and zzz is county code (if applicable).
    ADDRESS_ZIP     : [int]         : Affiliate's ZIP code?
    TIMESTAMP       : [datetime]    : When the account was created (UTC)
    APPLICANTS      : [int]         : Links to applicants the affiliate recruited.
    SKYPE_ID        : [str(70)]     : Skype ID for contact.
    PAYPAL_EMAIL    : [str(70)]     : PayPal email address for pay-outs.
    '''
    __tablename__ = 'usa_affiliate'

    # IDENTIFYING INFORMATION
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(70), index = False, unique = True, nullable = False)
    cell_phone = db.Column(db.Integer, index = False, unique = True, nullable = False)
    password_hash = db.Column(db.String(128), index = False, unique = False, nullable = False)
    first_name = db.Column(db.String(35), index = False, unique = False, nullable = False)
    last_name = db.Column(db.String(35), index = False, unique = False, nullable = False)

    # BREADCRUMBS
    client_id = db.Column(db.String(44), index = False, unique = True, nullable = False)
    address_street = db.Column(db.String(35), index = False, unique = False, nullable = False)
    address_city = db.Column(db.String(22), index = False, unique = False, nullable = False)
    address_state = db.Column(db.Integer, index = False, unique = False, nullable = False)
    address_zip = db.Column(db.Integer, index = False, unique = False, nullable = False)
    timestamp = db.Column(db.DateTime, index = False, unique = False, nullable = False, default=datetime.utcnow)

    # FOREIGN KEYS
    applicants = db.relationship('USA_Applicant', backref='affiliate', lazy='dynamic')

    # ACTION NEEDED
    skype_id = db.Column(db.String(70), index = False, unique = True, nullable = False)
    paypal_email = db.Column(db.String(70), index = False, unique = True, nullable = False)

    def __repr__(self):
        return '<USA_Affiliate {}>'.format(self.email)


#################################################################
# //////////---------- CHINA AFFILIATE MODEL ----------\\\\\\\\\\
#################################################################

class China_Affiliate(db.Model):
    '''
    ID                  : [int]         : `china_affiliate`表的主键
    EMAIL               : [str(70)]     : 邮箱／用户名
    CELL_PHONE          : [int]         : 手机号码
    PASSWORD_HASH       : [str(128)]    : 密码的哈希版本
    LAST_NAME           : [str(10)]     : 姓
    GIVEN_NAME          : [str(10)]     : 名
    CLIENT_ID           : [str(44)]     : 成功完成筛选表格时生成的UID, 'CHI_AFF_' 开头
    ADDRESS_PROVINCE    : [int]         : xyyzzz, x=国家代码, yy=省代码, zzz=县代码（现在不支持县代码）
    ADDRESS_CITY        : [str(10)]     : 地址（市）
    ADDRESS_STREET      : [str(30)]     : 地址
    TIMESTAMP           : [datetime]    : 帐户创建时间戳(UTC)
    EMPLOYERS           : [int]         : 伙伴推荐的公司
    WECHAT_ID           : [str(70)]     : 伙伴的微信号
    '''
    __tablename__ = 'china_affiliate'

    # IDENTIFYING INFORMATION
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(70),index = False,unique = True,nullable = False)
    cell_phone = db.Column(db.Integer,index = False,unique = True,nullable = False)
    password_hash = db.Column(db.String(128),index = False,unique = False,nullable = False)
    last_name = db.Column(db.String(10),index = False,unique = False,nullable = False)
    given_name = db.Column(db.String(10),index = False,unique = False,nullable = False)

    # BREADCRUMBS
    client_id = db.Column(db.String(44),index = False,unique = True,nullable = False)
    address_province = db.Column(db.Integer,index = False,unique = False,nullable = False)
    address_city = db.Column(db.String(10),index = False,unique = False,nullable = False)
    address_street = db.Column(db.String(30),index = False,unique = False,nullable = False)
    timestamp = db.Column(db.DateTime, index = False, unique = False, nullable = False, default=datetime.utcnow)

    # FOREIGN KEYS
    employers = db.relationship('China_Employer', backref='affiliate', lazy='dynamic')

    # ACTION NEEDED
    wechat_id = db.Column(db.String(70), index = False, unique = True, nullable = False)

    def __repr__(self):
        return '<China_Affiliate {}>'.format(self.email)
