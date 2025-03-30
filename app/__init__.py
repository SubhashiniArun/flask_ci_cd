from flask import Flask

from .config import get_config
from .models import db
from .routes.user_routes import api_blueprint

def create_app(config_name="development"):

    # Setting up the Flask app
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(get_config(config_name))

    # Initialize extensions
    db.init_app(app)

    # Register the blueprints (routes)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app


