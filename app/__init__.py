from flask import Flask

from app.extensions import configuration

extensions = [
    "app.extensions.database",
    "app.extensions.commands",
    "app.extensions.logging",
    "app.extensions.mixer",
    "app.blueprints.api",
]


def create_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    configuration.load(extensions, app)

    return app
