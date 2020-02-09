from contextlib import contextmanager

from flask_restplus import Api, Namespace, Resource
from flask_restplus._http import HTTPStatus
from flask_restplus.errors import abort as restplus_abort
import sqlalchemy

from app.extensions.logging import logging

api = Api(
    version="1.0",
    title="Desafio Luiza Labs",
    description=(
        "Desafio Luiza Labs - Feito por Arthur Henrique (arthurhenrique)\n\n"
        '\t"Furioso Oceano, vem fluir dentro de mim."\n'
    ),
)


API_DEFAULT_HTTP_CODE_MESSAGES = {
    HTTPStatus.UNAUTHORIZED.value: (
        "The server could not verify that you are authorized to access the "
        "URL requested. You either supplied the wrong credentials (e.g. a bad "
        "password), or your browser doesn't understand how to supply the "
        "credentials required."
    ),
    HTTPStatus.FORBIDDEN.value: (
        "You don't have the permission to access the requested resource."
    ),
    HTTPStatus.UNPROCESSABLE_ENTITY.value: (
        "The request was well-formed but was unable to be followed due to semantic errors."
    ),
}


@contextmanager
def commit_or_abort(session, default_error_message="The operation failed to complete"):
    """
    Context manager to simplify a workflow in resources

    Args:
        session: db.session instance
        default_error_message: Custom error message
    """
    try:
        with session.begin():
            yield
    except ValueError as exception:
        logging.info("Database transaction was rolled back due to: %r", exception)
        abort(code=HTTPStatus.CONFLICT, message=str(exception))
    except sqlalchemy.exc.IntegrityError as exception:
        logging.info("Database transaction was rolled back due to: %r", exception)
        abort(code=HTTPStatus.CONFLICT, message=default_error_message)


def abort(code, message=None, **kwargs):
    """
    Custom abort function used to provide extra information in the error
    response, namely, ``status`` and ``message`` info.
    """
    if message is None:
        if code in API_DEFAULT_HTTP_CODE_MESSAGES:  # pylint: disable=consider-using-get
            message = API_DEFAULT_HTTP_CODE_MESSAGES[code]
        else:
            message = HTTPStatus(
                code
            ).description  # pylint: disable=no-value-for-parameter
    restplus_abort(code=code, status=code, message=message, **kwargs)


@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred."
    logging.exception(message)
    return {"message": message}, 500
