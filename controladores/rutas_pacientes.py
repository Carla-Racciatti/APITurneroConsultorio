from flask import Blueprint, jsonify, request 
from modelos.pacientes import obtener_pacientes, obtener_paciente_por_id, crear_paciente, actualizar_paciente, eliminar_paciente_por_id 
from modelos.turnos import turno_pendiente


pacientes_bp = Blueprint('pacientes_bp',__name__)


#obtener todos los pacientes 
@pacientes_bp.route('/pacientes', methods=['GET'])
def buscar_pacientes():
    paciente=obtener_pacientes()
    if len(paciente) > 0:
       return jsonify(paciente), 200
    else: 
       return jsonify({'error': 'No hay pacientes'}), 404
    

#obtener paciente por id: 
@pacientes_bp.route('/pacientes/<int:id>', methods=['GET'])
def buscar_paciente_por_id(id):
    paciente= obtener_paciente_por_id(id)
    if paciente:
       return jsonify(paciente), 200
    else:
       return jsonify({'error': 'paciente no encontrado'}), 404
    
#crear paciente
@pacientes_bp.route('/pacientes', methods=['POST'])
def nuevo_paciente():
    if request.is_json:
      nuevo= request.get_json()
      if 'dni' in nuevo and 'nombre' in nuevo and 'apellido' in nuevo and 'telefono' in nuevo and 'email' in nuevo and 'direccion_calle' in nuevo and 'direccion_numero' in nuevo:
         paciente_creado = crear_paciente(nuevo['dni'], nuevo['nombre'], nuevo['apellido'], nuevo['telefono'], nuevo['email'], nuevo['direccion_calle'], nuevo['direccion_numero'])
         return jsonify(paciente_creado), 201
      else:
         return jsonify({'error': 'Faltan datos'}), 400
    else:
      return jsonify({'error': 'No se ha recibido el formato json'}), 400
    

 # Actualizar datos de un paciente: 
@pacientes_bp.route('/pacientes/<int:id>', methods=['PUT'])
def editar_paciente(id):
    if request.is_json:
        actualizar = request.get_json()
        if 'dni' in actualizar and 'nombre' in actualizar and 'apellido' in actualizar and 'telefono' in actualizar and 'direccion_calle' in actualizar and 'direccion_numero' in actualizar:
            paciente_actualizado = actualizar_paciente(id,actualizar['dni'], actualizar['nombre'], actualizar['apellido'], actualizar['telefono'], actualizar['email'], actualizar['direccion_calle'], actualizar['direccion_numero'])
            if paciente_actualizado:
                return jsonify(paciente_actualizado), 200
            else:
                return jsonify({'error': 'Paciente no encontrado'}), 404
        else:
            return jsonify({'error': 'Faltan datos'}), 400
    else:
        return jsonify({'error': 'No se ha recibido el formato json'}), 400


#eliminar paciente 
@pacientes_bp.route('/pacientes/<int:id>', methods=['DELETE'])
def borrar_paciente(id): 
    paciente_pendiente = turno_pendiente(id)
    if not paciente_pendiente:
        eliminado = eliminar_paciente_por_id(id)
        if eliminado:
            return jsonify(eliminado), 200
        else:
            return jsonify({'error': 'paciente no encontrado'}), 404
    else:
        return jsonify({'error': 'No se puede eliminar un paciente con turnos pendientes'}), 400

