import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej9 import evaluar_examenes, calcular_porcentaje, calcular_si_aprobo


class Test_evaluar_examenes(unittest.TestCase):
    def test_evaluar_examenes_string(self):
        self.assertEqual(evaluar_examenes("Hola", "Fede"), None)
        self.assertEqual(evaluar_examenes("Diez", "Veinte"), None)
        self.assertEqual(evaluar_examenes(10, "Veinte"), None)
        self.assertEqual(evaluar_examenes("Diez", 20), None)
        self.assertEqual(evaluar_examenes("Doce", "Trece"), None)

    def test_evaluar_examenes_lista(self):
        self.assertEqual(evaluar_examenes([1, 2, 3, 4], [1, 2, 3]), None)

    def test_evaluar_examenes_tupla(self):
        self.assertEqual(evaluar_examenes((1, 2, 3, 4), (1, 2, 3)), None)
        
    def test_evaluar_examenes_float(self):
        self.assertEqual(evaluar_examenes(1.5, 65), None)
        self.assertEqual(evaluar_examenes(123.123333, 65.5), None)


class Test_calcular_porcentaje(unittest.TestCase):
    def test_calcular_porcentaje_string(self):
        self.assertEqual(calcular_porcentaje("Hola", "Fede"), None)
        self.assertEqual(calcular_porcentaje("Diez", "Veinte"), None)
        self.assertEqual(calcular_porcentaje(10, "Veinte"), None)
        self.assertEqual(calcular_porcentaje("Diez", 20), None)

    def test_calcular_porcentaje_lista(self):
        self.assertEqual(calcular_porcentaje([1, 2, 3], [1, 2]), None)

    def test_calcular_porcentaje_tupla(self):
        self.assertEqual(calcular_porcentaje((1, 2, 3), (1, 2)), None)        
    
    def test_calcular_porcentaje_float(self):
        self.assertEqual(calcular_porcentaje(1.5, 2.5), None)
        self.assertEqual(calcular_porcentaje(1, 2.5), None)
        self.assertEqual(calcular_porcentaje(1.5, 2), None)

    def test_calcular_porcentaje_dar_mayor(self):
        self.assertEqual(calcular_porcentaje(20, 10), None)

    def test_calcular_porcentaje_dar_asterisco(self):
        self.assertEqual(calcular_porcentaje("*", 2), "*")

    def test_calcular_porcentaje_int(self):
        self.assertEqual(calcular_porcentaje(1, 1), 100)
        self.assertEqual(calcular_porcentaje(9, 10), 90)
        self.assertEqual(calcular_porcentaje(8, 10), 80)
        self.assertEqual(calcular_porcentaje(7, 10), 70)
        self.assertEqual(calcular_porcentaje(6, 10), 60)
        self.assertEqual(calcular_porcentaje(5, 10), 50)
        self.assertEqual(calcular_porcentaje(4, 10), 40)
        self.assertEqual(calcular_porcentaje(1, 13), 7.6923076923076925)
        self.assertEqual(calcular_porcentaje(2, 7), 28.571428571428573)
        self.assertEqual(calcular_porcentaje(6, 15), 40.0)
        self.assertEqual(calcular_porcentaje(19, 25), 76.0)
        self.assertEqual(calcular_porcentaje(17, 66), 25.757575757575758)



class Test_calcular_si_aprobo(unittest.TestCase):
    def test_calcular_si_aprobo_string(self):
        self.assertEqual(calcular_si_aprobo("Hola", "Fede"), None)
        self.assertEqual(calcular_si_aprobo("Diez", "Viente"), None)
        self.assertEqual(calcular_si_aprobo(10, "Viente"), None)
        self.assertEqual(calcular_si_aprobo("Diez", 20), None)


    def test_calcular_si_aprobo_lista(self):
        self.assertEqual(calcular_si_aprobo([1, 2, 3, 4], [1, 2, 3]), None)
        

    def test_calcular_si_aprobo_tupla(self):
        self.assertEqual(calcular_si_aprobo((1, 2, 3, 4), (1, 2, 3)), None)
        

    def test_calcular_si_aprobo_fuera_de_cotas(self):
        self.assertEqual(calcular_si_aprobo(101, 9), None)
        self.assertEqual(calcular_si_aprobo(189237, 9), None)
        self.assertEqual(calcular_si_aprobo(9, 18237), None)
        self.assertEqual(calcular_si_aprobo(9,101), None)
        self.assertEqual(calcular_si_aprobo(101.1111, 9), None)


    def test_calcular_si_aprobo_int(self):
        self.assertEqual(calcular_si_aprobo(60, 60), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(80, 90), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(50, 60), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(20, 40), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(10, 60), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(60, 50), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(100, 50), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(80, 20), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(30, 20), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(10, 5), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(90, 66), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(96, 69), "No aprobó.")
        
    def test_calcular_si_aprobo_float(self):
        self.assertEqual(calcular_si_aprobo(60.78263, 70.78123), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(80.891273, 90.891273), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(50.81273, 60.891273), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(20.8923, 40.8923), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(10.8923, 60.8923), "Aprobó.")
        self.assertEqual(calcular_si_aprobo(60.8923, 50.8923), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(99.8923, 50.8923), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(80.8923, 20.8923), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(30.8923, 20.8923), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(10.8923, 5.8923), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(90.8923, 66.8923), "No aprobó.")
        self.assertEqual(calcular_si_aprobo(96.8923, 69.8923), "No aprobó.")


unittest.main()