import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '<h1>probando la API, Equipo Rojo<h1/>'
