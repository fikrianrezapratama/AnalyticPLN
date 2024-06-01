from flask import Flask
from config.settings import setup_logging

def create_app():
    app = Flask(__name__)
    
    # logging
    setup_logging()

    # Load configuration
    app.config.from_object('config.settings.Config')

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
