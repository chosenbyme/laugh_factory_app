from flask import Flask
import os
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate 
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()
    my_id = os.getenv("SQL")
    app.config['SECRET_KEY'] = "helloworld"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = my_id
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    # with app.app_context():
    #     db.create_all()

    return app


