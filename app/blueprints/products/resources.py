from flask import abort, jsonify

from app.extensions.api import (
    HTTPStatus,
    Namespace,
    Resource,
    commit_or_abort,
    paginate,
)
from app.extensions.database import db

from .models import Product
from app.blueprints.customers.models import Favorite


api = Namespace("products", description="Products")


@api.route("/")
class ProductResource(Resource):
    def get(self, page_number=1, page_size=20):
        products = Product.get_all_products() or abort(204)

        data = [product.to_dict() for product in products]

        return jsonify(paginate(page_number, page_size, len(data), data))

    def post(self):

        with commit_or_abort(
            db.session, default_error_message="Failed to create a new product"
        ):
            product = Product(self.api.payload)
            db.session.add(product)

        return jsonify({"product": product.to_dict()})


@api.route("/<int:product_id>")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="Product not found.",
)
class ProductByID(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first_or_404()
        return jsonify(product.to_dict())

    def put(self, product_id):
        with commit_or_abort(
            db.session, default_error_message="Failed to update the product"
        ):
            product = Product.query.filter_by(id=product_id).first_or_404()
            payload = self.api.payload

            for k in payload:
                if "id" not in k:
                    setattr(product, k, payload[k])

        return jsonify({"message": "updated"})

    def delete(self, product_id):
        with commit_or_abort(
            db.session, default_error_message="Failed to update the product"
        ):
            product = Product.query.filter_by(id=product_id).first_or_404()
            db.session.delete(product)

            # delete favorites
            favorites = Favorite.query.filter_by(id=product_id)
            db.session.delete(favorites)

        return jsonify({"message": "deleted"})
