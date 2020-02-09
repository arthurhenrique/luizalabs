import click

from app.blueprints.customers.models import Customer, Favorite
from app.blueprints.products.models import Product
from app.extensions.database import db
from app.extensions.mixer import mixer
from app.extensions.api import commit_or_abort


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""

    # TODO automated population using mixer
    with commit_or_abort(db.session):
        customer = Customer(data=dict(name="Turing", email="turing@gnirut.com"))
        db.session.add(customer)

        product = Product(
            data=dict(
                price=10.0,
                image="google/fotos/espelho",
                brand="ceviu",
                title="espelho",
                review_score=8000.01,
            )
        )
        db.session.add(product)
        product = Product(
            data=dict(
                price=19.99,
                image="google/fotos/xicaras",
                brand="xixisdavovo",
                title="Xicaras",
                review_score=800.01,
            )
        )
        db.session.add(product)

        favorite = Favorite(data=dict(customer_id=1, product_id=1))
        db.session.add(favorite)

        favorite = Favorite(data=dict(customer_id=1, product_id=2))
        db.session.add(favorite)

    return Customer.query.all()


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

