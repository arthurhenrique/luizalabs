from luizalabs.app.extensions.logging import logging
from flask_restplus import Api, Namespace, Resource
from flask_restplus._http import HTTPStatus


api = Api(
    version="1.0",
    title="Desafio Luiza Labs",
    description=(
        "Desafio Luiza Labs - Feito por Arthur Henrique (arthurhenrique)\n"
        '"Furioso Oceano, vem fluir dentro de mim."\n'
    ),
)


@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred."
    logger.exception(message)
    return {"message": message}, 500
