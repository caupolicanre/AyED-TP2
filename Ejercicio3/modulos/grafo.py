# Ponderación es el peso de la arista, es fijo
# Dist varía, es la acumulacion del as aristas

class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.dist = 0
        self.predecesor = None

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        '''
        Retorna la ciudad, y las ciudades a las que está conectada.

        Returns
        -------
        str
            String con los datos del vértice.

        '''
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        '''
        Getter de clave.

        Returns
        -------
        any type
            Clave del Nodo Actual.

        '''
        return self.id

    def obtenerPonderacion(self, vecino):
        '''
        Getter de Ponderacion.
        Peso/Costo de la arista.
        '''
        return self.conectadoA[vecino]
    
    def obtenerDistancia(self):
        '''
        Getter de dist.

        Returns
        -------
        int
            Distancia del vertice.

        '''
        return self.dist
    
    def asignarDistancia(self, nuevaDistancia):
        '''
        Setter de dist.

        Parameters
        ----------
        nuevaDistancia : int
            Distancia que va a reemplazar la actual.
        '''
        self.dist = nuevaDistancia
    
    def asignarPredecesor(self, predecesor):
        '''
        Setter de predecesor.
        '''
        self.predecesor = predecesor
    

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def __getitem__(self, clave):
        return self.obtenerVertice(clave)

    def agregarVertice(self, clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.listaVertices

    def agregarArista(self, de, a, costo=0):
        '''
        Genera una nueva arista de un Vértice a otro.
        Si alguno de los Vértices no existe, los crea,
        y luego los conecta.

        Parameters
        ----------
        de : Vertice()
            Vértice inicial.
        a : Vertice()
            Vecino del vértice inicial.
        costo : int, optional
            Cosot (Peso) que tiene la Arista. Por defecto es 0.

        Returns
        -------
        None.

        '''
        if de not in self.listaVertices:
            '''Si el primer Vértice no existe, lo crea'''
            nv = self.agregarVertice(de)
            
        if a not in self.listaVertices:
            '''Si el segundo Vértice no existe, lo crea'''
            nv = self.agregarVertice(a)
            
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        '''Método para iterar el Grafo.'''
        return iter(self.listaVertices.values())