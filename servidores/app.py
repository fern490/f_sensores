#
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/api/sensor", methods=['POST'])
def escribir_valor():
    datos = request.get_json()

    valor = datos['valor']
    sensor_name = datos['sensor_name']

    print(f"Sensor: {sensor_name}, Valor: {valor}")

    return "ok"