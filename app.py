#Monitor de consumo para un panel solar
#Componentes: ESP32 + sensor de tensión y corriente (ACS712 o INA219) + Pantalal OLED
#Funciones:
#Mide corriente y voltaje, calcula potencia y consumo acumulado.
#Muestra en la OLED potencia instantánea y consumo total.
#Envía los datos a una API o base de datos remota.
#Usa pandas y pyplot para graficar consumo diario o por hora.
#💡: Alerta si se supera cierto límite de potencia (mostrando un aviso en pantalla).

import sqlite3
from flask import Flask, g, jsonify, request, url_for
from math import ceil

def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}

def abrirConexion():
   if 'db' not in g:
      g.db = sqlite3.connect("sensores.sqlite")
      g.db.row_factory = dict_factory
   return g.db

def cerrarConexion(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

app = Flask(__name__)
app.teardown_appcontext(cerrarConexion)

@app.route("/api/test")
def test():
    return "funcionando!"

@app.route("/api/sensor", methods=['POST'])
def sensor():
    datos = request.json
    nombre = datos["nombre"]
    valor = datos["valor"]
    print(f"nombre del sensor {nombre}, valor: {valor}")
    return "OK"

