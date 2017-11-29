import bcrypt
from flask import Blueprint, render_template

from common.utilities import AuthUtils
from user.forms import RegisterForm, LoginForm
from user.models import User
from wtforms.validators import ValidationError

user_app = Blueprint('user_app', __name__)

@user_app.route('/login', methods=('GET','POST'))
def login():
    invalid_msg = "Invalid Username or Password"
    success_msg = "Successfully logged in."
    
    form = LoginForm()
    if form.validate_on_submit():
        # Authentication check happens in form validators; if validation succeeded, log user in
        return success_msg
    return render_template('user/login.html', form=form)

@user_app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=AuthUtils.hash_password(plaintext_pw=form.password.data),
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        user.save()
        return "User Successfully Registered (TODO make this page)"
    return render_template('user/register.html', form=form)