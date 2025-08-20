import sqlite3
from flask import Flask, g, jsonify, request, url_for, render_template
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
    nombre = datos.get('nombre')

    if valor is None or nombre is None:
        return jsonify({"error": "Faltan datos"}), 400

    db = abrirConexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO valores (nombre, valor) VALUES (?, ?)",
        (nombre, valor)
    )
    db.commit()

    print(f"Sensor: {nombre}, Valor: {valor} (guardado en DB)")

    return jsonify({"resultado": "OK"})

@app.route("/api/valores", methods=['GET'])
def listar_valores():
    args = request.args
    pagina = int(args.get("page", 1))
    descartar = (pagina - 1) * resultados_por_pag

    db = abrirConexion()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) AS cant FROM valores;")
    cant = cursor.fetchone()["cant"]
    paginas = ceil(cant / resultados_por_pag) if cant > 0 else 1

    if pagina < 1 or pagina > paginas:
        return jsonify({"error": f"Página inexistente: {pagina}"}), 400

    # obtener registros paginados
    cursor.execute(
        """SELECT id, nombre, valor, fecha_hora FROM valores
           ORDER BY fecha_hora DESC
           LIMIT ? OFFSET ?;""",
        (resultados_por_pag, descartar),
    )
    lista = cursor.fetchall()

    return jsonify({"results": lista})

if __name__ == '__main__':
    app.run(debug=True)
