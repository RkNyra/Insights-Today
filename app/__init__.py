from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
fa = FontAwesome(app)

# Registering the blueprint - main
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Registering the blueprint - auth
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')