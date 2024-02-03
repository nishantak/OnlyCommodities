from flask import Blueprint, render_template, url_for, request, flash, redirect, session
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    return render_template('reg.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')		
		print(email)
		
	return render_template("login.html", user=current_user)

@views.route('/home')
@login_required
def home():
	return render_template('home.html',  user=current_user)

@views.route('/profile')
def usr_prof():
	return render_template('profile.html')

@views.route('/settings')
def settings():
	return render_template('settings.html')