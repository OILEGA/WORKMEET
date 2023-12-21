from app import db

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact_num = db.Column(db.String(20), nullable=False)
    country_of_residence = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    freelancer_job_category = db.Column(db.String(50),nullable=False )
    area_of_specialization = db.Column(db.String(50), nullable=False)
    programming_skills_acquired = db.Column(db.String(100), nullable=False)
    years_of_experience = db.Column(db.Integer, nullable=False)
    

    