'''
Decidí hacer un archivo aparte para manejo de request a la api de random user.
'''

import requests

#función para obtener lista de pacientes generada por random user 
def get_pacientes(num_pacientes):
    
    URL = f"https://randomuser.me/api/?inc=id,name_first,name,phone,email,location&nat=US&results={num_pacientes}"
            #en la URL pido solo los datos necesarios. Decidí no poner una cantidad fija de resultados, sino usar la variable num_pacientes
    response_pacientes = requests.get(URL)

    codigo_respuesta = response_pacientes.status_code

    if codigo_respuesta == 200:
        respuesta_json = response_pacientes.json()
        pacientes = []

        for pac in respuesta_json['results']:
        
            paciente ={
                "dni": pac['id']['value'].replace("-", "")[:8], #para quitar los guiones y para solo tener 8 digitos
                "nombre": pac['name']['first'],
                "apellido": pac['name']['last'],
                "telefono": pac['phone'],
                "email": pac['email'],
                "direccion_calle": pac['location']['street']['name'],
                "direccion_numero": pac['location']['street']['number'],
            }
            pacientes.append(paciente)
    elif codigo_respuesta == 400:
        print("Error en la llamada a la API")
        
    return pacientes

#función para obtener lista de medicos generada por random user 
def get_medicos(num_medicos):
    
    URL = f"https://randomuser.me/api/?inc=id,name,phone,email,login&password=number,6-6&nat=US&results={num_medicos}"
            #en la URL pido solo los datos necesarios. Decidí no poner una cantidad fija de resultados, sino usar la variable num_medicos
    response_medicos = requests.get(URL)

    codigo_respuesta = response_medicos.status_code

    if codigo_respuesta == 200:
        respuesta_json = response_medicos.json()
        medicos = []

        for med in respuesta_json['results']:
        
            medico ={
                "dni": med['id']['value'].replace("-", "")[:8], #para quitar los guiones y para solo tener 8 digitos
                "nombre": med['name']['first'],
                "apellido": med['name']['last'],
                "matricula": med['login']['password'],
                "telefono": med['phone'],
                "email": med['email'],
                "habilitado":1 #por defecto los medicos están habilitados. decidí que "1" signifique habilitado y "0" deshabilitado
                
            }
            medicos.append(medico)
    elif codigo_respuesta == 400:
        print("Error en la llamada a la API")
        
    return medicos
