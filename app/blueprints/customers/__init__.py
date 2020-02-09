from app.extensions.api import api


def init_app(app, **kwargs):
    from . import resources

    api.add_namespace(resources.api)
