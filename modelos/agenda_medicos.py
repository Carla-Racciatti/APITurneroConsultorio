import csv
import os
import datetime

#variables globales a utilizar: 
agenda=[]
ruta_archivo_agenda= 'modelos\\db\\agenda_medicos.csv'

#iniciar agenda
def inicio_agenda():
    global agenda
    agenda = []  # Limpio la lista
    with open(ruta_archivo_agenda, newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            agenda.append(row)

# función para exportar a csv
def exportar_a_csv():
    with open(ruta_archivo_agenda, 'w', newline='') as csvfile:
        campo_nombres = ['id_medico', 'dia_numero', 'hora_inicio', 'hora_fin','fecha_actualizacion']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for horario in agenda:
            writer.writerow(horario)


#para obtener la agenda ordenada como lo pide la consigna: 
def obtener_agenda():
    return sorted(agenda, key=lambda x: (x['id_medico'], x['dia_numero']))

#OBTENER LA AGENDA DE UN MEDICO ESPECÍFICO: 
#voy a utilizarlo para hacer la busqueda mas facil en algunas oportunidades. 

def obtener_agenda_por_id(id_medico):
    agenda_completa = obtener_agenda()
    agenda_medico = [horario for horario in agenda_completa if horario['id_medico'] == id_medico]
    return agenda_medico


#agregar día y horario de atención de un médico
def agregar_dia_y_horario(id_medico,dia_numero,hora_inicio,hora_fin):
    global agenda
    agenda.append({
        "id_medico": id_medico,
        "dia_numero": dia_numero,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
        "fecha_actualizacion": datetime.datetime.now().strftime("%Y-%m-%d")
    })
    exportar_a_csv()
    return agenda[-1]  # devuelve el nuevo día y horario de atencion recién creado

#- - - 
#función para averiguar si un médico trabaja en un día específico
def trabaja_en_dia(id_medico, dia_numero):
    # Obtengo los horarios del médico del archivo agenda_medicos
    horarios_medico = obtener_agenda_por_id(id_medico)

    # Verifico si el médico trabaja en el día especificado, utilizando strftime como lo sugiere la consigna
    for horario_medico in horarios_medico:
        if horario_medico['dia_numero'] == str(dia_numero) and horario_medico['id_medico'] == str(id_medico):
            return True
    return False


#Modificar el horario de atención si es que el médico trabaja en ese día
'''
la request a enviar tendría el siguiente formato: 
{
  "id_medico": 7,
  "nuevos_horarios": [
    {"dia_a_editar": 1, "hora_inicio_a_modificar": "10:00", "hora_fin_a_modificar": "17:00"},
    {"dia_a_editar": 3, "hora_inicio_a_modificar": "8:00", "hora_fin_a_modificar": "12:00"}
  ]
}
'''
def modificar_horarios_atencion(id_medico, nuevos_horarios):
    for nuevo_horario in nuevos_horarios:
        dia_a_editar = nuevo_horario['dia_a_editar']
        hora_inicio_a_modificar = nuevo_horario['hora_inicio_a_modificar']
        hora_fin_a_modificar = nuevo_horario['hora_fin_a_modificar']
         
        print(hora_fin_a_modificar)  
        # Lógica para modificar los horarios de atención existentes
        for horario in agenda:
            if horario['id_medico'] == str(id_medico) and horario['dia_numero'] == str(dia_a_editar):
                horario['hora_inicio'] = hora_inicio_a_modificar
                horario['hora_fin'] = hora_fin_a_modificar  
    exportar_a_csv()
    return agenda







#Eliminar los días de atención de un medico por su id  en un día especifico
#se deben enviar los días a eliminar. 


# Función para eliminar los días de atención de un médico por su ID
def eliminar_dias_atencion(id_medico):
    
    global agenda
    

    agenda_actualizada = [horario for horario in agenda if horario['id_medico'] != str(id_medico)]
    if len(agenda_actualizada) < len(agenda):
        agenda = agenda_actualizada
        exportar_a_csv()
        return True
    else:     
        return False
            
             
  
