
# Hacer modificaciones finales a los docstrings del montículo y algunas pruebas locales.

class MonticuloBinario:
    
    def __init__(self):
        self.listaMonticulo = ['']
        self.tamanoActual = 0
        self.hijoMin
        
        
    # Métodos Mágicos
    
    def __len__(self):
        '''
        Método mágico que retorna el tamaño del montículo.

        Returns
        -------
        int
            Entero que representa el tamaño del Montículo.

        '''
        return self.tamanoActual
    
    
    def __iter__(self):
        '''
        Método para iterar el Montículo.
        '''
        
        for i in self.listaMonticulo:
            yield i
    
    
    def __str__(self):
        '''
        Retorna todos los elementos del montículo.

        Returns
        -------
        str
            String con todos los elementos del Montículo.

        '''
        return str(self.listaMonticulo)
    
    
    # Métodos
    
    def infilt_arriba(self, i):
        '''
        Infiltra un ítem hacia arriba en el árbol hasta donde 
        sea necesario para mantener la propiedad de montículo.

        Parameters
        ----------
        i : int
            Tamaño del Montículo.

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
        Recibe un ítem como parámetro, lo inserta en el Montículo y llama
        al método "infilt_arriba".

        Parameters
        ----------
        k : int
            Ítem que se inserta en el Montículo.

        Returns
        -------
        None.

        '''
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infilt_arriba(self.tamanoActual)
    
    
    def infilt_abajo(self, i):
        '''
        Infiltra un ítem hacia abajo en el árbol hasta donde 
        sea necesario para mantener la propiedad de montículo.

        Parameters
        ----------
        i : int
            Hijo menor de la raíz del Montículo.

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
        Encuentra el Hijo mínimo de un ítem.

        Parameters
        ----------
        i : int
            DESCRIPTION.

        Returns
        -------
        int
            DESCRIPTION.

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
        Elimina el valor mínimo del Montículo.
        Gran parte del proceso se realiza 
        cuando se llama al método: "infilt_abajo"

        Returns
        -------
        valorSacado : any type
            DESCRIPTION.

        '''
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infilt_abajo(1)
        
        return valorSacado



# Pruebas locales

if __name__ == '__main__':
    None    