from luizalabs.app.extensions import database
from luizalabs.app.extensions import logging
from luizalabs.app.extensions import auth
from luizalabs.app.blueprints import api


def load(app):
    init_app(app)


def init_app(app):
    database.init_app(app)
    logging.init_app(app)
    auth.init_app(app)
    api.init_app(app)

