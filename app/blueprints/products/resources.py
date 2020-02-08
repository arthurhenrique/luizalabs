from luizalabs.app.blueprints import customers
from luizalabs.app.extensions.database import db
from luizalabs.app.extensions.logging import logging
from luizalabs.app.extensions.rest import HTTPStatus, Namespace, Resource

from .models import Product

api = Namespace("products", description="Products")


@api.route("/")
class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify({"products": [product.to_dict() for product in products]})


@api.route("/<int:product_id>")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="Product not found.",
)
# @api.resolve_object_by_model(Product, "product")
class ProductByID(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())
