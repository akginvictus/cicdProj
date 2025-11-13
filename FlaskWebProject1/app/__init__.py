"""
Application factory for the Flask project.
"""

from flask import Flask

from .config import Config
from .main import bp as main_bp


def create_app(config_class: type[Config] | None = None) -> Flask:
    """Create and configure the Flask application instance."""
    app = Flask(__name__, instance_relative_config=False)

    config_obj = config_class or Config()
    app.config.from_object(config_obj)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> None:
    """Register application blueprints."""
    app.register_blueprint(main_bp)

