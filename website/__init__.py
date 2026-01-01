from flask import Flask

def create_app():
    # Create and configure the Flask application
    app = Flask(__name__)
    # Set a secret key for session management
    app.config['SECRET_KEY'] = 'qsdfdsgfdsghdfhgfjgjhjgfjhnbngng' # Randomly generated string to enhance security and protect against certain attacks.Mustnot be shared publicly.
    
    from .views.views import views
    from .views.views_auth import views_auth
    from .views.views_articles import views_articles
    
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(views_auth, url_prefix='/auth')
    app.register_blueprint(views_articles, url_prefix='/articles')
    return app