
from cola_prioridad import ColaPrioridadMax, ColaPrioridadMin
from grafo import Grafo, Vertice
import numpy as np


def dijkstra_capacidad_de_carga(grafo, inicio):
    '''
    Este algoritmo de dijkstra modificado se utiliza para buscar
    la mayor capacidad de carga posible, buscando el menor cuello de botella.
    Utilizando una Cola de Prioridad inicializada con un Montículo de Máximos.

    Parameters
    ----------
    grafo : Grafo()
        Grafo cargado con las ciudades y sus capacidades de carga.
    inicio : Vertice
        Ciudad de inicio.

    Returns
    -------
    None.

    '''
    
    # Inicializo la Cola de Prioridad (Con un Montículo de Máximos)
    cp = ColaPrioridadMax()
    
    '''
    Se inicializa con Infinito el inicio, ya que es el mejor caso, así cuando se comparan los
    cuello de botella, se actualiza con el menor entre infinito y la ponderación para llegar
    al siguiente Vértice.
    '''
    inicio.asignarDistancia(np.Inf)  # Infinito
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in grafo]) # El resto de vértices se inicializa con 0
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()    # Vértice con mayor capacidad de carga
        
        # Recorro todos los vecinos del Vértice actual
        for verticeSiguiente in verticeActual.obtenerConexiones():
            
            '''
            Cuello de botella (Capacidad de carga que limita el camino).
            Se busca la capacidad de carga mínima.
            '''
            distancia = min(verticeActual.obtenerDistancia(), verticeActual.obtenerPonderacion(verticeSiguiente))
            
            
            '''
            Si la ponderación del vértice siguiente es menor
            al mínimo cuello de botella, se actualiza su ponderación
            y se guarda el predecesor.
            '''
            if distancia > verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia(distancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente, distancia)
    
    
def dijkstra_precio(grafo, inicio):
    '''
    Este algoritmo de dijkstra se utiliza para buscar
    el menor precio posible para llegar a un Vértice,
    Utilizando una Cola de Prioridad inicializada con
    un Montículo de Mínimos.

    Parameters
    ----------
    grafo : Grafo
        Grafo cargado con las ciudades y sus precios.
    inicio : Vertice
        Ciudad de inicio.

    Returns
    -------
    None.

    '''
    
    # Inicializo la Cola de Prioridad (Con un Montículo de Mínimos)
    cp = ColaPrioridadMin()
    
    '''
    Se inicializa con 0 el inicio, ya que es el mejor caso, así cuando se comparan los
    precios, se actualiza con el menor entre el vértice de inicio y la ponderación (Precio) 
    para llegar al siguiente Vértice.
    '''
    inicio.asignarDistancia(0)
    
    '''Inicializo la ponderación de los Vértices, en infinito '''
    for vertice in grafo:
        if vertice == inicio:       # Si el Vértice, es el de Inicio, continua con el bucle para no modificar su ponderación
            continue
        vertice.asignarDistancia(np.Inf)    # Inicializo los vértices con Infinito
        
    # Creo el Montículo de mínimos
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in grafo])
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        
        # Recorro todos los vecinos del Vértice actual
        for verticeSiguiente in verticeActual.obtenerConexiones():
            
            '''
            Sumo el precio del Vértice actual con el precio de la arista que conecta al vecino,
            para luego compararlo con la ponderación actual del Vecino, y ver si conviene esta ruta.
            '''
            nuevoPrecio = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
            
            if nuevoPrecio < verticeSiguiente.obtenerDistancia():
                '''
                Si el nuevo Precio es menor al precio del Vértice vecino,
                Se actualiza la ponderación del Vecino con el nuevo Precio
                y se guarda el Predecesor.
                '''
                verticeSiguiente.asignarDistancia(nuevoPrecio)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente, nuevoPrecio)