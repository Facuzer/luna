import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej4 import distancia_centro, mayor_numero_de_tres 
# Aviso, lo hable con fede y me dijo que testee solamente las dos funciones,
# no hace falta testear la interacción entre las mismas.


class Test_distancia_centro(unittest.TestCase):
    def test_distancia_centro_int(self):
        self.assertEqual(distancia_centro(4), None)
        self.assertEqual(distancia_centro(1.23872), None)
    
    def test_distancia_centro_float(self):
        self.assertEqual(distancia_centro(4.238728), None)
        self.assertEqual(distancia_centro(0.0000000111), None)
    
    def test_distancia_centro_string(self):
        self.assertEqual(distancia_centro("Hola fede"), None)
        self.assertEqual(distancia_centro("15"), None)
    
    def test_distancia_centro_tupla(self):
        self.assertEqual(distancia_centro((1,2,3,4,5)), None)

    def test_distancia_centro_valores_string(self):
        self.assertEqual(distancia_centro(["12", "15"]), None)
        self.assertEqual(distancia_centro(["15",1]), None)
        self.assertEqual(distancia_centro([1,"15"]), None)

    def test_distancia_centro_valores_int(self):
        self.assertEqual(distancia_centro([1, 1]), 1.4142135623730951)
        self.assertEqual(distancia_centro([100, 7]), 100.24470060806208)
        self.assertEqual(distancia_centro([20, 25]), 32.01562118716424)
        self.assertEqual(distancia_centro([23123, 989]), 23144.140727190545)
        self.assertEqual(distancia_centro([87878, 3434]), 87945.06944678593)


    def test_distancia_centro_valores_float(self):
        self.assertEqual(distancia_centro([13123.2313, 333.3333]),
                                          13127.463991273737)
        self.assertEqual(distancia_centro([0.000001, 328932.2]), 328932.2)
        self.assertEqual(distancia_centro([0.0128937283, 1.127836]),
                                          1.127909699898655)
        self.assertEqual(distancia_centro([4.5, 3.2]), 5.52177507691141)
        self.assertEqual(distancia_centro([1.1, 1.2]), 1.6278820596099708)
        


class Test_mayor_numero_de_tres(unittest.TestCase):
    def test_mayor_numero_de_tres_string(self):
        self.assertEqual(mayor_numero_de_tres("1", 2, 3), None)
        self.assertEqual(mayor_numero_de_tres("1", "2", 3), None)
        self.assertEqual(mayor_numero_de_tres("1", 2, "3"), None)
        self.assertEqual(mayor_numero_de_tres(1, "2", 3), None)
        self.assertEqual(mayor_numero_de_tres(1, "2", "3"), None)    
    def test_mayor_numero_de_tres_lista(self):
        self.assertEqual(mayor_numero_de_tres([1, 2, 3], [1, 2], [1, 2]), 
                                              None)

    def test_mayor_numero_de_tres_tupla(self):
         self.assertEqual(mayor_numero_de_tres((1, 2, 3), (1, 2), (1, 2)), 
                                              None)       

    def test_mayor_numero_de_tres_int(self):
        self.assertEqual(mayor_numero_de_tres(1, 2, 3), "3")
        self.assertEqual(mayor_numero_de_tres(1, 3, 2), "2")
        self.assertEqual(mayor_numero_de_tres(3, 2, 1), "1")
        self.assertEqual(mayor_numero_de_tres(3, 3, 1), "1 = 2")
        self.assertEqual(mayor_numero_de_tres(3, 2, 3), "1 = 3")
        self.assertEqual(mayor_numero_de_tres(1, 3, 3), "2 = 3")
        self.assertEqual(mayor_numero_de_tres(3, 3, 3), "1 = 2 = 3")



    def test_mayor_numero_de_tres_float(self):
        self.assertEqual(mayor_numero_de_tres(1.123, 2.12312, 3.12312), "3")
        self.assertEqual(mayor_numero_de_tres(1.123, 3.1231, 2.213), "2")
        self.assertEqual(mayor_numero_de_tres(3.123, 2.123123, 1.1231), "1")
        self.assertEqual(mayor_numero_de_tres(3.123, 3.123, 1.123), "1 = 2")
        self.assertEqual(mayor_numero_de_tres(3.123, 2.123, 3.123), "1 = 3")
        self.assertEqual(mayor_numero_de_tres(1.123, 3.321, 3.321), "2 = 3")
        self.assertEqual(mayor_numero_de_tres(3.1, 3.1, 3.1), "1 = 2 = 3")


unittest.main()