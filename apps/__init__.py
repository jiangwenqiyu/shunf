from flask import Flask



def create_app():
    app = Flask(__name__)

    from apps.apis import api
    app.register_blueprint(api, url_prefix = '/sf')
    return app