
class ColaPrioridad:
    
    def __init__(self):
        self.listaMonticulo = ['']
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
    
    
    # Métodos
    
    def infilt_arriba(self, i):
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
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             temp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = temp
          i = i // 2
    
    
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
            Hijo menor de la raí­z del Montí­culo.

        Returns
        -------
        None.

        '''
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)    # Hijo 
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                temp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = temp
            i = hm
    
    
    def hijoMin(self, i):
        '''
        Encuentra el Hijo mí­nimo de un í­tem.

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
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    
    def eliminar_min(self):
        '''
        Elimina el valor mí­nimo de la Cola de Prioridad.
        Gran parte del proceso se realiza 
        cuando se llama al método: "infilt_abajo"

        Returns
        -------
        valorSacado : any type
            Valor mínimo de la Cola de Prioridad extraído.

        '''
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infilt_abajo(1)
        
        return valorSacado
    
    
    # Método implementado para realizar pruebas locales
    def construir_monticulo(self, unaLista):
        '''
        Construye una Cola de Prioridad completa 
        a partir de una lista de claves.

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
            self.infilt_abajo(i)
            i = i - 1



# Pruebas locales

if __name__ == '__main__':
    
    miColaPrioridad = ColaPrioridad()
    miColaPrioridad.construir_monticulo([9,5,6,2,3])
    
    print(miColaPrioridad.eliminar_min())
    print(miColaPrioridad.eliminar_min())
    print(miColaPrioridad.eliminar_min())
    print(miColaPrioridad.eliminar_min())
    print(miColaPrioridad.eliminar_min())