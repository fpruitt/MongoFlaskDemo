from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    """
    Factory to create and configure this flask application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    
    # initialize the mongo engine with the app context.
    db.init_app(app)
    
    from user.views import user_app
    app.register_blueprint(user_app)
    
    return app