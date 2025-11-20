from config import db
from datetime import datetime, UTC

class Medicion(db.Model):
    __tablename__ = 'mediciones'

    medicion_id = db.Column(db.Integer, primary_key=True)
    voltaje = db.Column(db.Float, nullable=False)
    corriente = db.Column(db.Float, nullable=False)
    potencia = db.Column(db.Float, nullable=False)
    wh_total = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
