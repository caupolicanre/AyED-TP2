import unittest
from Temperaturas_DB import Temperaturas_DB
class test_temperaturas_db(unittest.TestCase):
    
    def setUp(self):
            self.data = Temperaturas_DB()
            self.nro_temps = 0
            self.fechas = ["27/03/2003","04/04/2003","30/10/2003","14/12/2003","04/12/2003"]
            self.temps = [25,22,29,32,26]
            self.temp_max = 32
            self.temp_min = 22
            self.fecha1 = "27/03/2003"
            self.fecha2 = "14/12/2003"
            self.fecha_y_temp = ("04/04/2003",22)
    
    def test_guardar_devolver_temp(self):
        self.data.guardar_temperatura(self.fechas[0],self.temps[0])
        temp=self.data.devolver_temperatura(self.fechas[0])
        self.assertEqual(temp,self.temps[0])
    
    # def setUp(self):
    #     self.data.guardar_temperatura(self.fechas[0], self.temps[0])
    #     self.data.guardar_temperatura(self.fechas[1], self.temps[1])
    #     self.data.guardar_temperatura(self.fechas[2], self.temps[2])
    #     self.data.guardar_temperatura(self.fechas[3], self.temps[3])

    def test_max_temp_rango(self):
        # t=0
        self.data.guardar_temperatura(self.fechas[0], self.temps[0])
        self.data.guardar_temperatura(self.fechas[1], self.temps[1])
        self.data.guardar_temperatura(self.fechas[2], self.temps[2])
        self.data.guardar_temperatura(self.fechas[3], self.temps[3])
        max_temp=self.data.max_temp_rango(self.fecha1,self.fecha2)
        self.assertEqual(max_temp,self.temp_max)
        
    def test_min_temp_rango(self):
        # t=0
        self.data.guardar_temperatura(self.fechas[0], self.temps[0])
        self.data.guardar_temperatura(self.fechas[1], self.temps[1])
        self.data.guardar_temperatura(self.fechas[2], self.temps[2])
        self.data.guardar_temperatura(self.fechas[3], self.temps[3])
        min_temp=self.data.min_temp_rango(self.fecha1,self.fecha2)
        self.assertEqual(min_temp,self.temp_min )

    def test_extremos_rango(self):
        self.data.guardar_temperatura(self.fechas[0], self.temps[0])
        self.data.guardar_temperatura(self.fechas[1], self.temps[1])
        self.data.guardar_temperatura(self.fechas[2], self.temps[2])
        self.data.guardar_temperatura(self.fechas[3], self.temps[3])
        min_temp=self.data.min_temp_rango(self.fecha1,self.fecha2)
        max_temp=self.data.max_temp_rango(self.fecha1,self.fecha2)
        self.assertEqual(min_temp,self.temp_min)
                    
        
if __name__ == "__main__":
    unittest.main()