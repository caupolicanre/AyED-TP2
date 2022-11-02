from datetime import date
class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.carga_util = valor
        self.hijo_izquierdo = izquierdo
        self.hijo_derecho = derecho
        self.padre = padre
        self.factor_equilibrio = 0
        
    def __str__(self):
        lista=[]
        for nodo in self.mediciones:
            lista.append([(nodo.clave.date()), nodo.carga_util])
        return str(lista)

    def tiene_hijo_izquierdo(self):
        '''
        Retorna el Hijo Izquierdo del Nodo actual.

        Returns
        -------
        any type
            Retorna el nodo hijo izquierdo.

        '''
        return self.hijo_izquierdo

    def tiene_hijo_derecho(self):
        '''
        Retorna el Hijo Derecho del Nodo actual.

        Returns
        -------
        any type
            Retorna el nodo hijo derecho.

        '''
        return self.hijo_derecho

    def es_hijo_izquierdo(self):
        '''
        Comprueba si el Nodo actual es un Hijo Izquierdo.

        Returns
        -------
        bool
            Si tiene padre, y el Nodo actual es igual al hijo izquierdo del padre,
            retorna True.

        '''
        return self.padre and self.padre.hijo_izquierdo == self

    def es_hijo_derecho(self):
        '''
        Comprueba si el Nodo actual es un Hijo Derecho.

        Returns
        -------
        bool
            Si tiene padre, y el Nodo actual es igual al hijo derecho del padre,
            retorna True.

        '''
        return self.padre and self.padre.hijo_derecho == self

    def es_raiz(self):
        '''
        Comprueba si el Nodo actual es la Raíz.

        Returns
        -------
        bool
            Si el nodo actual no tiene padre, retorna True.

        '''
        return not self.padre

    def es_hoja(self):
        '''
        Comprueba si el Nodo actual es una hoja (o sea, si no tiene hijos).

        Returns
        -------
        bool
            Si no tiene hijo derecho o izquierdo retorna True.

        '''
        return not (self.hijo_derecho or self.hijo_izquierdo)

    def tiene_algun_hijo(self):
        '''
        Comprueba si el Nodo actual tiene algún hijo.

        Returns
        -------
        bool
            Retorna True si el nodo actual posee un hijo izquierdo y/o derecho.

        '''
        return self.hijo_derecho or self.hijo_izquierdo

    def tiene_ambos_hijos(self):
        '''
        Comprueba si el Nodo actual tiene ambos hijos (derecho e izquierdo).

        Returns
        -------
        bool
            Retorna True si el nodo actual posee un hijo izquierdo y derecho.

        '''
        return self.hijo_derecho and self.hijo_izquierdo

    def reemplazar_dato_de_nodo(self, clave, valor, hizq, hder):
        '''
        

        Parameters
        ----------
        clave : any type
            Clave nueva que va a reemplazar la actual.
        valor : any type
            Carga útil que va a reemplazar la actual.
        hizq : reference
            Hijo izquierdo que va a reemplazar al actual.
        hder : reference
            Hijo derecho que va a reemplazar al actual.

        Returns
        -------
        None.

        '''
        # Actualizo properties del Nodo
        self.clave = clave
        self.carga_util = valor
        self.hijo_izquierdo = hizq
        self.hijo_derecho = hder
        
        # Si el Nodo tiene hijos, actualizo el padre de éstos
        if self.tiene_hijo_izquierdo():
            self.hijo_izquierdo.padre = self
        if self.tiene_hijo_derecho():
            self.hijo_derecho.padre = self
        
    def encontrar_sucesor(self):
            '''
            

            Returns
            -------
            suc : TYPE
                DESCRIPTION.

            '''
            suc = None
            if self.tiene_hijo_derecho():
                suc = self.hijo_derecho.encontrar_min()
            else:
                if self.padre:
                       if self.es_hijo_izquierdo():
                           suc = self.padre
                       else:
                           self.padre.hijo_derecho = None
                           suc = self.padre.encontrar_sucesor()
                           self.padre.hijo_derecho = self
            return suc



class AVL:

    def __init__(self):
        self.raiz = None
        self.tamano = 0     # Contador del tamaño del Árbol

    def longitud(self):
        '''
        Retorna la longitud del Árbol.

        Returns
        -------
        int
            Entero que representa el tamaño del árbol.

        '''
        return self.tamano

    def __len__(self):
        '''
        Método mágico que retorna el tamaño del Árbol.

        Returns
        -------
        int
            Entero que representa el tamaño del árbol.

        '''
        return self.tamano

    def agregar(self, clave, valor):
        '''
        Si el árbol no está vacío (Tiene raíz), llama al método
        "_agregar". Si el árbol está vacío, crea un nuevo Nodo,
        actualiza la raíz, y aumenta el contador del tamaño.

        Parameters
        ----------
        clave : any type
            Clave del Nodo a agregar.
        valor : any type
            Carga útil que contiene el Nodo a agregar.

        Returns
        -------
        None.

        '''
        if self.raiz:
            '''
            El Árbol tiene raíz (No está vacío).
            '''
            self._agregar(clave, valor, self.raiz)
            
        else:
            '''
            El Árbol no tiene raíz (Está vacío).
            '''
            self.raiz = NodoArbol(clave, valor) # Crea un nuevo Nodo y actualiza la raíz con éste
        
        self.tamano = self.tamano + 1   # Aumento el tamaño del árbol

    def _agregar(self, clave, valor, nodo_actual):
        '''
        

        Parameters
        ----------
        clave : any ype
            Clave del Nodo a agregar.
        valor : TYPE
            Carga útil que contiene el Nodo a agregar.
        nodo_actual : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if clave < nodo_actual.clave:
            if nodo_actual.tiene_hijo_izquierdo():
                    self._agregar(clave, valor, nodo_actual.hijo_izquierdo)
            else:
                    nodo_actual.hijo_izquierdo = NodoArbol(clave, valor, padre=nodo_actual)
                    self.actualizar_equilibrio(nodo_actual.hijo_izquierdo)
        else:
            if nodo_actual.tiene_hijo_derecho():
                    self._agregar(clave, valor, nodo_actual.hijo_derecho)
            else:
                    nodo_actual.hijo_derecho = NodoArbol(clave, valor, padre=nodo_actual)
                    self.actualizar_equilibrio(nodo_actual.hijo_derecho)
    
    def rotar_izquierda(self, rot_raiz):
        nueva_raiz = rot_raiz.hijo_derecho
        rot_raiz.hijo_derecho = nueva_raiz.hijo_izquierdo
        if nueva_raiz.hijo_izquierdo != None:
            nueva_raiz.hijo_izquierdo.padre = rot_raiz
        nueva_raiz.padre = rot_raiz.padre
        if rot_raiz.es_raiz():
            self.raiz = nueva_raiz
        else:
            if rot_raiz.es_hijo_izquierdo():
                    rot_raiz.padre.hijo_izquierdo = nueva_raiz
            else:
                rot_raiz.padre.hijo_derecho = nueva_raiz
        nueva_raiz.hijo_izquierdo = rot_raiz
        rot_raiz.padre = nueva_raiz
        rot_raiz.factor_equilibrio = rot_raiz.factor_equilibrio + 1 - min(nueva_raiz.factor_equilibrio, 0)
        nueva_raiz.factor_equilibrio = nueva_raiz.factor_equilibrio + 1 + max(rot_raiz.factor_equilibrio, 0)
    
    def rotar_derecha(self, rot_raiz):
        nueva_raiz = rot_raiz.hijo_izquierdo
        rot_raiz.hijo_izquierdo = nueva_raiz.hijo_derecho
        
        if rot_raiz.padre!= None:
          self.raiz = nueva_raiz
        else:
            if rot_raiz.es_hijo_izquierdo():
                rot_raiz.padre.izq = nueva_raiz
            elif rot_raiz.es_hijo_derecho():
                rot_raiz.padre.der = nueva_raiz
        nueva_raiz.hijo_izquierdo = rot_raiz
        rot_raiz.padre = nueva_raiz
        rot_raiz.factor_equilibrio = rot_raiz.factor_equilibrio - 1 - max(0,nueva_raiz.factor_equilibrio)
        nueva_raiz.factor_equilibrio = nueva_raiz.factor_equilibrio - 1 + min(0,rot_raiz.factor_equilibrio)
    

    def actualizar_equilibrio(self, nodo):
        '''
        

        Parameters
        ----------
        nodo : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if nodo.factor_equilibrio > 1 or nodo.factor_equilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.es_hijo_izquierdo():
                    nodo.padre.factor_equilibrio += 1
            elif nodo.es_hijo_derecho():
                    nodo.padre.factor_equilibrio -= 1
    
            if nodo.padre.factor_equilibrio != 0:
                    self.actualizar_equilibrio(nodo.padre)
    
    def reequilibrar(self,nodo):
        '''
        

        Parameters
        ----------
        nodo : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if nodo.factor_equilibrio < 0:
               if nodo.hijo_derecho.factor_equilibrio > 0:
                  self.rotar_derecha(nodo.hijo_derecho)
                  self.rotar_izquierda(nodo)
               else:
                  self.rotar_izquierda(nodo)
        elif nodo.factor_equilibrio > 0:
               if nodo.hijo_izquierdo.factor_equilibrio < 0:
                  self.rotar_izquierda(nodo.hijo_izquierdo)
                  self.rotar_derecha(nodo)
               else:
                  self.rotar_derecha(nodo)
    
    def __setitem__(self, c, v):
        '''
        Llama al método "agregar".

        Parameters
        ----------
        c : TYPE
            DESCRIPTION.
        v : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.agregar(c, v)

    def obtener(self, clave):
        '''
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                   return res.carga_util
            else:
                   return None
        else:
            return None

    def _obtener(self, clave, nodo_actual):
        '''
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.
        nodo_actual : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if not nodo_actual:
            return None
        elif nodo_actual.clave == clave:
            return nodo_actual
        elif clave < nodo_actual.clave:
            return self._obtener(clave, nodo_actual.hijo_izquierdo)
        else:
            return self._obtener(clave, nodo_actual.hijo_derecho)

    def __getitem__(self, clave):
        '''
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return self.obtener(clave)

    def __contains__(self, clave):
        '''
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        '''
        if self._obtener(clave, self.raiz):
            return True
        else:
            return False

    def eliminar(self, clave):
        '''
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.

        Raises
        ------
        KeyError
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if self.tamano > 1:
           nodo_a_eliminar = self._obtener(clave, self.raiz)
           if nodo_a_eliminar:
               self.remover(nodo_a_eliminar)
               self.tamano = self.tamano-1
           else:
               raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
           self.raiz = None
           self.tamano = self.tamano - 1
        else:
           raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self, clave):
        '''
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.eliminar(clave)

    def empalmar(self):
        '''
        

        Returns
        -------
        None.

        '''
        if self.es_hoja():
            if self.es_hijo_izquierdo():
                   self.padre.hijo_izquierdo = None
            else:
                   self.padre.hijo_derecho = None
        elif self.tiene_algun_hijo():
            if self.tiene_hijo_izquierdo():
                   if self.es_hijo_izquierdo():
                      self.padre.hijo_izquierdo = self.hijo_izquierdo
                   else:
                      self.padre.hijo_derecho = self.hijo_izquierdo
                   self.hijo_izquierdo.padre = self.padre
            else:
                   if self.es_hijo_izquierdo():
                      self.padre.hijo_izquierdo = self.hijo_derecho
                   else:
                      self.padre.hijo_derecho = self.hijo_derecho
                   self.hijo_derecho.padre = self.padre

   

    def encontrar_min(self):
        '''
        

        Returns
        -------
        actual : TYPE
            DESCRIPTION.

        '''
        actual = self
        while actual.tiene_hijo_izquierdo():
            actual = actual.hijo_izquierdo
        return actual

    def remover(self, nodo_actual):
        '''
        

        Parameters
        ----------
        nodo_actual : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if nodo_actual.es_hoja(): #hoja
          if nodo_actual == nodo_actual.padre.hijo_izquierdo:
              nodo_actual.padre.hijo_izquierdo = None
          else:
              nodo_actual.padre.hijo_derecho = None
        elif nodo_actual.tiene_ambos_hijos(): #interior
          suc = nodo_actual.encontrar_sucesor()
          suc.empalmar()
          nodo_actual.clave = suc.clave
          nodo_actual.carga_util = suc.carga_util

        else: # este nodo tiene un (1) hijo
          if nodo_actual.tiene_hijo_izquierdo():
            if nodo_actual.es_hijo_izquierdo():
                nodo_actual.hijo_izquierdo.padre = nodo_actual.padre
                nodo_actual.padre.hijo_izquierdo = nodo_actual.hijo_izquierdo
            elif nodo_actual.es_hijo_derecho():
                nodo_actual.hijo_izquierdo.padre = nodo_actual.padre
                nodo_actual.padre.hijo_derecho = nodo_actual.hijo_izquierdo
            else:
                nodo_actual.reemplazar_dato_de_nodo(nodo_actual.hijo_izquierdo.clave,
                                   nodo_actual.hijo_izquierdo.carga_util,
                                   nodo_actual.hijo_izquierdo.hijo_izquierdo,
                                   nodo_actual.hijo_izquierdo.hijo_derecho)
          else:
            if nodo_actual.es_hijo_izquierdo():
                nodo_actual.hijo_derecho.padre = nodo_actual.padre
                nodo_actual.padre.hijo_izquierdo = nodo_actual.hijo_derecho
            elif nodo_actual.es_hijo_derecho():
                nodo_actual.hijo_derecho.padre = nodo_actual.padre
                nodo_actual.padre.hijo_derecho = nodo_actual.hijo_derecho
            else:
                nodo_actual.reemplazar_dato_de_nodo(nodo_actual.hijo_derecho.clave,
                                nodo_actual.hijo_derecho.carga_util,
                                nodo_actual.hijo_derecho.hijo_izquierdo,
                                nodo_actual.hijo_derecho.hijo_derecho)
    
class Iterador:
    
    def __init__(self, arbol, inicio):
        self.inicio = arbol._obtener(inicio, arbol.raiz)
        
    def __next__(self):
        nodoSalida = self.inicio
        self.inicio =self.inicio.encontrar_sucesor()
        if self.inicio== None:
            raise StopIteration
        return nodoSalida
             
    def __iter__(self):
        return self
             
if __name__ == "__main__":
    mediciones = AVL()
    mediciones.agregar(date(2021,11,9),23)
    mediciones.agregar(date(2022,10,21),24)
    mediciones.agregar(date(2022,12,11),19)
    mediciones.agregar(date(2022,12,1),18)
    mediciones.agregar(date(2021,3,13),16)    
    mediciones.agregar(date(2019,4,19),11)                  
    print(mediciones.tamano)
    print(mediciones.raiz.clave)

    
    # for nodo in mediciones:
    #     print (nodo.clave, nodo.clave)