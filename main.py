from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret Key'

# Create a Form Class
class CreateUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    middle_name = StringField("Middle Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    contact_number = StringField("Contact Number", validators=[DataRequired()])
    company_email = StringField("Company Email", validators=[Email()])
    personal_email = StringField("Personal Email", validators=[Email()])
    submit = SubmitField("Submit")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    first_name = None
    middle_name = None
    last_name = None
    contact_number = None
    company_email = None
    personal_email = None
    form = CreateUserForm()
    # Validate Form
    if form.validate_on_submit():
        first_name = form.first_name.data
        form.first_name.data = ''
        middle_name = form.middle_name.data
        form.middle_name.data = ''
        last_name = form.last_name.data
        form.last_name.data = ''
        contact_number = form.contact_number.data
        form.contact_number.data = ''
        company_email = form.company_email.data
        form.company_email.data = ''
        personal_email = form.personal_email.data
        form.personal_email.data = ''

    return render_template('create_user.html',
        first_name = first_name,
        middle_name = middle_name,
        last_name = last_name,
        contact_number = contact_number,
        company_email = company_email,
        personal_email = personal_email,
        form = form)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500





if __name__ == "__main__":
    app.run(debug=True)

