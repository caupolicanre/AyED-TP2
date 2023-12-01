# Algorithm and Data Structures - Practical Work 2

This repository contains scripts for the Algorithm and Data Structures Practical Work 2.  
Tecnicatura Universitaria en Procesamiento y Explotación de Datos, Facultad de Ingeniería UNER. Brehm, Ré. 2022

## Exercise 1: Emergency Room

### Description
Emergency Room Management using a minimum binary heap structure. Patients are prioritized and served based on their critical risk level, with earliest arrivals attended first in case of identical risk levels. Complexity for insertion and removal: Avg: O(log n), Best: O(1), Worst: O(log n).

### Files
- [`main.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio1/aplicaciones/main.py): Emergency room app.
- [`monticulo_binario.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio1/modulos/monticulo_binario.py): Minimum binary heap structure.
- [`paciente.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio1/modulos/paciente.py): Emergency room patient class.

## Exercise 2: Temperaturas_DB

### Description
The temperature database exercise employs an AVL tree, ensuring efficient storage and retrieval of temperature records through self-balancing properties.

### Files
- [`AVL.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio2/modulos/AVL.py): Contains the AVL Data Structure.
- [`Temperaturas_DB.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio2/modulos/Temperaturas_DB.py): Implements a class for managing temperatures using the AVL data structure.
- [`test_Temperaturas_DB.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio2/pruebas/test_Temperaturas_DB.py): Tests the temperature management class.

## Exercise 3: Transportation Service

### Description
Involves loading data into a graph, using a modified Dijkstra's algorithm with priority queues to determine the route with the highest load capacity and lowest cost from the initial city to the destination city.

### Files
- [`main.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio3/aplicaciones/main.py): Main application for city selection
- [`procesamiento.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio3/aplicaciones/procesamiento.py): Routes file processing and use of graph data structure and dijkstra's algorithm.
- [`rutas.txt`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio3/aplicaciones/rutas.txt): Routes file.
- [`algoritmos_dijkstra.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio3/modulos/algoritmos_dijkstra.py): Dijkstra's algorithms.
- [`cola_prioridad.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio3/modulos/cola_prioridad.py): Implements two priority queue classes, one based on a Max Heap and the other on a Min Heap.
- [`grafo.py`](https://github.com/caupolicanre/AyED-TP2/blob/main/Ejercicio3/modulos/grafo.py): Graph Data Structure.
