from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__)

@login_required
@admin.route('')
def administrativControl():
    if not current_user.is_admin:
        abort(403)
    return render_template('admin/admin.html')