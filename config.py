import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = 'ruleta_simulador_key'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///'+os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False