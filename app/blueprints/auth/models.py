from app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, SerializerMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, data):
        self.username = data.get("username")
        self.password = self.hash_password(data.get("password"))

    def verify_password(self, password) -> bool:
        return check_password_hash(pwhash=self.password, password=password)

    def hash_password(self, paverify_token_claimsssword) -> str:
        return generate_password_hash(password)

    def __repr__(self):
        return "<User {}>".format(self.username)

