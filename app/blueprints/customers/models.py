from luizalabs.app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class CustomerProduct(db.Model, SerializerMixin):

    __tablename__ = "customer_product"

    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), primary_key=True)
    customer = db.relationship(
        "Customer", backref=db.backref("customers", cascade="delete, delete-orphan")
    )
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)
    product = db.relationship(
        "Product", backref=db.backref("products", cascade="delete, delete-orphan")
    )

    __table_args__ = (db.UniqueConstraint(customer_id, product_id),)


class Customer(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    email = db.Column(db.String(120), unique=True, nullable=False)

