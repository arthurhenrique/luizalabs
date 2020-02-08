from flask import Blueprint
from luizalabs.app.extensions.rest import api
from luizalabs.app.blueprints import customers, products


def init_app(app):
    bp = Blueprint("api", __name__, url_prefix="/api/v1")
    api.init_app(bp)
    app.register_blueprint(bp)

    products.init_app(app)
    customers.init_app(app)
