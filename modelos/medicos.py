import csv
import os
from modelos.api import get_medicos #importo función que pide datos de la api randomuser
#variables globales: 
medicos=[] #lista de medicos
id_medicos = 1
ruta_medicos= "modelos\\db\\medicos.csv"

#función para iniciar el archivo csv. En caso de que no exista el archivo, llama a la función para crearlo y escribir en él 
def inicio_medicos():
    global id_medicos 
    if os.path.exists(ruta_medicos):#chequeo que exista el archivo. si existe, importo sus datos
            importar_datos_desde_csv_medicos()
    else:#si no existe, lo creo y lo escribo con los datos de la api
        escribir_csv_medicos()             
        


# función para importar datos desde csv medicos: 
def importar_datos_desde_csv_medicos():
    global medicos 
    global id_medicos
    medicos =[] #limpio la lista 
    with open(ruta_medicos, newline='', encoding='utf8') as csvfile:
        reader= csv.DictReader(csvfile)
        for row in reader:
            medicos.append(row)
            id_medicos= int(row["id"]) + 1   
      #puede ser que el archivo exista pero esté vacio. entonces agrego otra validación: 
        # si la lista de medicos está vacía, llamo a la función para escribir en el csv
        if len(medicos) == 0:
                    escribir_csv_medicos()      


#función para crear/escribir en el archivo csv los datos de medicos proporcionados por la api random user
def escribir_csv_medicos():
    """
     escribe los datos de medicos generados por la api en el archivo CSV.
    """
    with open(ruta_medicos, 'w', newline='') as csvfile:
        global id_medicos
        campo_nombres = ["id", "dni","nombre", "apellido","matricula","telefono", "email","habilitado"]
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for med in get_medicos(100):#aquí sí le envío el número de resultados que deseo obtener de la api
            med['id'] = str(id_medicos)
            writer.writerow(med)
            id_medicos = id_medicos +1
        
#exportar a csv: 
def exportar_a_csv():
     with open(ruta_medicos, 'w', newline='') as csvfile:
        global medicos
        campo_nombres = ["id", "dni","nombre", "apellido","matricula","telefono", "email","habilitado"]
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for med in medicos:
            writer.writerow(med)

#Para obtener la lista de todos los médicos: 
def obtener_medicos():
     return medicos

# Para obtener un médico por su id: 
def obtener_medico_por_id(id):
     for medico in medicos: 
          if str(medico["id"]) == str(id):
               return medico #devuelve el medico si encuentra su id 
     return None     #devuelve none si no encuentra ese id 

#crear medico: 
def crear_medico(dni,nombre,apellido,matricula,telefono,email,habilitado):
     global id_medicos
     medicos.append({
          "id": id_medicos,
          "dni": dni, 
          "nombre": nombre, 
          "apellido": apellido, 
          "matricula":matricula, 
          "telefono":telefono, 
          "email": email, 
          "habilitado": habilitado   
        })
     id_medicos+=1
     exportar_a_csv()
     return medicos[-1] #devuelve el medico recien creado


# actualizar medico por su id:
def actualizar_medico(id_medicos, dni, nombre, apellido,matricula, telefono, email, habilitado):
    print("actualizar_medico")
    for medico in medicos:
        if medico["id"] == str(id_medicos):
            medico["dni"] = dni
            medico["nombre"] = nombre
            medico["apellido"] = apellido
            medico["matricula"] = matricula
            medico["telefono"] = telefono
            medico["email"] = email
            medico["habilitado"] = habilitado
            exportar_a_csv()
            return medico
    return None

#actualizar habilitacion del medico: 
'''
en mi archivo csv, el campo habilitado tiene un valor de 1 o 0 siendo 1= habilitado y 0= deshabilitado.

'''
def deshabilitar_medico(id):
    medico= obtener_medico_por_id(id)
    if medico:
        medico["habilitado"]=0  
        exportar_a_csv()    
        return medico
    else:     
      return None
    
#agrego funcion extra para volver a habilitar medico por su id 
def habilitar_medico(id):
    medico= obtener_medico_por_id(id)
    if medico:
        medico["habilitado"]=1  
        exportar_a_csv()    
        return medico
    else:     
      return None
    

   
     
                
