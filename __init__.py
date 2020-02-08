from flask import Flask

from luizalabs.app.extensions import configuration


def create_app(**config):
    app = Flask(__name__)
    app = configuration.load(app)

    return app
