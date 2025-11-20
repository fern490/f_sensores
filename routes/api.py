from flask import Blueprint, request, jsonify
from models import db, Medicion

api_bp = Blueprint("api", __name__)

@api_bp.get("/config") 
def get_config():
    return jsonify({"limite_potencia": 15})

@api_bp.post("/datos")
def recibir_datos():
    data = request.get_json()

    nueva = Medicion(
        voltaje=data.get("voltaje"),
        corriente=data.get("corriente"),
        potencia=data.get("potencia"),
        wh_total=data.get("wh_total")
    )

    db.session.add(nueva)
    db.session.commit()

    return jsonify({"status": "ok"})
