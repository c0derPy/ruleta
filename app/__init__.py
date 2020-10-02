from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ruleta_simulador_key'

from app.api import bp as api_bp
app.register_blueprint(api_bp, prefix='/api')