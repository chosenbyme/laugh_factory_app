from flask import Flask , render_template
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:tyler7820@localhost:5432/laugh-factory-app'
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:Kai280707@localhost:5434/laugh-factory-app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def main():
        return render_template('index.html')

    # meme index route
    @app.route('/memes')
    def memes():
        return 'These are the memes'


    from . import index
    app.register_blueprint(index.bp)
    from . import login
    app.register_blueprint(login.bp)
    from . import loggedin
    app.register_blueprint(loggedin.bp)
    from . import signup
    app.register_blueprint(signup.bp)
    from . import upload
    app.register_blueprint(upload.bp)
    from . import error
    app.register_blueprint(error.bp)
    return app