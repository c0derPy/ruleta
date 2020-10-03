from flask import jsonify, url_for, request
from app.api import bp
from app import db
from app.models import Jugador


@bp.route('/jugadores', methods=['GET'])
def jugadores():
	jugadores = Jugador.query.order_by(Jugador.id.desc()).all()
	return jsonify([jugador.to_dict()
		            for jugador in jugadores])

@bp.route('/jugador/registro', methods=['POST'])
def jugador_registro():
	data = request.get_json() or {}
	if('nombre' not in data and 'apellido' not in data):
		return jsonify('Error')
	jugador = Jugador()
	jugador.nombre = data['nombre']
	jugador.apellido = data['apellido']
	db.session.add(jugador)
	db.session.commit()

	respuesta = jsonify(jugador.to_dict())
	respuesta.status_code = 201
	respuesta.headers['Location'] = url_for('api.jugador_detalle', id=jugador.id)
	return(respuesta)

@bp.route('/jugador/editar/<id>', methods=['PUT'])
def jugador_editar(id):
	jugador = Jugador.query.get_or_404(id)
	data = request.get_json() or {}
	
	jugador.nombre = data['nombre']
	jugador.apellido = data['apellido']
	jugador.activo = data['activo']
	jugador.dinero = data['dinero']
	db.session.add(jugador)
	db.session.commit()
	
	return jsonify(jugador.to_dict())

@bp.route('/jugador/<id>', methods=['GET'])
def jugador_detalle(id):
	return jsonify(Jugador.query.get_or_404(id).to_dict())