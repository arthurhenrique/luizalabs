from flask import Flask

from app.extensions import configuration

extensions = [
    "app.extensions.database",
    "app.extensions.commands",
    "app.extensions.logging",
    "app.extensions.mixer",
    "app.extensions.auth",
    "app.blueprints.api",
]


def create_app(**config):
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "super-secret"

    configuration.init_app(app, **config)
    configuration.load(extensions, app)

    return app
