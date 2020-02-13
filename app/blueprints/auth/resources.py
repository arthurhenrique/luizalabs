from http import HTTPStatus
from datetime import timedelta
from flask import abort, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

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
            db.session.add(user)

        return jsonify({"message": "created"})


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
        try:
            payload = self.api.payload

            user = User.query.filter_by(username=payload.get("username")).first()
            if user.verify_password(password=payload.get("password")):
                access_token = create_access_token(
                    identity=user.id, expires_delta=timedelta(minutes=10)
                )
                refresh_token = create_refresh_token(identity=user.id)
                msg_token = dict(
                    access_token={"Authorization": f"Bearer {access_token}"},
                )

                return jsonify(dict(msg=msg_token), HTTPStatus.OK)
            else:
                return jsonify(
                    {"error": "Invalid credentials, please insert a valid credential"},
                    HTTPStatus.BAD_REQUEST,
                )
        except KeyError:
            return jsonify(dict(error="Payload is not valid"), HTTPStatus.BAD_REQUEST)
        except Exception as e:
            return jsonify(dict(error=e.args[0]), HTTPStatus.BAD_REQUEST)
