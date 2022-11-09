# Ponderación es el peso de la arista, es fijo
# Dist varía, es la acumulacion del as aristas

class Vertice:
    def __init__(self, clave):
        self.clave = clave      # Nombre de la ciudad
        self.conectadoA = {}    # Ciudades a las que está conectada
        self.dist = 0           # Distancia que está en la arista que conecta el predecesor con el vertice actual.
        self.predecesor = None

    def __str__(self):
        '''
        Retorna la ciudad, y las ciudades a las que está conectada.

        Returns
        -------
        str
            String con los datos del vértice.

        '''
        return str(self.clave) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def agregarVecino(self, vecino, ponderacion=0):
        '''
        Agrega un vecino al Vértice actual con la 
        ponderación para llegar a éste.

        Parameters
        ----------
        vecino : Vertice()
            Vecino del vértice actual.
        ponderacion : int, optional
            Ponderación de la arista que conecta a los vértices.
            Por defecto es 0.

        Returns
        -------
        None.

        '''
        self.conectadoA[vecino] = ponderacion

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerClave(self):
        '''
        Getter de clave.

        Returns
        -------
        any type
            Clave del Nodo Actual.

        '''
        return self.clave

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
    
    def obtenerPredecesor(self):
        '''
        Getter de predecesor.

        Returns
        -------
        reference
            Vértice predecesor del Vértice actual.

        '''
        return self.predecesor
    

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0    # Contador de Vértices

    def __getitem__(self, clave):
        return self.obtenerVertice(clave)

    def agregarVertice(self, clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        '''
        Busca al Vértice en el Grafo, y lo retorna.

        Parameters
        ----------
        n : Clave
            Clave del vértice a buscar.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
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
            Costo (Peso) que tiene la Arista. Por defecto es 0.

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
        
        '''
        Agrega al segundo Vértice como vecino del primer Vértice,
        Creando una arista con la ponderación
        '''
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        '''
        Retorna todos los vertices del Grafo
        '''
        return self.listaVertices.keys()

    def __iter__(self):
        '''Método para iterar el Grafo.'''
        return iter(self.listaVertices.values())