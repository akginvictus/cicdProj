from flask import Blueprint

# Main blueprint for the application. Explicitly point to this package's
# templates and static folders so Flask uses the new UI correctly.
# We also expose static files under '/static' for predictable URLs.
bp = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)

# Use a relative import so this works regardless of the package name.
from . import routes
