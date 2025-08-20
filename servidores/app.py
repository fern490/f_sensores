import sqlite3
from flask import Flask, g, jsonify, request, url_for
from math import ceil

app = Flask(__name__)

# MANEJO DE LA BASE DE DATOS
def dict_factory(cursor, row):
    """Arma un diccionario con los valores de la fila."""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def abrirConexion():
    if 'db' not in g:
        g.db = sqlite3.connect("valor.sqlite")
        g.db.row_factory = dict_factory
    return g.db

def cerrarConexion(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

app.teardown_appcontext(cerrarConexion)

resultados_por_pag = 10

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

# RUTA SENSOR
@app.route("/api/sensor", methods=['POST'])
def escribir_valor():
    datos = request.get_json()

    valor = datos.get('valor')
    sensor_name = datos.get('sensor_name')

    print(f"Sensor: {sensor_name}, Valor: {valor}")

    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
