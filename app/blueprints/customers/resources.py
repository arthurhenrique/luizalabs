from flask import abort, jsonify
from flask_jwt_extended import jwt_required

from app.extensions.api import (
    HTTPStatus,
    Namespace,
    Resource,
    commit_or_abort,
    paginate,
    update_dict,
)
from app.extensions.database import db

from .models import Customer, Favorite

api = Namespace("customers", description="Customers")


@api.route("/")
class CustomerResource(Resource):
    @jwt_required
    def get(self):
        customers = Customer.get_all_customers() or abort(204)
        return jsonify({"customers": [customer.to_dict() for customer in customers]})

    @jwt_required
    def post(self):
        with commit_or_abort(
            db.session, default_error_message="Failed to create a new customer"
        ):
            customer = Customer(self.api.payload)
            db.session.add(customer)

        return jsonify({"customer": customer.to_dict()})


@api.route("/<int:customer_id>")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="Customer not found.",
)
class CustomerByID(Resource):
    @jwt_required
    def get(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first_or_404()
        return jsonify(customer.to_dict())

    @jwt_required
    def put(self, customer_id):
        with commit_or_abort(
            db.session, default_error_message="Failed to update the customer"
        ):
            customer = Customer.query.filter_by(id=customer_id).first_or_404()
            payload = self.api.payload

            customer, payload = update_dict(customer, payload)

        return jsonify({"message": "updated"})

    @jwt_required
    def delete(self, customer_id):
        with commit_or_abort(
            db.session, default_error_message="Failed to update the customer"
        ):
            customer = Customer.query.filter_by(id=customer_id).first_or_404()
            db.session.delete(customer)

            # delete favorites
            favorites = Favorite.query.filter_by(id=customer_id)
            db.session.delete(favorites)

        return jsonify({"message": "deleted"})


@api.route("/<int:customer_id>/favorite-product/")
class FavoriteResource(Resource):
    @jwt_required
    def get(self, customer_id):
        favorites = Favorite.query.filter_by(customer_id=customer_id).all()
        return jsonify({"favorites": [favorite.to_dict() for favorite in favorites]})

    @jwt_required
    def post(self):

        with commit_or_abort(
            db.session, default_error_message="Failed to create a new favorite"
        ):
            favorite = Favorite(self.api.payload)
            db.session.add(favorite)

        return jsonify({"favorite": favorite.to_dict()})


@api.route("/<int:customer_id>/favorite-product/<int:product_id>")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="Favorite not found.",
)
class FavoriteByID(Resource):
    @jwt_required
    def get(self, customer_id, product_id):
        favorite = Favorite.query.filter_by(
            product_id=product_id, customer_id=customer_id
        ).first_or_404()
        return jsonify(favorite.to_dict())

    @jwt_required
    def delete(self, product_id, customer_id):
        with commit_or_abort(
            db.session, default_error_message="Failed to delete the favorite"
        ):
            favorite = Favorite.query.filter_by(
                product_id=product_id, customer_id=customer_id
            ).first_or_404()
            db.session.delete(favorite)

        return jsonify({"message": "deleted"})
