from flask import jsonify
from app.api import bp
from app.models import Jugador, Rueda, Apuesta

@bp.route('/ruleta', methods=['GET'])
def ruleta():
    pass