from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "SecretKey"


    from .views import views
    from .auth import auth
    from .whatsbot import whatsbot

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(whatsbot, url_prefix='/')

    return app
