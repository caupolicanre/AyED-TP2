class MonticuloBinario:
    '''
    Mont�culo Binario de m�nimos.
    Se implementa con un �rbol binario completo, es decir,
    un �rbol en el que cada nivel tiene todos sus nodos.
    
    Orden de complejidad para inserciones:
        O(n log n) 
    Orden de complejidad para eliminaciones:
        O(n log n) 
    '''    
    
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
        
        
    # M�todos M�gicos
    
    def __len__(self):
        '''
        M�todo m�gico que retorna el tama�o del Mont��culo.

        Returns
        -------
        int
            Entero que representa el tama�o del Mont��culo.

        '''
        return self.tamanoActual
    
    
    def __iter__(self):
        '''
        M�todo para iterar el Mont��culo.
        '''
        
        for i in self.listaMonticulo:
            yield i
    
    
    def __str__(self):
        '''
        Retorna todos los elementos del Mont��culo.

        Returns
        -------
        str
            String con todos los elementos del Mont��culo.

        '''
        return str(self.listaMonticulo)
    
    
    # M�todos
    
    def infilt_arriba(self, i):
        '''
        Infiltra un �tem hacia arriba en el �rbol hasta donde 
        sea necesario para mantener la propiedad de mont��culo.

        Parameters
        ----------
        i : int
            Recibe como par�metro el tama�o del Mont��culo.
            Luego, se va actualizando con el �ndice actual del �tem insertado.

        Returns
        -------
        None.

        '''
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:  # Si el Nodo insertado es menor a su padre, los intercambio de posici�n
                temp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = temp
            i = i // 2  # Actualizo el �ndice del nodo insertado
    
    
    def insertar(self, k):
        '''
        Recibe un ��tem como par�metro, lo inserta en el Mont��culo y llama
        al m�todo "infilt_arriba".

        Parameters
        ----------
        k : int
            ͍tem que se inserta en el Mont��culo.

        Returns
        -------
        None.

        '''
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infilt_arriba(self.tamanoActual)
    
    
    def infilt_abajo(self, i):
        '''
        Infiltra un �tem hacia abajo en el �rbol hasta donde 
        sea necesario para mantener la propiedad de mont��culo.

        Parameters
        ----------
        i : int
            Recibe como par�metro el �ndice de la ra�z del Mont�culo (1).
            Luego se va modificando con el �ndice 
            del Hijo menor de la ra��z del Mont��culo.

        Returns
        -------
        None.

        '''
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i) # Hijo Menor
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:    # Si el nodo es mayor a su hijo, los intercambio de posici�n
                temp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = temp
            i = hm  # Actualizo el �ndice del nodo
    
    
    def hijoMin(self, i):
        '''
        Encuentra el Hijo m��nimo de un ��tem.

        Parameters
        ----------
        i : int
            �ndice del �tem.

        Returns
        -------
        int
            �ndice del hijo m�nimo del �tem.

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
        Elimina el valor m��nimo del Mont��culo (Elemento que se encuentra primero en la lista).
        Gran parte del proceso se realiza 
        cuando se llama al m�todo: "infilt_abajo"

        Returns
        -------
        valorSacado : any type
            Valor m�nimo extra�do del mont�culo.

        '''
        valorSacado = self.listaMonticulo[1] # Valor m�nimo extra�do del mont�culo (Ra�z).
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual] # Actualizo la ra�z con el �ltimo item de la lista
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infilt_abajo(1) # Restauro la propiedad de mont�culo, infiltrando hacia abajo el nuevo nodo raiz hasta su posici�n correcta
        
        return valorSacado