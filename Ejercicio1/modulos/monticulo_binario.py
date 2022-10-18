

class MonticuloBinario:
    
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
        self.hijoMin
        
    
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
    
    
    def infilt_arriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2
    
    
    def infilt_abajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
    
    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infilt_arriba(self.tamanoActual)
    
    
    def eliminar_min(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infilt_abajo(1)
        
        return valorSacado



# Pruebas locales

if __name__ == '__main__':
    None    