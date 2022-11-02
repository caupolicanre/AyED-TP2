import AVL
from datetime import date, time, datetime

class Temperaturas_DB:
    
    def __init__(self):
        self.arbol = AVL.AVL()
    
    def trans_fecha(self, fecha):
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        return fecha
    
    def guardar_temperatura(self, temperatura, fecha):
        self.arbol.agregar(fecha, temperatura)
    
    def devolver_temperatura(self,fecha):
        return self.arbol.obtener(fecha)
    
    def max_temp_rango(self, fecha1, fecha2):
        date1 = self.trans_fecha(fecha1)
        date2 = self.trans_fecha(fecha2)
        max_temp = 0
        iterador = self.Iterador(self.arbol, date1)
        for nodo in iterador:
            if date1 <= nodo <= date2:
                if self.obtener(nodo) > max_temp:
                    max_temp = self.obtener(nodo)
        return max_temp
    
    def min_temp_rango(self, fecha1, fecha2):    
        date1 = self.trans_fecha(fecha1)
        date2 = self.trans_fecha(fecha2)
        iterador = self.Iterador(self.arbol, date1)
        for nodo in iterador:
            if date1 <= nodo <= date2:
                temp_min = AVL.AVL.encontrar_min()
        return temp_min
    
    def temp_extremos_rango(self, fecha1, fecha2):
        date1 = self.trans_fecha(fecha1)
        date2 = self.trans_fecha(fecha2)
        iterador = self.Iterador(self.arbol, date1)
        for nodo in iterador:
            if date1 <= nodo <= date2:
                max_temp = self.max_temp_rango(date1, date2)
                min_temp = self.min_temp_rango(date1, date2)
        return max_temp,min_temp
    
    def borrar_temperatura(self, fecha):
        date1 = self.trans_fecha(fecha)
        AVL.AVL.eliminar(date1)
        
        
    def mostrar_temperaturas(self, fecha1, fecha2):
        date1 = self.trans_fecha(fecha1)
        date2 = self.trans_fecha(fecha2)
        iterador = AVL.Iterador(self.arbol, date1)
        lista = []
        for nodo in iterador:
            if date1 <= nodo <= date2:
                lista.append((nodo,nodo.clave))
        return lista
            
    
    def mostrar_cantidad_muestras(self):
        iterador = self.Iterador(self.arbol,self.raiz)
        contador = 0
        for nodo in iterador:
            contador += 1
        
if __name__ == "__main__":
    obj=Temperaturas_DB()
    obj.guardar_temperatura("20/10/2022",30)
    obj.guardar_temperatura("21/10/2022",27)
    obj.guardar_temperatura("22/10/2022",26)
    obj.guardar_temperatura("23/10/2022",25)
    obj.guardar_temperatura("24/10/2022",23)
    obj.guardar_temperatura("25/10/2022",22)
    obj.guardar_temperatura("26/10/2022",12)
    obj.guardar_temperatura("27/10/2022",3)
    obj.guardar_temperatura("28/10/2022",33)
    print(obj.devolver_temperatura("25/10/2022"))
    print()
    print("MAX",obj.max_temp_rango("20/10/2022", "28/10/2022"))
    print("MIN",obj.min_temp_rango("20/10/2022", "28/10/2022"))
    # obj.borrar_temperatura("25/10/2022")
    print(obj)
    print(obj.temp_extremos_rango("20/10/2022", "28/10/2022"))
    # obj.mostrar_temperaturas("20/10/2022", "28/10/2022")
        
                            
        
        
        