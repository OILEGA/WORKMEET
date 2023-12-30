from app import app
from flask import render_template
from flask_login import login_required


@app.route('/modify_useracct')
@login_required
def modify_useracct():
    render_template('admin/modify_useracct.html')