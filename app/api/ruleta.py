from flask import jsonify
from app.api import bp
from app import db
from app.models import Jugador, Rueda, Apuesta

@bp.route('/ruleta', methods=['GET'])
def ruleta():
    """ Genera la simulacion de la ruleta con todas las 
    reglas planteadas y retorna los resultados de las apuestas """
    jugadores = Jugador.query.filter_by(activo=True)
    rueda = Rueda()
    color_giro = rueda.girar()
    db.session.add(rueda)
    db.session.commit()
   
    datos_ruleta = []
    total_apuestas = 0
    total_pagado = 0
    for jugador in jugadores:
    	datos_jugador = {'nombre':jugador.nombre, 'apellido':jugador.apellido, 
    					 'color_apuesta':'', 'monto_apuesta':0,
    					 'monto_ganado':0, 'resultado_ruleta':''}
    	monto_apuesta = jugador.monto_apuesta()
    	if(monto_apuesta == 0):
    		datos_jugador['resultado_ruleta'] = 'No tiene saldo disponible'
    		datos_ruleta.append(datos_jugador)
    		continue
    	color_apuesta = jugador.seleccionar_color()
    	dinero_ganado = 0
    	if(color_giro == color_apuesta and (color_giro == 'NEGRO' or color_giro == 'ROJO')):
    		dinero_ganado = monto_apuesta * 2
    		jugador.dinero = jugador.dinero + dinero_ganado
    	elif(color_giro == color_apuesta and color_giro == 'VERDE'):
    		dinero_ganado = monto_apuesta * 10
    		jugador.dinero = jugador.dinero + monto_ganado

    	datos_jugador['monto_ganado'] = dinero_ganado
    	datos_jugador['color_apuesta'] = color_apuesta
    	datos_jugador['monto_apuesta'] = monto_apuesta
    	datos_jugador['resultado_ruleta'] = color_giro
    	datos_ruleta.append(datos_jugador)

    	apuesta = Apuesta()
    	apuesta.dinero = monto_apuesta
    	apuesta.color = color_apuesta
    	apuesta.pago = dinero_ganado
    	apuesta.jugador = jugador.id
    	apuesta.rueda = rueda.id
    	db.session.add(apuesta)
    	db.session.commit()

    	total_apuestas = total_apuestas + 1
    	total_pagado = float(total_pagado) + float(dinero_ganado)

    rueda.total_apuestas = total_apuestas
    rueda.total_pagado = total_pagado    
    db.session.commit()

    return jsonify(datos_ruleta)
