
class ColaPrioridadMax:
    '''
    Cola de Prioridad implementada con un Montículo de Máximos.
    '''
    
    def __init__(self):
        self.listaMonticulo = [(0,0)]
        self.tamanoActual = 0
        self.hijoMax
        
        
    # Métodos Mágicos
    
    def __len__(self):
        '''
        Método mágico que retorna el tamaño de la Cola de Prioridad.

        Returns
        -------
        int
            Entero que representa el tamaño de la Cola de Prioridad.

        '''
        return self.tamanoActual
    
    
    def __iter__(self):
        '''
        Método para iterar la Cola de Prioridad.
        '''
        
        for i in self.listaMonticulo:
            yield i
    
    
    def __str__(self):
        '''
        Retorna todos los elementos de la Cola de Prioridad.

        Returns
        -------
        str
            String con todos los elementos de la Cola de Prioridad.

        '''
        return str(self.listaMonticulo)
    
    def __contains__(self, vertice):
        for par in self.listaMonticulo:
            if par[1] == vertice:
                return True
            return False
    
    # Métodos
    
    def estaVacia(self) -> bool:
        '''
        Comrpueba si la Cola de Prioridad está vacía.

        Returns
        -------
        bool
            Si la Cola de Prioridad no contiene ningún elemento,
            retorna True, si contiene algun elemento, retorna False.

        '''
        return self.tamanoActual == 0
    
    def infiltArriba(self, i):
        '''
        Infiltra un Í­tem hacia arriba en el Árbol hasta donde 
        sea necesario para mantener la propiedad de montí­culo.

        Parameters
        ----------
        i : int
            Tamaño de la Cola de Prioridad.

        Returns
        -------
        None.

        '''
        while i // 2 > 0:
          if self.listaMonticulo[i][0] > self.listaMonticulo[i // 2][0]:
             temp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = temp
          i = i // 2
    
    
    def insertar(self, k):
        '''
        Recibe un í­tem como parámetro, lo inserta en la Cola de Prioridad
        y llama al método "infiltArriba".

        Parameters
        ----------
        k : int
            Ítem que se inserta en el Montí­culo.

        Returns
        -------
        None.

        '''
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
    
    
    def infiltAbajo(self, i):
        '''
        Infiltra un Ítem hacia abajo en el Árbol hasta donde 
        sea necesario para mantener la propiedad de montí­culo.

        Parameters
        ----------
        i : int
            Hijo mayor de la raí­z del Montí­culo.

        Returns
        -------
        None.

        '''
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMax(i)    # Hijo 
            if self.listaMonticulo[i][0] < self.listaMonticulo[hm][0]:
                temp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = temp
            i = hm
    
    
    def hijoMax(self, i):
        '''
        Encuentra el Hijo máximo de un í­tem.

        Parameters
        ----------
        i : int
            Posición del padre.

        Returns
        -------
        int
            Retorna el índice donde se encuentra el hijo máximo.

        '''
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2][0] > self.listaMonticulo[i*2+1][0]:
                return i * 2
            else:
                return i * 2 + 1
    
    
    def eliminarMax(self):
        '''
        Elimina el valor máximo de la Cola de Prioridad.
        Gran parte del proceso se realiza 
        cuando se llama al método: "infiltAbajo"

        Returns
        -------
        valorSacado : any type
            Valor máximo de la Cola de Prioridad extraído.

        '''
        valorSacado = self.listaMonticulo[1][1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        
        return valorSacado
    
    def devolverMaximo(self):
        return self.listaMonticulo[1][1]
    
    def decrementarClave(self, valor, nuevaClave):
        hecho = False
        i = 1
        clave = 0
        
        '''Busco cada valor (Vertice)'''
        while not hecho and i <= self.tamanoActual:
            if self.listaMonticulo[i][1] == valor:
                hecho = True
                clave = i
            else:
                i = i + 1
        
        if clave > 0:
            self.listaMonticulo[clave] = (nuevaClave, self.listaMonticulo[clave][1])
            self.infiltArriba(clave)

    def construirMonticulo(self, unaLista):
        '''
        Construye una Cola de Prioridad completa 
        a partir de una lista de claves con su Ponderación.

        Parameters
        ----------
        unaLista : list
            Lista de claves para crear la Cola de Prioridad.

        Returns
        -------
        None.

        '''
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1





'''
==========================================================================================================================
'''





class ColaPrioridadMin:
    '''
    Cola de Prioridad implementada con un Montículo de Mínimos.
    '''
    
    def __init__(self):
        self.listaMonticulo = [(0,0)]
        self.tamanoActual = 0
        self.hijoMin
        
        
    # Métodos Mágicos
    
    def __len__(self):
        '''
        Método mágico que retorna el tamaño de la Cola de Prioridad.

        Returns
        -------
        int
            Entero que representa el tamaño de la Cola de Prioridad.

        '''
        return self.tamanoActual
    
    
    def __iter__(self):
        '''
        Método para iterar la Cola de Prioridad.
        '''
        
        for i in self.listaMonticulo:
            yield i
    
    
    def __str__(self):
        '''
        Retorna todos los elementos de la Cola de Prioridad.

        Returns
        -------
        str
            String con todos los elementos de la Cola de Prioridad.

        '''
        return str(self.listaMonticulo)
    
    def __contains__(self, vertice):
        for par in self.listaMonticulo:
            if par[1] == vertice:
                return True
            return False
    
    # Métodos
    
    def estaVacia(self) -> bool:
        '''
        Comrpueba si la Cola de Prioridad está vacía.

        Returns
        -------
        bool
            Si la Cola de Prioridad no contiene ningún elemento,
            retorna True, si contiene algun elemento, retorna False.

        '''
        return self.tamanoActual == 0
    
    def infiltArriba(self, i):
        '''
        Infiltra un Í­tem hacia arriba en el Árbol hasta donde 
        sea necesario para mantener la propiedad de montí­culo.

        Parameters
        ----------
        i : int
            Tamaño de la Cola de Prioridad.

        Returns
        -------
        None.

        '''
        while i // 2 > 0:
          if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
             temp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = temp
          i = i // 2
    
    
    def insertar(self, k:tuple):
        '''
        Recibe un í­tem como parámetro, lo inserta en la Cola de Prioridad
        y llama al método "infiltArriba".

        Parameters
        ----------
        k : int
            Ítem que se inserta en el Montí­culo.

        Returns
        -------
        None.

        '''
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
    
    
    def infiltAbajo(self, i):
        '''
        Infiltra un Ítem hacia abajo en el Árbol hasta donde 
        sea necesario para mantener la propiedad de montí­culo.

        Parameters
        ----------
        i : int
            Hijo menor de la raí­z del Montí­culo.

        Returns
        -------
        None.

        '''
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)    # Hijo 
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                temp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = temp
            i = hm
    
    
    def hijoMin(self, i):
        '''
        Encuentra el Hijo mínimo de un í­tem.

        Parameters
        ----------
        i : int
            Índice.

        Returns
        -------
        int
            Retorna el índice donde se encuentra el hijo mínimo.

        '''
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2][0] < self.listaMonticulo[i*2+1][0]:
                return i * 2
            else:
                return i * 2 + 1
    
    
    def eliminarMin(self):
        '''
        Elimina el valor mínimo de la Cola de Prioridad.
        Gran parte del proceso se realiza 
        cuando se llama al método: "infiltAbajo"

        Returns
        -------
        valorSacado : any type
            Valor mínimo de la Cola de Prioridad extraído.

        '''
        valorSacado = self.listaMonticulo[1][1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        
        return valorSacado
    
    def devolverMinimo(self):
        return self.listaMonticulo[1][1]
    
    def decrementarClave(self, valor, nuevaClave):
        hecho = False
        i = 1
        clave = 0
        
        '''Busco cada valor (Vertice)'''
        while not hecho and i <= self.tamanoActual:
            if self.listaMonticulo[i][1] == valor:
                hecho = True
                clave = i
            else:
                i = i + 1
        
        if clave > 0:
            self.listaMonticulo[clave] = (nuevaClave, self.listaMonticulo[clave][1])
            self.infiltArriba(clave)

    def construirMonticulo(self, unaLista):
        '''
        Construye una Cola de Prioridad completa 
        a partir de una lista de claves con su Ponderación.

        Parameters
        ----------
        unaLista : list
            Lista de claves para crear la Cola de Prioridad.

        Returns
        -------
        None.

        '''
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1





# Pruebas locales

if __name__ == '__main__':
    
    miColaPrioridad = ColaPrioridadMax()
    miColaPrioridad.construirMonticulo([9,5,6,2,3])
    
    print(miColaPrioridad.eliminarMax())
    print(miColaPrioridad.eliminarMax())
    print(miColaPrioridad.eliminarMax())
    print(miColaPrioridad.eliminarMax())
    print(miColaPrioridad.eliminarMax())