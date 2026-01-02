from flask import Blueprint, render_template, request

views_articles = Blueprint('views_articles', __name__)

@views_articles.route('/articles')
def articles():
    lang = request.args.get("lang", "fr")
    return render_template("articles.html", lang=lang, text="Articles Page")