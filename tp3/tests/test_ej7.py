import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej7 import que_dia_es

class Test_que_dia_es(unittest.TestCase):
    def def_test_que_dia_es_string(self):
        self.assertEqual(que_dia_es("doce"), None)
        self.assertEqual(que_dia_es("18 de noviembre"), None)
        self.assertEqual(que_dia_es("El string de arriba es mi cumple"), None)

    def def_test_que_dia_es_lista(self):
        self.assertEqual(que_dia_es(["18", "noviembre", "2001"]), None)
        self.assertEqual(que_dia_es([1, 2, 3]), None)

    def def_test_que_dia_es_tupla(self):
        self.assertEqual(que_dia_es(("18", "noviembre", "2001")), None)
        self.assertEqual(que_dia_es((1, 2, 3)), None)

    def def_test_que_dia_es_mayor(self):
        self.assertEqual(que_dia_es(367), None)
        self.assertEqual(que_dia_es(128312873), None)
        self.assertEqual(que_dia_es(470), None)

    def def_test_que_dia_es_menor(self):
        self.assertEqual(que_dia_es(0), None)
        self.assertEqual(que_dia_es(-4), None)
        self.assertEqual(que_dia_es(-12837), None)

    def def_test_que_dia_es_float(self):
        self.assertEqual(que_dia_es(2.891372), None)
        self.assertEqual(que_dia_es(1.00000000001), None)
        self.assertEqual(que_dia_es(1.1892377823), None)
        self.assertEqual(que_dia_es(176.12832783), None)

    def def_test_que_dia_es_int(self):
        # Pruebas de lunes
        self.assertEqual(que_dia_es(1), "Lunes")
        self.assertEqual(que_dia_es(8), "Lunes")
        self.assertEqual(que_dia_es(15), "Lunes")
        self.assertEqual(que_dia_es(22), "Lunes")
        self.assertEqual(que_dia_es(29), "Lunes")
        self.assertEqual(que_dia_es(36), "Lunes")
        self.assertEqual(que_dia_es(41), "Lunes")
        self.assertEqual(que_dia_es(48), "Lunes")
        self.assertEqual(que_dia_es(55), "Lunes")
        self.assertEqual(que_dia_es(358), "Lunes")
        # Pruebas de martes
        self.assertEqual(que_dia_es(2), "Martes")
        self.assertEqual(que_dia_es(9), "Martes")
        self.assertEqual(que_dia_es(16), "Martes")
        self.assertEqual(que_dia_es(23), "Martes")
        self.assertEqual(que_dia_es(40), "Martes")
        self.assertEqual(que_dia_es(37), "Martes")
        self.assertEqual(que_dia_es(42), "Martes")
        self.assertEqual(que_dia_es(49), "Martes")
        self.assertEqual(que_dia_es(56), "Martes")
        self.assertEqual(que_dia_es(359), "Martes")
        # Pruebas de miércoles
        self.assertEqual(que_dia_es(3), "Miércoles")
        self.assertEqual(que_dia_es(10), "Miércoles")
        self.assertEqual(que_dia_es(17), "Miércoles")
        self.assertEqual(que_dia_es(24), "Miércoles")
        self.assertEqual(que_dia_es(41), "Miércoles")
        self.assertEqual(que_dia_es(38), "Miércoles")
        self.assertEqual(que_dia_es(43), "Miércoles")
        self.assertEqual(que_dia_es(50), "Miércoles")
        self.assertEqual(que_dia_es(57), "Miércoles")
        self.assertEqual(que_dia_es(360), "Miércoles")
        # Pruebas de jueves
        self.assertEqual(que_dia_es(4), "Jueves")
        self.assertEqual(que_dia_es(11), "Jueves")
        self.assertEqual(que_dia_es(18), "Jueves")
        self.assertEqual(que_dia_es(25), "Jueves")
        self.assertEqual(que_dia_es(42), "Jueves")
        self.assertEqual(que_dia_es(39), "Jueves")
        self.assertEqual(que_dia_es(44), "Jueves")
        self.assertEqual(que_dia_es(51), "Jueves")
        self.assertEqual(que_dia_es(58), "Jueves")
        self.assertEqual(que_dia_es(361), "Jueves")
        # Pruebas de viernes
        self.assertEqual(que_dia_es(4), "Viernes")
        self.assertEqual(que_dia_es(11), "Viernes")
        self.assertEqual(que_dia_es(18), "Viernes")
        self.assertEqual(que_dia_es(25), "Viernes")
        self.assertEqual(que_dia_es(42), "Viernes")
        self.assertEqual(que_dia_es(39), "Viernes")
        self.assertEqual(que_dia_es(44), "Viernes")
        self.assertEqual(que_dia_es(51), "Viernes")
        self.assertEqual(que_dia_es(58), "Viernes")
        self.assertEqual(que_dia_es(362), "Viernes")
        # Pruebas de Sábado
        self.assertEqual(que_dia_es(5), "Sábado")
        self.assertEqual(que_dia_es(12), "Sábado")
        self.assertEqual(que_dia_es(19), "Sábado")
        self.assertEqual(que_dia_es(26), "Sábado")
        self.assertEqual(que_dia_es(43), "Sábado")
        self.assertEqual(que_dia_es(40), "Sábado")
        self.assertEqual(que_dia_es(45), "Sábado")
        self.assertEqual(que_dia_es(52), "Sábado")
        self.assertEqual(que_dia_es(59), "Sábado")
        self.assertEqual(que_dia_es(363), "Sábado")
        # Pruebas de domingo
        self.assertEqual(que_dia_es(6), "Domingo")
        self.assertEqual(que_dia_es(13), "Domingo")
        self.assertEqual(que_dia_es(20), "Domingo")
        self.assertEqual(que_dia_es(27), "Domingo")
        self.assertEqual(que_dia_es(44), "Domingo")
        self.assertEqual(que_dia_es(41), "Domingo")
        self.assertEqual(que_dia_es(46), "Domingo")
        self.assertEqual(que_dia_es(53), "Domingo")
        self.assertEqual(que_dia_es(60), "Domingo")
        self.assertEqual(que_dia_es(364), "Domingo")


unittest.main()