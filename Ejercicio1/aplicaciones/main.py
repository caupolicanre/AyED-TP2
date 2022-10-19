
"""
Sala de emergencias
"""

import time
import datetime
import modulos.paciente as pac
import modulos.monticulo_binario as mon
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = mon.MonticuloBinario()

# Ciclo que gestiona la simulación
for i in range(n):
    
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente(i+1)  # Se inicializa con un turno de llegada
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        ''' Se atiende paciente que se encuentra al frente de la cola '''
        paciente_atendido = cola_de_espera.eliminar_min()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        ''' Se continúa atendiendo paciente de ciclo anterior '''
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)

