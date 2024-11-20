from flask import Blueprint, render_template, request, redirect, url_for
from app.models.database_SEDELT import db, Admin

bp_home = Blueprint('home',__name__)

@bp_home.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')