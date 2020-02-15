from mixer.backend.flask import Mixer

mixer = Mixer(commit=True)


def init_app(app):
    mixer.init_app(app)
