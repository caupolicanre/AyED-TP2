from AVL import AVL
from datetime import date, time, datetime

class Temperaturas_DB:
    
    def __init__(self):
        self.arbol = AVL()
    
    def trans_fecha(self,fecha):
        fecha=datetime.strptime(fecha, '%d/%m/%Y')
        return fecha
    def guardar_temperatura(self, temperatura, fecha):
        self.arbol.agregar(fecha, temperatura)
    
    def devolver_temperatura(self,fecha):
        return self.arbol.obtener(fecha)
    
    def max_temp_rango(self,fecha1, fecha2):
        date1=self.trans_fecha(fecha1)
        date2=self.trans_fecha(fecha2)
        lista=[]
        if date1<date2:
            for i in self.arbol:
                if date1<=i<=date2:
                   lista.append(self.arbol.obtener(i))             
                    
        
        
        
        