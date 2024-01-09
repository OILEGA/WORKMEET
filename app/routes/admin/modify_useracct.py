from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from app.models.admin import IT_Freelancing


@app.route('/modify_useracct', methods=['GET', 'POST'])
@login_required
def modify_useracct():
    if request.method == 'POST':
        area_of_specialization = request.form.get('area_of_specialization')
        birth_date = datetime.strptime(request.form.get('birth_date'), '%Y-%m-%d')
        skill_acquired = request.form.get('skill_acquired')
        experience = request.form.get('experience')
        total_users = int(request.form.get('total_users'))

        #checking if an IT Freelancing already exist
        existing_it_freelancing = IT_Freelancing.query.first()

        if existing_it_freelancing:
            #override existing details with new details
            existing_it_freelancing.area_of_specialization = area_of_specialization
            existing_it_freelancing.birth_date = birth_date
            existing_it_freelancing.skill_acquired = skill_acquired
            existing_it_freelancing.experience = experience
            existing_it_freelancing.total_users = total_users

        else:
            #create a new IT Freelancing to the database
            new_it_freelancing = IT_Freelancing(
                area_of_specialization=area_of_specialization,
                birth_date=birth_date,
                skill_acquired=skill_acquired,
                experience=experience,
                total_users=total_users,

            )
            db.session.add(new_it_freelancing)
            db.session.commit()
            flash('New IT Freelancing Added Successfully.', 'success')
            return redirect(url_for('dashboard'))
    return render_template('admin/modify_useracct.html')