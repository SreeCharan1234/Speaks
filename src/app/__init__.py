from flask import Flask

from jinja2.utils import escape
def create_app():
    app = Flask(__name__)
    with app.app_context():
        from . import views  # noqa: E402,F401
        from . import apis  # noqa: E402,F401
    return app
