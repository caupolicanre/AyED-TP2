
from cola_prioridad import ColaPrioridad
from grafo import Grafo, Vertice


def dijkstra_modificado(unGrafo, inicio):
    
    cp = ColaPrioridad()
    
    inicio.asignarDistancia(9999999999999)  # Infinito
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()
        
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
                    
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)