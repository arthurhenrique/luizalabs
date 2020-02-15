from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy


class SQLAlchemy(BaseSQLAlchemy):
    def __init__(self, *args, **kwargs):
        if "session_options" not in kwargs:
            kwargs["session_options"] = {}
        kwargs["session_options"]["autocommit"] = True

        super(SQLAlchemy, self).__init__(*args, **kwargs)

    def init_app(self, app):
        super(SQLAlchemy, self).init_app(app)


db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
