def rotarDerecha(self,rot_raiz):
    nueva_raiz = rot_raiz.izq
    rot_raiz.izq = nueva_raiz.der
    if rot_raiz.padre!= None:
      self.raiz=nueva_raiz
    else:
        if rot_raiz.es_izq():
            rot_raiz.padre.izq = nueva_raiz
        elif rot_raiz.es_der():
            rot_raiz.padre.der=nueva_raiz()
    nueva_raiz.hijoIzquierdo = rot_raiz
    rot_raiz.padre = nueva_raiz
    rot_raiz.factorEquilibrio = rot_raiz.factorEquilibrio + 1 - min(0,nueva_raiz.factorEquilibrio)
    nueva_raiz.factorEquilibrio = nueva_raiz.factorEquilibrio + 1 + max(0,rot_raiz.factorEquilibrio)