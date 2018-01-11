from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def is_empty(text):
    if text == "":
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def display_errors():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pwv = request.form['verify_pass']
        email = request.form['email']

        username_error = ''
        password_error = ''
        pwv_error = ''
        email_error = ''

        if is_empty(username) == True:
            username_error = "This field cannot be left empty."
        else:
            if ' ' in username:
                username_error = "Username cannot contain space characters."
            if len(username) > 20 or len(username) < 3:
                username_error = "Username must be 3-20 characters in length."
            

        if is_empty(password) == True:
            password_error = "This field cannot be left empty."

        else:
            if len(password) > 20 or len(password) < 3:
                password_error = "Password must be 3-20 characters in length."
                password = ''

        if password != pwv:
            pwv_error = 'Values for "Password" and "Verify Password" fields must match.'
        
        
        if is_empty(email) == False: 
            if len(email) > 20 or len(email) < 3:
                email_error = "Email must be 3-20 characters in length."
            else:
                if '@' not in email or '.' not in email:
                    email_error = "Please enter a valid email address."
                if ' ' in email:
                    email_error = "Email cannot contain space characters."


            

        if not username_error and not password_error and not pwv_error and not email_error:
            return render_template('welcome.html', username=username)
        else:
            return render_template('index.html', username_error=username_error, password_error=password_error, pwv_error=pwv_error, email_error=email_error)


app.run()
