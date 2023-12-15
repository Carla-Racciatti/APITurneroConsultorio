from flask import Blueprint, jsonify, request 
from modelos.agenda_medicos import obtener_agenda, agregar_dia_y_horario,modificar_horarios_atencion, eliminar_dias_atencion



agenda_bp = Blueprint('agenda_bp',__name__)

#obtener agenda con horarios 
@agenda_bp.route('/agenda_medicos', methods=['GET'])
def obtener_horarios():
    horarios= obtener_agenda()
    if len(horarios) > 0:
        return jsonify(horarios), 200
    else: 
        return jsonify({'error': 'No hay horarios habilitados'}), 404
    
'''
 obtener agenda por id del medico
@agenda_bp.route('/agenda_medicos/<int:id_medico>', methods=['GET'])    
def obtener_horarios_por_id_(id_medico):
    agenda_medico= obtener_agenda_por_id(id_medico)
    if agenda_medico:
       return jsonify(agenda_medico), 200
    else:
       return jsonify({'error': 'paciente no encontrado'}), 404
 '''   



#agregar nuevo día y horario de atención: 
@agenda_bp.route('/agenda_medicos', methods=['POST'])
def agregar_atencion():
    if request.is_json:
        nuevo_horario = request.get_json()
        if 'id_medico' in nuevo_horario and 'dia_numero' in nuevo_horario and 'hora_inicio' in nuevo_horario and 'hora_fin' in nuevo_horario: 
            horario_agregado = agregar_dia_y_horario(nuevo_horario['id_medico'], nuevo_horario['dia_numero'], nuevo_horario['hora_inicio'], nuevo_horario['hora_fin'])
            if horario_agregado:
              return jsonify({"mensaje": "Horario agregado con éxito"}), 201
            else:
              return jsonify({"mensaje": "No se pudo agregar el horario"}), 400
        else: 
           return jsonify({'error': 'Faltan datos'}), 400
    else:
       return jsonify({'error': 'No se ha recibido el formato json'}), 400
    

   


@agenda_bp.route('/agenda_medicos/<int:id>', methods=['PUT'])
def modificar_horarios(id):
    if request.is_json:
        nuevo = request.get_json()
        if 'id_medico' in nuevo and 'nuevos_horarios' in nuevo:
            horario_actualizado = modificar_horarios_atencion(nuevo['id_medico'], nuevo['nuevos_horarios'])
            if horario_actualizado:
                return jsonify(horario_actualizado), 200
            else:
                return jsonify({"mensaje": "No se pudo modificar el horario"}), 404  
        else:
            return jsonify({'error': 'Faltan datos'}), 400
    else:
        return jsonify({'error': 'No se recibió fomrato JSON'}), 400




@agenda_bp.route('/agenda_medicos/<int:id_medico>', methods=['DELETE'])
def eliminar_horarios(id_medico):
    horario_eliminado = eliminar_dias_atencion(id_medico)
    if horario_eliminado:
        return jsonify({"mensaje": "Horarios de atención eliminados con éxito"}), 200
    else:
        return jsonify({"mensaje": "No se encontró un médico con ese id"}), 400
