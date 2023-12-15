import csv
import os
from modelos.api import get_pacientes  # Importo función que pide datos de la api randomuser

pacientes = []
id_pacientes = 1
ruta_pacientes = "modelos\\db\\pacientes.csv"


# función para iniciar el archivo csv. En caso de que no exista el archivo, llama a la función para crearlo y escribir en él
def inicio_pacientes():
    global id_pacientes
    if os.path.exists(ruta_pacientes):  # Chequeo que exista el archivo. si existe, importo sus datos
        importar_datos_desde_csv_pacientes()
    else:  # Si no existe, lo creo y lo escribo con los datos de la api
        escribir_csv_pacientes()


# función para importar datos desde csv pacientes:
def importar_datos_desde_csv_pacientes():
    global pacientes
    global id_pacientes
    pacientes = []  # Limpio la lista
    with open(ruta_pacientes, newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pacientes.append(row)
            id_pacientes = int(row["id"]) + 1  
        # puede ser que el archivo exista pero esté vacío. entonces agrego otra validación:
        # si la lista de pacientes está vacía, llamo a la función para escribir en el csv
        if not pacientes:
            escribir_csv_pacientes()


# función para crear/escribir en el archivo csv los datos de pacientes proporcionados por la api random user
def escribir_csv_pacientes():
    """
     escribe los datos de pacientes generados por la api en el archivo CSV.
    """
    with open(ruta_pacientes, 'w', newline='') as csvfile:
        global id_pacientes
        campo_nombres = ["id", "dni", "nombre", "apellido", "telefono", "email", "direccion_calle", "direccion_numero"]
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for pac in get_pacientes(100):  # aquí sí le envío el número de resultados que deseo obtener de la api
            pac['id'] = str(id_pacientes)
            writer.writerow(pac)
            id_pacientes += 1


# función para exportar a csv
def exportar_a_csv():
    with open(ruta_pacientes, 'w', newline='') as csvfile:
        global id_pacientes
        campo_nombres = ["id", "dni", "nombre", "apellido", "telefono", "email", "direccion_calle", "direccion_numero"]
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for pac in pacientes:
            writer.writerow(pac)


# obtener todos los pacientes:
def obtener_pacientes():
    return pacientes


# Para obtener un paciente por su id:
def obtener_paciente_por_id(id):
    global id_pacientes
    for paciente in pacientes:
        if str(paciente["id"]) == str(id):
          return paciente  # devuelve el paciente si encuentra su id
    return None  # devuelve none si no encuentra ese id


# crear paciente
def crear_paciente(dni, nombre, apellido, telefono, email, direccion_calle, direccion_numero):
    global id_pacientes
    pacientes.append({
        "id": id_pacientes,
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "direccion_calle": direccion_calle,
        "direccion_numero": direccion_numero
    })
    id_pacientes += 1
    exportar_a_csv()
    return pacientes[-1]  # devuelve el paciente recién creado


# actualizar paciente por su id:
def actualizar_paciente(id_pacientes, dni, nombre, apellido, telefono, email, direccion_calle, direccion_numero):
    for paciente in pacientes:
        if  paciente["id"]== str(id_pacientes):
            paciente["dni"] = dni
            paciente["nombre"] = nombre
            paciente["apellido"] = apellido
            paciente["telefono"] = telefono
            paciente["email"] = email
            paciente["direccion_calle"] = direccion_calle
            paciente["direccion_numero"] = direccion_numero
            exportar_a_csv()
            return paciente
    return None


def eliminar_paciente_por_id(id):
    global pacientes
    pacientes = [paciente for paciente in pacientes if int(paciente["id"]) != int(id)]
    exportar_a_csv()
    if len(pacientes) > 0:
        return pacientes, 200
    else: 
        return None, 200

   