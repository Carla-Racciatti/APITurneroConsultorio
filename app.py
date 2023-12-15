#PROYECTO FINAL - RACCIATTI CARLA - PROGRAMACIÓN II

from flask import Flask

#cargo las funciones para inicializar
from modelos.pacientes import inicio_pacientes
from modelos.medicos import inicio_medicos
from modelos.turnos import inicio_turnos
from modelos.agenda_medicos import inicio_agenda

#cargo los blueprints
from controladores.rutas_pacientes import pacientes_bp
from controladores.rutas_medicos import medicos_bp
from controladores.rutas_agenda_medicos import agenda_bp
from controladores.rutas_turnos import turnos_bp

app = Flask(__name__)

#inicializo
inicio_pacientes()
inicio_medicos()
inicio_turnos()
inicio_agenda()

#registro los blueprints en la aplicación 
app.register_blueprint(pacientes_bp)
app.register_blueprint(medicos_bp)
app.register_blueprint(agenda_bp)
app.register_blueprint(turnos_bp)

if __name__ == "__main__":
    app.run(debug=True, port=4000)

