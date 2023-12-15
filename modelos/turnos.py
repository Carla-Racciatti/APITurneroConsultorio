import csv
import os
import datetime

#variables globales a utilizar: 
turnos=[]
ruta_archivo_turnos= 'modelos\\db\\turnos.csv'

#iniciar turnos
def inicio_turnos():
    global turnos
    turnos = []  # Limpio la lista
    with open(ruta_archivo_turnos, newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            turnos.append(row)
            id_turnos = int(row["id"]) + 1 

#obtener todos los turnos: 
def obtener_turnos():
    return turnos           


def turno_pendiente(id_paciente): 
    #devuelve true si tiene turno pendiente, y false si no tiene turno pendiente
    global turnos
    for turno in turnos:
        if turno["id_paciente"]==str(id_paciente):  
            return True 
    return False

 #obtener todos los turnos de un medico por su id: 


#obtener todos los turnos pendientes de un médico por su id : 

# Registrar un nuevo turno 

# Verificar: la fecha del turno debe estar dentro de los próximos 30 días respecto al día actual
# verificar que el médico esté habilitado a dar turnos, 
#que el turno solicitado sea en un día de la semana que el médico trabaja,
# que el horario del turno solicitado esté dentro del rango horario de atención del médico 
# que no se haya dado ese turno.