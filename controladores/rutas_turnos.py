from flask import Blueprint, jsonify, request 
from modelos.turnos import obtener_turnos

turnos_bp = Blueprint('turnos_bp',__name__)

#obtener todos los turnos 
@turnos_bp.route('/turnos', methods=['GET'])
def buscar_turnos():
    turno=obtener_turnos()
    if len(turno) > 0:
       return jsonify(turno), 200
    else: 
       return jsonify({'error': 'No hay turnos'}), 404


