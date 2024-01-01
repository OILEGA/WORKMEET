from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.models.user import Registration
from app.models.admin import IT_Freelancing


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        #get the form data
        form_data = request.form

        #creating a registration object to add to the database
        registration = Registration(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            contact_num=form_data['contact_num'],
            country_of_residence=form_data['country_of_residence'],
            date_of_birth=form_data['birth_date'],
            number_of_users=form_data['number_of_users'],
            freelancer_job_category=form_data['job_type'],
            area_of_specialization=form_data['area_of_specialization'],
            programming_skills_acquired=form_data['skill_acquired'],
            years_of_experience=form_data['experience']
        )
        db.session.add(registration)
        db.session.commit()

        flash('You have successfully registered as an IT Freelancer', 'success')

        #redirect user to the page of displaying the user inputs
        return redirect(url_for('user_inputs'))
    return render_template('root/register.html')

@app.route('/user_inputs')
def user_inputs():
    #Display all user inputs from the database
    registrations = Registration.query.all()

    return render_template('root/user_inputs.html', registrations=registrations)
