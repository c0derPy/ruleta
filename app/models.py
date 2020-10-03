from app import db
from datetime import datetime
from enum import Enum
import random

class Color(Enum):
    VERDE = 1 
    ROJO =  2
    NEGRO = 3

class Jugador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    apellido = db.Column(db.String(200))
    dinero = db.Column(db.Float(precision=10, asdecimal=True, decimal_return_scale=2), default=15000.00) 
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    apuesta = db.relationship('Apuesta', backref='persona', lazy='dynamic')

    def __repr__(self):
        return '<Jugador %r>'%self.nombre

    def to_dict(self):
        data = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dinero': float(self.dinero),
            'activo': self.activo,
            'fecha_creacion': self.fecha_creacion
        }
        return data

    def seleccionar_color(self):
        resultado = random.randrange(1, 101, 1)
        color_seleccionado = ''
        if(resultado <= 49.5):
            color_seleccionado = 'ROJO'
        elif(resultado > 49.5 and resultado <= 99):
            color_seleccionado = 'NEGRO'
        else:
            color_seleccionado = 'VERDE'
        return color_seleccionado
    
    def monto_apuesta(self):
        porcentaje = random.randrange(11, 20, 1)
        dinero_apuesta = 0
        if(self.dinero > 0 and self.dinero <= 1000):
            dinero_apuesta = self.dinero
            self.dinero = self.dinero - dinero_apuesta
        elif (self.dinero > 1000):
            dinero_apuesta = float(self.dinero) * (porcentaje / 100)
            self.dinero = float(self.dinero) - dinero_apuesta
        return dinero_apuesta


class Rueda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum(Color))
    total_apuestas = db.Column(db.Integer)
    total_pagado = db.Column(db.Float(precision=10, asdecimal=True, decimal_return_scale=2))
    resultado_giro = db.Column(db.String(50))
    apuesta = db.relationship('Apuesta', backref='sorteo', lazy='dynamic')
    fecha_creacion = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Rueda %r>' % self.resultado_giro

    def girar(self):
        resultado = random.randrange(1, 101, 1)
        color_sorteo = ''
        if(resultado <= 49.5):
            color_sorteo = 'ROJO'
        elif(resultado > 49.5 and resultado <= 99):
            color_sorteo = 'NEGRO'
        else:
            color_sorteo = 'VERDE'
        self.resultado_giro = color_sorteo
        return color_sorteo


class Apuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dinero = db.Column(db.Numeric(10,2))
    color = db.Column(db.String(20))
    pago = db.Column(db.Float(precision=10, asdecimal=True, decimal_return_scale=2))
    jugador = db.Column(db.Integer, db.ForeignKey('jugador.id'), nullable= False)
    rueda = db.Column(db.Integer, db.ForeignKey('rueda.id'), nullable= False)
    fecha_creacion = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Apuesta %r>' % self.color
