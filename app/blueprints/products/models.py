from luizalabs.app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric())
    image = db.Column(db.String(140))
    brand = db.Column(db.String(140))
    title = db.Column(db.String(140))
    review_score = db.Column(db.Numeric())
