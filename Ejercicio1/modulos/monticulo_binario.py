
class MonticuloBinario:
    '''
    Montículo Binario de mínimos.
    Se implementa con un árbol binario completo, es decir,
    un árbol en el que cada nivel tiene todos sus nodos.
    
    Orden de complejidad para inserciones:
        O(n log n) 
    Orden de complejidad para eliminaciones:
        O(n log n) 
    '''    
    
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
        
        
    # Métodos Mágicos
    
    def __len__(self):
        '''
        Método mágico que retorna el tamaño del Montí­culo.

        Returns
        -------
        int
            Entero que representa el tamaño del Montí­culo.

        '''
        return self.tamanoActual
    
    
    def __iter__(self):
        '''
        Método para iterar el Montí­culo.
        '''
        
        for i in self.listaMonticulo:
            yield i
    
    
    def __str__(self):
        '''
        Retorna todos los elementos del Montí­culo.

        Returns
        -------
        str
            String con todos los elementos del Montí­culo.

        '''
        return str(self.listaMonticulo)
    
    
    # Métodos
    
    def infilt_arriba(self, i):
        '''
        Infiltra un ítem hacia arriba en el Árbol hasta donde 
        sea necesario para mantener la propiedad de montí­culo.

        Parameters
        ----------
        i : int
            Recibe como parámetro el tamaño del Montí­culo.
            Luego, se va actualizando con el índice actual del ítem insertado.

        Returns
        -------
        None.

        '''
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:  # Si el Nodo insertado es menor a su padre, los intercambio de posición
                temp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = temp
            i = i // 2  # Actualizo el índice del nodo insertado
    
    
    def insertar(self, k):
        '''
        Recibe un í­tem como parámetro, lo inserta en el Montí­culo y llama
        al método "infilt_arriba".

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
        self.infilt_arriba(self.tamanoActual)
    
    
    def infilt_abajo(self, i):
        '''
        Infiltra un Ítem hacia abajo en el Árbol hasta donde 
        sea necesario para mantener la propiedad de montí­culo.

        Parameters
        ----------
        i : int
            Recibe como parámetro el índice de la raíz del Montículo (1).
            Luego se va modificando con el índice 
            del Hijo menor de la raí­z del Montí­culo.

        Returns
        -------
        None.

        '''
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i) # Hijo Menor
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:    # Si el nodo es mayor a su hijo, los intercambio de posición
                temp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = temp
            i = hm  # Actualizo el índice del nodo
    
    
    def hijoMin(self, i):
        '''
        Encuentra el Hijo mí­nimo de un í­tem.

        Parameters
        ----------
        i : int
            Índice del ítem.

        Returns
        -------
        int
            Índice del hijo mínimo del ítem.

        '''
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                '''Hijo Izquierdo es menor'''
                return i * 2
            else:
                '''Hijo Derecho es menor'''
                return i * 2 + 1
    
    
    def eliminar_min(self):
        '''
        Elimina el valor mí­nimo del Montí­culo (Elemento que se encuentra primero en la lista).
        Gran parte del proceso se realiza 
        cuando se llama al método: "infilt_abajo"

        Returns
        -------
        valorSacado : any type
            Valor mínimo extraído del montículo.

        '''
        valorSacado = self.listaMonticulo[1] # Valor mínimo extraído del montículo (Raíz).
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual] # Actualizo la raíz con el último item de la lista
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infilt_abajo(1) # Restauro la propiedad de montículo, infiltrando hacia abajo el nuevo nodo raiz hasta su posición correcta
        
        return valorSacado