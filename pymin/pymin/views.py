from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import logout_user
from pymin.services import Services

bp = Blueprint('views', __name__)
services = Services()


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    services.check_if_authenticated()
    return services.handle_login()


@bp.route('/logout')
def logout():
    logout_user()
    flash('Successful logout.')
    return redirect(url_for('views.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    services.check_if_authenticated()
    return services.validate_form()
