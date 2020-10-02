from flask import jsonify
from app.api import bp

@bp.route('/', methods=['GET'])
def inicio():
    return 'Hello API'