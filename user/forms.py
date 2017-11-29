from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from common.utilities import AuthUtils

from user.models import User


class LoginForm(Form):
    username = StringField('Username', [validators.Required(), validators.length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required()]) 
    
    @staticmethod
    def validate_password(form, field):
        """
        Check the username to see if a matching user exists, then if the PW is correct.
        Raises a purposefully vague message about either the username or password not matching.
        """
        valid = False
        user = User.objects.filter(username=form.username.data).first()
        if user:
            valid = AuthUtils.check_password(plaintext_pw=field.data, hashed_pw=user.password)
        if not valid:
            raise ValidationError("Invalid Username or Password")


class RegisterForm(Form):
    """
    Fields to be rendered on the Registration form at /register
    """
    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    username = StringField('Username', [validators.Required(), validators.length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.Required(), 
        validators.EqualTo('confirm', message="Passwords must match!"),
        validators.length(min=4, max=80)
    ])
    confirm = PasswordField('Re-enter Password')
    
    @staticmethod
    def validate_username(form, field):
        """
        Validate that the username does not already exist.
        """
        if User.objects.filter(username=field.data).first():
            raise ValidationError("Username already exists.")
    
    @staticmethod
    def validate_email(form, field):
        """
        Validate that the email does not already exist.
        """
        if User.objects.filter(email=field.data).first():
            raise ValidationError("Email is already in use.")
    