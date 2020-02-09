import datetime
from app.blueprints import customers
from app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(), nullable=False)
    image = db.Column(db.String(140), nullable=False)
    brand = db.Column(db.String(140), nullable=False)
    title = db.Column(db.String(140), nullable=False)
    review_score = db.Column(db.Numeric(), nullable=False)

    def __init__(self, data):
        self.price = data.get("price")
        self.image = data.get("image")
        self.brand = data.get("brand")
        self.title = data.get("title")
        self.review_score = data.get("review_score")

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_one_product(product_id):
        return Product.query.get(product_id)

    def __repr__(self):
        return "<Product {}>".format(self.title)

