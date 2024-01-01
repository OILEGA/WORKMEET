from app import db
import random,string

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    contact_num = db.Column(db.String(20), nullable=False)
    country_of_residence = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    number_of_users = db.Column(db.Integer, nullable=False)
    freelancer_job_category = db.Column(db.String(50),nullable=False )
    area_of_specialization = db.Column(db.String(50), nullable=False)
    programming_skills_acquired = db.Column(db.String(100), nullable=False)
    years_of_experience = db.Column(db.Integer, nullable=False)
    unique_code = db.Column(db.String(4), unique=True, nullable=False)

#creating a self function that takes in arguments for itself 
    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.generate_unique_code()

#generate a 4 digits unique code
    def generate_unique_code(self):
        code = ''.join(random.choices(string.digits, k=4))

        #checking if the code is unique
        while Registration.query.filter_by(unique_code.code).first() is not None:
            code = ''.join(random.choices(string.digits, k=4))
        self.unique_code = code


    
    

    