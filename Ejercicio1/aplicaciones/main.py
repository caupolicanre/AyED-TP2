from modulos.monticulo_binario import MonticuloBinario
    
"""
Sala de emergencias
"""

import time
import datetime
from modulos.paciente import Paciente
import random

n = 20  # cantidad de ciclos de simulación

'''Inicializo la cola de espera como un montículo binario de mínimos, 
así cada vez que sale de la cola un paciente, 
es el que tiene un nivel de riesgo (1, 2 o 3) menor.
Siendo 1: crítico, 2: moderado y 3: bajo'''
cola_de_espera = MonticuloBinario()

# Ciclo que gestiona la simulación
for i in range(n):
    
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*25)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = Paciente(turno = i+1, hora = ahora.strftime('%H:%M:%S'))  # Se inicializa con un turno de llegada y se registra la hora de ingreso
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        ''' Se atiende paciente que se encuentra al frente de la cola '''
        paciente_atendido = cola_de_espera.eliminar_min()
        print('*'*80)
        print(' Se atiende el paciente:', paciente_atendido)
        print('*'*80)
    else:
        ''' Se continúa atendiendo paciente de ciclo anterior '''
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*25)
    
    time.sleep(1)

