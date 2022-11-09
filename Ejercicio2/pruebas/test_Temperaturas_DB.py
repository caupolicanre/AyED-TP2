import unittest
from modulos.Temperaturas_DB import Temperaturas_DB
class test_temperaturas_db(unittest.TestCase):
    
    def setUp(self):
            self.data = Temperaturas_DB()
            self.arbol_prueba=Temperaturas_DB()
            self.nro_temps = 4
            self.fechas = ["27/03/2003","04/04/2003","30/10/2003","14/12/2003"]
            self.temps = [25,22,29,32]
            self.fecha_temps=[('2003-03-27',25),('2003-04-04', 22),('2003-10-30', 29),('2003-12-14', 32)]
            self.temp_max = 32
            self.temp_min = 22
            self.fecha1 = "27/03/2003"
            self.fecha2 = "14/12/2003"
            self.data.guardar_temperatura(self.fechas[0], self.temps[0])
            self.data.guardar_temperatura(self.fechas[1], self.temps[1])
            self.data.guardar_temperatura(self.fechas[2], self.temps[2])
            self.data.guardar_temperatura(self.fechas[3], self.temps[3])
    
    def test_guardar_devolver_temp(self):
        self.arbol_prueba.guardar_temperatura(self.fechas[0], self.temps[0])
        temp = self.arbol_prueba.devolver_temperatura(self.fechas[0])
        self.assertEqual(temp, self.temps[0])

    def test_max_temp_rango(self):
        max_temp = self.data.max_temp_rango(self.fecha1, self.fecha2)
        self.assertEqual(max_temp,self.temp_max)
        
    def test_min_temp_rango(self):
        min_temp = self.data.min_temp_rango(self.fecha1, self.fecha2)
        self.assertEqual(min_temp,self.temp_min)

    def test_extremos_rango(self):       
        max_temp,min_temp = self.data.temp_extremos_rango(self.fecha1, self.fecha2)
        self.assertEqual(min_temp, self.temp_min)
        self.assertEqual(max_temp, self.temp_max)
    
    def test_borrar_temp(self):
        self.data.borrar_temperatura(self.fechas[2])
        self.nro_temps = self.data.tamanio
        self.assertEqual(self.nro_temps, 3)
    
    def test_mostrar_temps(self):
        lista = self.data.mostrar_temperaturas(self.fecha1, self.fecha2)
        self.assertEqual(lista,self.fecha_temps)
    
    def test_mostrar_cantidad_muestras(self):
        tamanio=self.data.mostrar_cantidad_muestras()
        self.assertEqual(tamanio, self.nro_temps)
                    
        
if __name__ == "__main__":
    unittest.main()