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

from .main import views