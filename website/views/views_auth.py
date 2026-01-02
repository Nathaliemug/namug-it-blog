from flask import Blueprint, render_template,request
views_auth = Blueprint('views_auth', __name__)

@views_auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@views_auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")  
@views_auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template("logout.html")
@views_auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        if len(email) < 4:
            print("Email must be greater than 3 characters.")
        elif len(first_name) < 2:
            print("First name must be greater than 1 character.")   
        elif len(last_name) < 2:
            print("Last name must be greater than 1 character.")
        elif password != password1:
            print("Passwords don't match.")
        elif len(password) < 7:
            print("Password must be at least 7 characters.")
    
    return render_template("sign-up.html")