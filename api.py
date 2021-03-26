import flask
from flask import request, jsonify
import psycopg2
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

conn = psycopg2.connect(host = "tuffi.db.elephantsql.com", database = "ewayqilc", user = "ewayqilc", password = "c_3fHeJM-wn6440Q4ZU0F9hf7dyDu9ba")
cur = conn.cursor()

@app.route('/', methods=['GET'])
def home():
    return '<h1>hello world!</h1>'

@app.route('/personas', methods=['GET'])
def get_personas():
    personas = []
    sql = "select * from per.persona"
    cur.execute(sql)
    for row in cur.fetchall():
        personas.append({
            'id': row[0],
            'nss': row[1],
            'nombre': row[2],
            'telefono': row[3]
        })
    return jsonify({
        'msg': 'personas recibidas correctamente',
        'personas': personas
    })

@app.route('/personas', methods=['POST'])
def add_persona():
    sql = f"""insert into per.persona(nss, nombre, telefono) 
    values({request.json['nss']}, '{request.json['nombre']}, {request.json['telefono']})"""
    cur.execute(sql)
    return jsonify({
        'msg': 'persona agregada correctamente'
    })