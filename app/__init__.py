from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import config_options, DevConfig
from flask_mail import Mail
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
simple = SimpleMDE()



def create_app(config_name):
    
    app = Flask(_name_)
    
  
    #app.config.from_object(config_options[config_name])
    
  
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
  
    app.config.from_object(DevConfig)
    
    

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    from .auth import auth as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix = '/auth')
    
    
    
    return app