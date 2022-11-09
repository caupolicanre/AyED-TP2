from datetime import date
class Nodo_arbol:
   
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.carga_util = valor
        self.hijo_izquierdo = izquierdo
        self.hijo_derecho = derecho
        self.padre = padre
        self.factor_equilibrio = 0
        
    

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
            suc : Nodo

            '''
            suc = None
            if self.tiene_hijo_derecho():
                '''
                Si el nodo tiene un hijo derecho, el sucesor es la clave más pequeña en el subárbol derecho.
                '''
                suc = self.hijo_derecho.encontrar_min()
            else:
                if self.padre:
                       if self.es_hijo_izquierdo():
                           '''
                           Si el nodo no tiene hijo derecho y es el hijo izquierdo de su padre, el padre es el sucesor.
                           '''
                           suc = self.padre
                       else:
                           '''
                           Si el nodo es el hijo derecho de su padre, y no tiene hijo derecho, 
                           entonces el sucesor de este nodo es el sucesor de su padre, excluyendo este nodo.
                           '''
                           self.padre.hijo_derecho = None
                           suc = self.padre.encontrar_sucesor()
                           self.padre.hijo_derecho = self
            return suc
        

    def encontrar_min(self):
        '''
        Toma el hijo del nodo de un nodo repetitivamente hasta que el nodo en el que esta no tenga hijo izquierdo

        Returns
        -------
        actual : Nodo_Arbol
            DESCRIPTION.

        '''
        actual = self
        while actual.tiene_hijo_izquierdo():
            actual = actual.hijo_izquierdo
        return actual
    
    
    def empalmar(self):
        '''
        Elimina el sucesor del nodo

        Returns
        -------
        None.

        '''
        if self.es_hoja():
            if self.es_hijo_izquierdo():
                '''
                Si el nodo es hoja y a su vez es hijo izquierdo el padre de este nodo va a ser None
                '''
                self.padre.hijo_izquierdo = None
            else:
                '''
                Hace None al padre
                '''
                self.padre.hijo_derecho = None
        elif self.tiene_algun_hijo():
            '''
            Si el nodo tiene un hijo transforma conecta a su nodo hijo derecho o izquierdo con su nodo padre
            '''
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


class AVL:

    def __init__(self):
        self.raiz = None
        self.tamano = 0     # Contador del tamaño del Árbol
        
    
    def __getitem__(self, clave):
        '''
       Llama al metodo "obtener"
        Parameters
        ----------
        clave : Any type

        Returns
        -------
        Any type
            Devuelve el valor almacenado en la carga util del nodo 

        '''
        return self.obtener(clave)
    
    
    def __len__(self):
        '''
        Método mágico que retorna el tamaño del Árbol.

        Returns
        -------
        int
            Entero que representa el tamaño del árbol.

        '''
        return self.tamano
    
    
    def __setitem__(self, c, v):
        '''
        Llama al método "agregar".

        Parameters
        ----------
        c : Clave del Nodo, en este caso es la fecha
        v : Valor almacenado en el nodo, en este caso es la temperatura

        Returns
        -------
        None.

        '''
        self.agregar(c, v)
        
        
    def __contains__(self, clave):
        '''
        Llama al metodo "obtener".

        Parameters
        ----------
        clave : Date
                Fecha en formato Date.

        Returns
        -------
        bool
            Devuelve True si "obtener" devuelve un valor o False si devuelve None.

        '''
        if self._obtener(clave, self.raiz):
            return True
        else:
            return False
        
        
    def __delitem__(self, clave):
        '''
        Llama al metodo "eliminar"

        Parameters
        ----------
        clave : Date
                Fecha en formato Date.

        Returns
        -------
        None.

        '''
        self.eliminar(clave)
        
    
    def longitud(self):
        '''
        Retorna la longitud del Árbol.

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
        clave : 
            Clave del Nodo a agregar.
        valor : 
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
            self.raiz = Nodo_arbol(clave, valor) # Crea un nuevo Nodo y actualiza la raíz con éste
        
        self.tamano = self.tamano + 1   # Aumento el tamaño del árbol
        

    def _agregar(self, clave, valor, nodo_actual):
        '''
        Mientras busca compara la clave recibida con la clave del nodo actual y las compara
        dependiendo de el resultado de la comparacion es donde se va a agregar el nuevo nodo

        Parameters
        ----------
        clave : 
            Clave del Nodo a agregar.
        valor : 
            Carga útil que contiene el Nodo a agregar.
        nodo_actual : 
            Posicion en la que se va a agrega el nuevo nodo

        Returns
        -------
        None.

        '''
        if clave < nodo_actual.clave:
            '''
            Si la nueva clave es menor que el nodo actual, buscar en el subárbol izquierdo.
            '''
            if nodo_actual.tiene_hijo_izquierdo():
                    self._agregar(clave, valor, nodo_actual.hijo_izquierdo)
            else:
                '''
                Crea un nuevo nodo y lo inserta en la posicion actual
                '''
                nodo_actual.hijo_izquierdo = Nodo_arbol(clave, valor, padre=nodo_actual)
                self.actualizar_equilibrio(nodo_actual.hijo_izquierdo)
        else:
            '''
            Si la nueva clave es mayor que el nodo actual, buscar en el subárbol derecho.
            '''
            if nodo_actual.tiene_hijo_derecho():
                    self._agregar(clave, valor, nodo_actual.hijo_derecho)
            else:
                '''
                Crea un nuevo nodo y lo inserta en la posicion actual
                '''
                nodo_actual.hijo_derecho = Nodo_arbol(clave, valor, padre=nodo_actual)
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
        Comprueba si el nodo actual está lo suficientemente desequilibrado como para requerir el reequilibrio.

        Parameters
        ----------
        nodo : Nodo_arbol

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
        nodo : Nodo_arbol

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
    
   
    def obtener(self, clave):
        '''
        Recorre el arbol en forma recursiva hasta que llega a un nodo hoja no coincidente 
        o encuentra la clave recibida y devuelve el valor guardado en la carga util del nodo
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
        Llama al método "agregar".

        Parameters
        ----------
        c : Date
            Clave del Nodo, Fecha en formato Date.
        v : Float
            Valor almacenado en el nodo, Temperatura en Int

        Returns
        -------
        None.

        '''
        if not nodo_actual:
            return None
        elif nodo_actual.clave == clave:
            return nodo_actual
        elif clave < nodo_actual.clave:
            return self._obtener(clave, nodo_actual.hijo_izquierdo)
        else:
            return self._obtener(clave, nodo_actual.hijo_derecho)
        
    
    def eliminar(self, clave):
        '''
        Busca en el árbol el nodo que se va a eliminar. 
        
        Parameters
        ----------
        clave : Date
                Fecha en formato Date.
        Raises
        ------
        KeyError
            No se encuentra la clave debido a que el arbol es solo un nodo

        Returns
        -------
        None.

        '''
        if self.tamano > 1:           
            '''
            Si el árbol tiene más de un nodo, buscamos usando el método "_obtener" para encontrar el NodoArbol que debe ser eliminado. 
            '''
            nodo_a_eliminar = self._obtener(clave, self.raiz)
            if nodo_a_eliminar:
               self.remover(nodo_a_eliminar)
               self.tamano = self.tamano-1
            else:
               raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            '''
            Si el árbol tiene un solo nodo, eliminamos la raíz del árbol, 
            se comprueba que la clave de la raíz sea igual a la clave que se va a eliminar.
            '''
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            '''
            Si no se encuentra la clave, el operador del genera un error.
            '''
            raise KeyError('Error, la clave no está en el árbol')

    


    def remover(self, nodo_actual):
        '''
        

        Parameters
        ----------
        nodo_actual : Nodo_Arbol

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
        if self.inicio== None:
            raise StopIteration
        self.inicio =self.inicio.encontrar_sucesor()
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
    #     print (nodo.clave, nodo_actual.clave)