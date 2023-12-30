from app import app
from flask import render_template
from flask_login import login_required


@app.route('/review_job')
@login_required
def review_job():
    render_template('admin/review_job.html')