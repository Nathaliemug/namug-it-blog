from flask import Blueprint
views_auth = Blueprint('views_auth', __name__)

@views_auth.route('/login')
def login():
    return "Welcome to the Login Page!"

@views_auth.route('/register')
def register():
    return "Welcome to the Registration Page!"  
@views_auth.route('/logout')
def logout():
    return "You have been logged out!"
@views_auth.route('/Sign-up')
def profile():
    return "This is your sign-up page."