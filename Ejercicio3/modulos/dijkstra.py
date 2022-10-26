
from cola_prioridad import ColaPrioridad


def dijkstra(unGrafo, inicio):
    
    cp = ColaPrioridad()
    
    inicio.asignar_distancia(0)
    cp.construirMonticulo([(v.obtener_distancia(),v) for v in unGrafo])
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtener_distancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtener_distancia():
                verticeSiguiente.asignar_distancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)