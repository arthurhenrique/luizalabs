from flask import Flask

from luizalabs.app.extensions import configuration


def create_app(**config):
    app = Flask(__name__)
    configuration.load(app)

    return app
