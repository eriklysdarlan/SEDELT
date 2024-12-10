from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

admin = Blueprint('admin', __name__)

@login_required
@admin.route('/admin')
def administrativControl():
    return render_template('admin/admin.html')