from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
fa = FontAwesome(app)
login_manager.init_app(app)

# Registering the blueprint - main
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Registering the blueprint - auth
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')