from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from pymin import db
from pymin.forms import RegistrationForm
from flask_login import current_user, login_user
from pymin.models import User


class Services:
    @staticmethod
    def check_if_authenticated():
        if current_user.is_authenticated:
            return redirect(url_for('views.index'))

    @staticmethod
    def handle_login():
        if request.method == 'POST':
            username = request.form['username']
            pw = request.form['pw']
            try:
                remember = request.form['remember']
            except:
                remember = False
            user = User.query.filter_by(username=username).first()
            if user is None or not user.check_password(pw):
                flash('Invalid username or password')
                return redirect(url_for('views.login'))
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('views.index')
                flash('You have been logged in successfully!')
            return redirect(next_page)
        return render_template('login.html')

    @staticmethod
    def validate_form():
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('views.login'))
        else:
            return render_template('register.html', form=form)
