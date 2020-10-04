from flask import jsonify, url_for, request
from app.api import bp
from app import db
from app.models import Jugador
from app.api.errores import bad_request
import json

@bp.route('/jugadores', methods=['GET'])
def jugadores():
	""" Retorna JSON con todos los jugadores activos """
	jugadores = Jugador.query.order_by(Jugador.id.desc()).filter_by(activo=True)
	return jsonify([jugador.to_dict()
		            for jugador in jugadores])

@bp.route('/jugador/registro', methods=['POST'])
def jugador_registro():
	""" Recibe la informacion de registro de Jugador """
	data = json.loads(request.get_data())
	if(data['nombre'] == '' or data['apellido'] == ''):
		return bad_request('Registrar nombre y apellido')

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
	""" Recibe la informacion a modificar del jugador """
	jugador = Jugador.query.get_or_404(id)
	data = json.loads(request.get_data())
	if(data['nombre'] == '' or data['apellido'] == ''):
		return bad_request('Registrar nombre y apellido')
	if(data['activo'] == '1'):
		jugador.activo = True
	else:
		jugador.activo = False
	
	jugador.nombre = data['nombre']
	jugador.apellido = data['apellido']
	jugador.dinero = data['dinero']
	db.session.add(jugador)
	db.session.commit()

	return jsonify(jugador.to_dict())

@bp.route('/jugador/<id>', methods=['GET'])
def jugador_detalle(id):
	""" Retorna el detalle de un jugador dado """
	return jsonify(Jugador.query.get_or_404(id).to_dict())