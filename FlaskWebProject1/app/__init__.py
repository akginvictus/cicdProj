from flask import Flask

from .config import Config
from .main import bp as main_bp


def create_app(config_class: type[Config] = Config) -> Flask:
    """Application factory used by runserver and gunicorn."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register the main blueprint so templates/static under app/main are used.
    app.register_blueprint(main_bp)

    return app
