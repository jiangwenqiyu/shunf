from flask import Blueprint

api = Blueprint('getInfo', __name__)

from apps.apis import getInfo
