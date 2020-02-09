from flask import Blueprint
from app.extensions.api import api
from app.blueprints import customers, products


def init_app(app):

    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)

    app.register_blueprint(blueprint)

    products.init_app(app)
    customers.init_app(app)
