from flask import abort, jsonify

from app.extensions.api import (
    HTTPStatus,
    Namespace,
    Resource,
    commit_or_abort,
    paginate,
    update_dict,
)
from app.extensions.database import db

from .models import User

api = Namespace("auth", description="Authentication")


@api.route("/")
class UserResource(Resource):
    def post(self):
        with commit_or_abort(
            db.session, default_error_message="Failed to create a new user"
        ):
            user = User(self.api.payload)
            import ipdb

            ipdb.set_trace()
            db.session.add(user)

        return jsonify({"created": user.to_dict()})


@api.route("/<int:user_id>")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="User not found.",
)
class UserByID(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first_or_404()
        return jsonify(user.to_dict())

    def put(self, user_id):
        with commit_or_abort(
            db.session, default_error_message="Failed to update the user"
        ):
            user = User.query.filter_by(id=user_id).first_or_404()
            payload = self.api.payload

            user, payload = update_dict(user, payload)

        return jsonify({"message": "updated"})

    def delete(self, user_id):
        with commit_or_abort(
            db.session, default_error_message="Failed to update the user"
        ):
            user = User.query.filter_by(id=user_id).first_or_404()
            db.session.delete(user)

        return jsonify({"message": "deleted"})


@api.route("/login")
class UserLogin(Resource):
    def post(self):
        with commit_or_abort(
            db.session, default_error_message="Failed to create a new user"
        ):
            user = User(self.api.payload)
            db.session.add(user)

        return jsonify({"created": user.to_dict()})
