from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.admin import IT_Freelancing


@app.route('/review_job', methods=['GET', 'POST'])
@login_required
def review_job():
    if request.method == 'POST':
        area_of_specialization = request.form.get('area_of_specialization')
        birth_date = request.form.get('birth_date')
        skill_acquired = request.form.get('skill_acquired')
        experience = request.form.get('experience')
        total_users = int(request.form.get('total_users'))

        #using the id to know which freelancing to edit
        it_freelancing_id = request.args.get('it_freelancing_id')

        existing_it_freelancing = IT_Freelancing.query.get(it_freelancing_id)

        if existing_it_freelancing:
            #update existing freelancing details
            existing_it_freelancing.area_of_specialization = area_of_specialization
            existing_it_freelancing.birth_date = birth_date
            existing_it_freelancing.skill_acquired = skill_acquired
            existing_it_freelancing.experience = experience
            existing_it_freelancing.total_users = total_users

            db.session.commit()
            flash('IT Freelancing details edited and reviewed successfully', 'success')
            return redirect(url_for('dashboard'))

    it_freelancing_id = request.args.get('it_freelancing_id')

    existing_it_freelancing = IT_Freelancing.query.get(it_freelancing_id)

    if existing_it_freelancing:
        return render_template('admin/review_job.html', existing_it_freelancing=existing_it_freelancing)
    else:
        flash('IT Freelancing Not Found', 'danger')
        return redirect(url_for('dashboard'))