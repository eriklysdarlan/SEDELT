from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

bp_home = Blueprint('home',__name__)

@bp_home.route('/', methods=['GET', 'POST'])
def home():

    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.admin_panel'))

    return render_template('home.html')