from importlib import import_module
from dynaconf import FlaskDynaconf


def load(extensions, app):
    for extension in extensions:
        ext = import_module(extension)
        getattr(ext, "init_app")(app)


def init_app(app, **config):
    FlaskDynaconf(app, **config)

