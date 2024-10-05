from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = '2ijb4r3khu5v323lh5v32lhv'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app