from flask import Flask
from typing import Optional, Type
from .config import Config

def create_app(config_class: Optional[Type[Config]] = None) -> Flask:
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object(config_class or Config)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

