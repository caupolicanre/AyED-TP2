import AVL
from AVL import Iterador
from datetime import date, time, datetime

class Temperaturas_DB:
    
    def __init__(self):
        '''
       Crea el arbol e inicia la variable tamanio en 0.

        '''
        self.arbol = AVL.AVL()
        self.tamanio = 0
        
    
    def trans_fecha(self, fecha):
        '''
        Transforma la fecha de formato string a date.
        
        Parameters
        ----------
        Fecha : string

        Returns
        -------
        Date
            Devuelve la fecha en formato date.

        '''
        fecha = datetime.strptime(fecha, '%d/%m/%Y') 
        return fecha
    
    
    def guardar_temperatura(self, fecha, temperatura):
        '''
        Agrega un nuevo nodo en el arbol con clave igual a "date1" y valor igual a "temperatura".
        
        Parameters
        ----------
        fecha : String
        temperatura : Float
        
        '''
        date1 = self.trans_fecha(fecha)
        self.arbol.agregar(date1, temperatura)
        self.tamanio += 1
        
        
    def devolver_temperatura(self,fecha):
        '''
        
        Parameters
        ----------
        fecha : string

        Returns
        -------
        Float
            Devuelve la temperatura en el nodo que tiene como clave a el valor de "date1".
        '''
        date1 = self.trans_fecha(fecha)
        return self.arbol.obtener(date1)
    
    
    def max_temp_rango(self, fecha1, fecha2):
        '''
        Recorre el arbol entre "fecha1" hasta "fecha2", mientras 
        compara el valor de la carga util de cada nodo y almacenando el mayor.
        
        Parameters
        ----------
        fecha1 : String
        fecha2 : String 
        
        Returns
        -------
        Float
            Devuelve la temperatura maxima entre las dos fechas.
        '''
        date1 = self.trans_fecha(fecha1)
        date2 = self.trans_fecha(fecha2)
        max_temp = 0
        iterador =Iterador(self.arbol, date1)
        for nodo in iterador:
            if  date1 <= nodo.clave <= date2:
                if self.arbol.obtener(nodo.clave) > max_temp:
                    max_temp = self.arbol.obtener(nodo.clave)
        return max_temp
    
    
    def min_temp_rango(self, fecha1, fecha2):  
        '''
        Recorre el arbol entre "fecha1" hasta "fecha2", mientras 
        compara el valor de la carga util de cada nodo y almacenando el menor.
        
        Parameters
        ----------
        fecha1 : String
        fecha2 : String 
        
        Returns
        -------
        Float
            Devuelve la temperatura minima entre las dos fechas.
        '''
        date1 = self.trans_fecha(fecha1)
        date2 = self.trans_fecha(fecha2)
        iterador = Iterador(self.arbol, date1)
        temp_min = self.arbol.obtener(date1)
        for nodo in iterador:
            if date1 <= nodo.clave <= date2:
               if nodo.carga_util < temp_min:
                   temp_min = nodo.carga_util
        return temp_min
    
    
    def temp_extremos_rango(self, fecha1, fecha2):
        '''
        LLama a los modulos "max_temp_rango" y "min_temp_rango".
        
        Parameters
        ----------
        fecha1 : String
        fecha2 : String 
        
        Returns
        -------
        Float
            Devuelve las temperaturas maxima y minima entre las dos fechas.
        '''
        max_temp = self.max_temp_rango(fecha1, fecha2)
        min_temp = self.min_temp_rango(fecha1, fecha2)
        return max_temp, min_temp
    
    '''
    Recibe una fecha y borra la temperatura correspondiente a la fecha
    tambien reduce la variable tamanio en 1
    '''
    def borrar_temperatura(self, fecha):
        '''
        LLama al metodo "eliminar" para "date1" y reduce "tamanio" en -1.
        
        Parameters
        ----------
        fecha1 : String
        fecha2 : String 
        
        '''
        date1 = self.trans_fecha(fecha)
        self.arbol.eliminar(date1)
        self.tamanio -= 1
        
    '''
    Recibe dos fechas y devuelve una lista de tuplas
    las cuales contienen una fecha y su temperatura correspondiente 
    '''
    def mostrar_temperaturas(self, fecha1, fecha2):
        '''
        Agrega a una lista tuplas que contienen (fecha en formato date, temperatura).
        
        Parameters
        ----------
        fecha1 : String
        fecha2 : String 
        
        Returns
        -------
        List
            Devuelve la lista con todas las tuplas.
        '''
        date1 = self.trans_fecha(fecha1)
        date2 = self.trans_fecha(fecha2)
        iterador = AVL.Iterador(self.arbol, date1)
        lista = []
        for nodo in iterador:
            if date1 <= nodo.clave <= date2:
                lista.append((str(nodo.clave.date()),nodo.carga_util))
        return lista
            
    '''
    Muestra la cantidad de nodos en el arbol
    '''
    def mostrar_cantidad_muestras(self):
        '''
        
        Returns
        -------
        Int
            Devuelve el tamaño actual del arbol almacenado en "tamanio".
        '''
        cantidad = self.tamanio
        return cantidad 
        
if __name__ == "__main__":
    obj=Temperaturas_DB()
    obj.guardar_temperatura("20/10/2022",30)
    obj.guardar_temperatura("21/10/2022",27)
    obj.guardar_temperatura("22/10/2022",26)
    obj.guardar_temperatura("23/10/2022",25)
    obj.guardar_temperatura("24/10/2022",23)
    obj.guardar_temperatura("25/10/2022",22)
    obj.guardar_temperatura("26/10/2022",12)
    obj.guardar_temperatura("27/10/2022",33)
    obj.guardar_temperatura("28/10/2022",3)
    
    print(obj.devolver_temperatura("25/10/2022"))
    # print()
    print("MAX",obj.max_temp_rango("20/10/2022", "28/10/2022"))
    print("MIN",obj.min_temp_rango("20/10/2022", "28/10/2022"))
    obj.borrar_temperatura("25/10/2022")
    a=obj.mostrar_cantidad_muestras()
    b=obj.mostrar_temperaturas("20/10/2022","28/10/2022")
    c=obj.devolver_temperatura("21/10/2022")
    print(a)
    print(b)
    print(c)
    print(obj.temp_extremos_rango("20/10/2022", "28/10/2022"))
    obj.mostrar_temperaturas("20/10/2022", "28/10/2022")
    
    
        
        