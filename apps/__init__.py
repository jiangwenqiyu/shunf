from flask import Flask
from Config import Produce



def create_app():
    app = Flask(__name__)
    app.config.from_object(Produce)

    from apps.apis import api
    app.register_blueprint(api, url_prefix = '/sf')
    return app