from urllib.parse import urlparse
from flask import Blueprint, render_template, flash, redirect, url_for, request
from pymin import db
from pymin.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from pymin.models import User

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('views.index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('views.login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('views.index')
#         return redirect(next_page)
#     return render_template('login.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
    if request.method == 'POST':
        username = request.form['username']
        pw = request.form['pw']
        remember = request.form['remember']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(pw):
            flash('Invalid username or password')
            return redirect(url_for('views.login'))
        if remember:
            login_user(user, remember=remember)
        else:
            login_user(user, remember=False)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('views.index')
            flash('You have been logged in successfully!')
        return redirect(next_page)
    return render_template('login.html')


@bp.route('/logout')
def logout():
    logout_user()
    flash('Successful logout.')
    return redirect(url_for('views.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('views.login'))
    return render_template('register.html', form=form)
