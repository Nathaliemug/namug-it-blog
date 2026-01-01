# Blueprint is a module within the Flask framework that allows developers to organize their application into smaller, reusable components. Each blueprint can define its own routes, views, templates, and static files, making it easier to manage large applications by breaking them down into modular sections.
from flask import Blueprint, render_template
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")