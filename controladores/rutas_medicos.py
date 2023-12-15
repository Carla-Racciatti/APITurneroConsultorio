from flask import Blueprint, jsonify, request 
from modelos.medicos import obtener_medicos, obtener_medico_por_id, crear_medico, actualizar_medico, deshabilitar_medico, habilitar_medico
#actualizar_habilitado_medico


 # creo Blueprint para medicos
medicos_bp = Blueprint('medicos_bp', __name__)

#obtener todos los médicos: 
@medicos_bp.route('/medicos', methods=['GET'])
def buscar_medicos():
    medico=obtener_medicos()
    if len(medico) > 0:
       return jsonify(medico), 200
    else: 
       return jsonify({'error': 'No hay medicos'}), 404
    
#obtener medico por id: 
@medicos_bp.route('/medicos/<int:id>', methods=['GET'])
def buscar_medico_por_id(id):
    medico=obtener_medico_por_id(id)
    if medico:
       return jsonify(medico), 200
    else:
       return jsonify({'error': 'Médico no encontrado'}), 404
    
#crear medico
@medicos_bp.route('/medicos', methods=['POST'])
def nuevo_medico():
    if request.is_json:
      nuevo= request.get_json()
      print("soy carla")
      if 'dni' in nuevo and 'nombre' in nuevo and 'apellido' in nuevo and 'matricula' in nuevo and 'telefono' in nuevo and 'email' in nuevo and 'habilitado' in nuevo:
         medico_creado = crear_medico(nuevo['dni'], nuevo['nombre'], nuevo['apellido'], nuevo['matricula'], nuevo['telefono'], nuevo['email'], nuevo['habilitado'])
         print("soy carla")
         return jsonify(medico_creado), 201
      else:
         return jsonify({'error': 'Faltan datos'}), 400
    else:
      return jsonify({'error': 'No se ha recibido el formato json'}), 400
    
    

#actualizar medico
@medicos_bp.route('/medicos/<int:id>', methods=['PUT'])
def editar_medico(id):
    if request.is_json:
        actualizar = request.get_json()
        if 'dni' in actualizar and 'nombre' in actualizar and 'apellido' in actualizar and 'matricula' in actualizar and 'telefono' in actualizar and 'email' in actualizar and 'habilitado' in actualizar:
            medico_actualizado = actualizar_medico(id,actualizar['dni'], actualizar['nombre'], actualizar['apellido'],actualizar['matricula'], actualizar['telefono'], actualizar['email'], actualizar['habilitado'])
            if medico_actualizado:
                return jsonify(medico_actualizado), 200
            else:
                return jsonify({'error': 'Medico no encontrado'}), 404
        else:
            return jsonify({'error': 'Faltan datos'}), 400
    else:
        return jsonify({'error': 'No se ha recibido el formato json'}), 400


#deshabilitar medico
@medicos_bp.route('/medicos/deshabilitar/id', methods=['PUT'])    
def inhabilitar_medico(id):
   if request.is_json:
      inhabilitar= request.get_json()
      if 'id' in inhabilitar:
         inhabilitado= deshabilitar_medico(id)
         if inhabilitado:
            return jsonify(inhabilitado), 200
         else:
            return jsonify({'error': 'No existe el id'}), 400 
   else: 
      return jsonify({'error': 'No se ha recibido el formato json'}), 400

#agrego extra habilitar medico
@medicos_bp.route('/medicos/habilitar/id', methods=['PUT'])    
def activar_medico(id):
   if request.is_json:
      habilitar= request.get_json()
      if 'id' in habilitar:
         habilitado= habilitar_medico(id)
         if habilitado:
            return jsonify(habilitado), 200
         else:
            return jsonify({'error': 'No existe el id'}), 400 
   else: 
      return jsonify({'error': 'No se ha recibido el formato json'}), 400

