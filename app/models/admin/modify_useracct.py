from datetime import datetime
from app import db

class IT_Freelancing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_of_specialization = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    skill_acquired = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.String(100), nullable=False)
