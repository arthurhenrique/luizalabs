from app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Customer(db.Model, SerializerMixin):
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, data):
        self.name = data.get("name")
        self.email = data.get("email")

    @staticmethod
    def get_all_customers():
        return Customer.query.all()

    @staticmethod
    def get_one_customer(customer_id):
        return Customer.query.get(customer_id)

    def __repr__(self):
        return "<Customer {}>".format(self.name)


class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorite"

    customer_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, data):
        self.customer_id = data.get("customer_id")
        self.product_id = data.get("product_id")

    @staticmethod
    def get_all_favorites():
        return Favorite.query.all()

    def __repr__(self):
        return "<Favorite {}>".format(self.customer_id)
