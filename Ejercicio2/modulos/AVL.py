class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tiene_hijo_izquierdo(self):
        '''
        Retorna el Hijo Izquierdo del Nodo actual.

        Returns
        -------
        any type
            Retorna el nodo hijo izquierdo.

        '''
        return self.hijoIzquierdo

    def tiene_hijo_derecho(self):
        '''
        Retorna el Hijo Derecho del Nodo actual.

        Returns
        -------
        any type
            Retorna el nodo hijo derecho.

        '''
        return self.hijoDerecho

    def es_hijo_izquierdo(self):
        '''
        Comprueba si el Nodo actual es un Hijo Izquierdo.

        Returns
        -------
        bool
            Si tiene padre, y el Nodo actual es igual al hijo izquierdo del padre,
            retorna True.

        '''
        return self.padre and self.padre.hijoIzquierdo == self

    def es_hijo_derecho(self):
        '''
        Comprueba si el Nodo actual es un Hijo Derecho.

        Returns
        -------
        bool
            Si tiene padre, y el Nodo actual es igual al hijo derecho del padre,
            retorna True.

        '''
        return self.padre and self.padre.hijoDerecho == self

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
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tiene_algun_hijo(self):
        '''
        Comprueba si el Nodo actual tiene algún hijo.

        Returns
        -------
        bool
            Retorna True si el nodo actual posee un hijo izquierdo y/o derecho.

        '''
        return self.hijoDerecho or self.hijoIzquierdo

    def tiene_ambos_hijos(self):
        '''
        Comprueba si el Nodo actual tiene ambos hijos (derecho e izquierdo).

        Returns
        -------
        bool
            Retorna True si el nodo actual posee un hijo izquierdo y derecho.

        '''
        return self.hijoDerecho and self.hijoIzquierdo

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
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        
        # Si el Nodo tiene hijos, actualizo el padre de éstos
        if self.tiene_hijo_izquierdo():
            self.hijoIzquierdo.padre = self
        if self.tiene_hijo_derecho():
            self.hijoDerecho.padre = self



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

    def _agregar(self, clave, valor, nodoActual):
        '''
        

        Parameters
        ----------
        clave : any ype
            Clave del Nodo a agregar.
        valor : TYPE
            Carga útil que contiene el Nodo a agregar.
        nodoActual : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if clave < nodoActual.clave:
            if nodoActual.tiene_hijo_izquierdo():
                    self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
                    self.actualizar_equilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tiene_hijo_derecho():
                    self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
                    self.actualizar_equilibrio(nodoActual.hijoDerecho)

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
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1
    
            if nodo.padre.factorEquilibrio != 0:
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
        if nodo.factorEquilibrio < 0:
               if nodo.hijoDerecho.factorEquilibrio > 0:
                  self.rotarDerecha(nodo.hijoDerecho)
                  self.rotarIzquierda(nodo)
               else:
                  self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
               if nodo.hijoIzquierdo.factorEquilibrio < 0:
                  self.rotarIzquierda(nodo.hijoIzquierdo)
                  self.rotarDerecha(nodo)
               else:
                  self.rotarDerecha(nodo)
    
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
                   return res.cargaUtil
            else:
                   return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        '''
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.
        nodoActual : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

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

    def __contains__(self,clave):
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
           nodoAEliminar = self._obtener(clave, self.raiz)
           if nodoAEliminar:
               self.remover(nodoAEliminar)
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
                   self.padre.hijoIzquierdo = None
            else:
                   self.padre.hijoDerecho = None
        elif self.tiene_algun_hijo():
            if self.tiene_hijo_izquierdo():
                   if self.es_hijo_izquierdo():
                      self.padre.hijoIzquierdo = self.hijoIzquierdo
                   else:
                      self.padre.hijoDerecho = self.hijoIzquierdo
                   self.hijoIzquierdo.padre = self.padre
            else:
                   if self.es_hijo_izquierdo():
                      self.padre.hijoIzquierdo = self.hijoDerecho
                   else:
                      self.padre.hijoDerecho = self.hijoDerecho
                   self.hijoDerecho.padre = self.padre

    def encontrar_sucesor(self):
        '''
        

        Returns
        -------
        suc : TYPE
            DESCRIPTION.

        '''
        suc = None
        if self.tiene_hijo_derecho():
            suc = self.hijoDerecho.encontrar_min()
        else:
            if self.padre:
                   if self.es_hijo_izquierdo():
                       suc = self.padre
                   else:
                       self.padre.hijoDerecho = None
                       suc = self.padre.encontrar_sucesor()
                       self.padre.hijoDerecho = self
        return suc

    def encontrar_min(self):
        '''
        

        Returns
        -------
        actual : TYPE
            DESCRIPTION.

        '''
        actual = self
        while actual.tiene_hijo_izquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def remover(self, nodoActual):
        '''
        

        Parameters
        ----------
        nodoActual : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if nodoActual.es_hoja(): #hoja
          if nodoActual == nodoActual.padre.hijoIzquierdo:
              nodoActual.padre.hijoIzquierdo = None
          else:
              nodoActual.padre.hijoDerecho = None
        elif nodoActual.tiene_ambos_hijos(): #interior
          suc = nodoActual.encontrar_sucesor()
          suc.empalmar()
          nodoActual.clave = suc.clave
          nodoActual.cargaUtil = suc.cargaUtil

        else: # este nodo tiene un (1) hijo
          if nodoActual.tiene_hijo_izquierdo():
            if nodoActual.es_hijo_izquierdo():
                nodoActual.hijoIzquierdo.padre = nodoActual.padre
                nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
            elif nodoActual.es_hijo_derecho():
                nodoActual.hijoIzquierdo.padre = nodoActual.padre
                nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
            else:
                nodoActual.reemplazar_dato_de_nodo(nodoActual.hijoIzquierdo.clave,
                                   nodoActual.hijoIzquierdo.cargaUtil,
                                   nodoActual.hijoIzquierdo.hijoIzquierdo,
                                   nodoActual.hijoIzquierdo.hijoDerecho)
          else:
            if nodoActual.es_hijo_izquierdo():
                nodoActual.hijoDerecho.padre = nodoActual.padre
                nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
            elif nodoActual.es_hijo_derecho():
                nodoActual.hijoDerecho.padre = nodoActual.padre
                nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
            else:
                nodoActual.reemplazar_dato_de_nodo(nodoActual.hijoDerecho.clave,
                                nodoActual.hijoDerecho.cargaUtil,
                                nodoActual.hijoDerecho.hijoIzquierdo,
                                nodoActual.hijoDerecho.hijoDerecho)
            