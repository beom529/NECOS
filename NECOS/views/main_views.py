from flask import Blueprint

blueprint = Blueprint('main', __name__, url_prefix='/')

@blueprint.route('/')
def fistBlueprint():
    return 'First Blueprint'