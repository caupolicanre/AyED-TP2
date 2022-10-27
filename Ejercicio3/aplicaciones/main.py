import csv
from Ejercicio3.modulos.grafo import Grafo, Vertice
from Ejercicio3.modulos.cola_prioridad import ColaPrioridad
from Ejercicio3.modulos.algoritmos_dijkstra import dijkstra_modificado

grafoRutas = Grafo()

with open("rutas.txt" + 'r') as rutas:
    lector = csv.reader(rutas, delimiter=",")
    for linea in lector:
        grafoRutas.agregarArista(linea[0], linea[1], int(linea[2]))

dijkstra_modificado(grafoRutas, inicio = grafoRutas)