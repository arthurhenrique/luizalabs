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


def paginate(
    page_number=1, page_size=20, total_count=0, data=None, start_page_as_1=True
):
    """Return payload that contains metainformations about
    pagination and listing data.
    page_number starts with 0 (array like),
    if start_page_as_1 defined as True, start with 1.
    """
    if start_page_as_1 and page_number <= 0:
        raise Exception(
            "Page number must starts > 0.\nCause: start_page_as_1=True and page_number defined as <= 0"
        )
    elif start_page_as_1 and page_number > 0:
        page_number -= 1

    # The remaining on the last page
    remaining = total_count % page_size
    total_pages = (
        total_count // page_size + 1 if remaining else total_count // page_size
    )

    # Prepares to iterate only the data requested on page_number
    begin = page_number * page_size
    end = begin

    if page_number == total_pages and remaining:
        end += remaining
    else:
        end += page_size

    # TODO
    next_page = ""
    previous_page = ""

    result = {
        "total_pages": total_pages,
        "total_count": total_count,
        "page_number": page_number,
        "items": data[begin:end],
        "next": next_page,
        "previous": previous_page,
    }

    return result


def update_dict(query_result, payload):

    for key in payload:
        if "id" not in key:
            setattr(query_result, key, payload[key])

    return query_result, payload
