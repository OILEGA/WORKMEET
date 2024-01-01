from app import app
from flask import render_template
from flask_login import login_required
from app.models.admin import IT_Freelancing
from app.models.user import Registration

@app.route('/dashboard')
@login_required
def dashboard():
    #Retrieve existing IT Freelancing from the database
    existing_it_freelancing = IT_Freelancing.query.first()
    job_postings = 0 

    if existing_it_freelancing is not None:
        total_users = existing_it_freelancing.total_users
        #count the number of registered users
        it_freelancing = Registration.query.count()

        # Check if both total_users and job_postings have valid values
        if total_users is not None and isinstance(total_users, int) and isinstance(it_freelancing, int):
           
            total_users = job_postings + it_freelancing


        #Retrieve all user registrations
        registrations = Registration.query.all()

        return render_template(
            'admin/dashboard.html',
            total_users=total_users,
            job_postings=job_postings,
            it_freelancing=it_freelancing,
            existing_it_freelancing=existing_it_freelancing,
            registrations=registrations
        )
    return render_template('admin/dashboard.html')
    