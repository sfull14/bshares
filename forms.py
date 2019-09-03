from flask_wtf import FlaskForm # we'll be writing python classes that are automatically turned into python forms
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	# going to write some imported classes from wtForms
	username = StringField('Username', 
							validators=[DataRequired(), Length(min=2, max=20)]) # 'Username' will be our label in html
	email = StringField('Email', 
						validators=[DataRequired(), Email(), ])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	# going to write some imported classes from wtForms
	email = StringField('Email', 
						validators=[DataRequired(), Email(), ])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')	