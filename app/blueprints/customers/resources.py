from flask import abort, jsonify
from luizalabs.app.extensions.rest import Namespace, Resource

from .models import Customer

api = Namespace("customers", description="Customers")


@api.route("/")
class CustomerResource(Resource):
    def get(self):
        import ipdb

        ipdb.set_trace()
        customers = Customer.query.all() or abort(204)
        return jsonify({"customers": [customer.to_dict() for customer in customers]})


@api.route("/<int:customer_id>")
class CustomerByID(Resource):
    def get(self, customer_id):

        customer = Customer.query.filter_by(id=customer_id).first() or abort(404)
        return jsonify(customer.to_dict())
