import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej3 import numeros_triangulares


class Test_numeros_triangulares(unittest.TestCase):
    def test_numeros_triangulares_string(self):
        self.assertEqual(numeros_triangulares("Holaaa"), None)
        self.assertEqual(numeros_triangulares("12345"), None)
        self.assertEqual(numeros_triangulares(""), None)
        self.assertEqual(numeros_triangulares("Diez"), None)
        self.assertEqual(numeros_triangulares("Veinte"), None)

    def test_numeros_triangulares_lista(self):
        self.assertEqual(numeros_triangulares([1, 2]), None)
        self.assertEqual(numeros_triangulares(["soy", "una", "lista"]), None)
        self.assertEqual(numeros_triangulares(["aguante", "windows"]), None)

    def test_numeros_triangulares_tupla(self):
        self.assertEqual(numeros_triangulares((1, 2)), None)
        self.assertEqual(numeros_triangulares(("soy", "una", "tupla")), None)
        self.assertEqual(numeros_triangulares(("aguante", "windows")), None)

    def test_numeros_triangulares_cero(self):
        self.assertEqual(numeros_triangulares(0), None)

    def test_numeros_triangulares_neg(self):
        self.assertEqual(numeros_triangulares(-123786), None)
        self.assertEqual(numeros_triangulares(-0.00001), None)
        self.assertEqual(numeros_triangulares(-10), None)

    def test_numeros_triangulares_float(self):
        self.assertEqual(numeros_triangulares(4.512312312), None)
        self.assertEqual(numeros_triangulares(0.111), None)
        self.assertEqual(numeros_triangulares(1.1), None)

    def test_numeros_triangulares_funcionalidad(self):
        # Prueba con 10 numeros
        lista_numeros_triangulares = numeros_triangulares(10)
        self.assertEqual(len(lista_numeros_triangulares), 10)
        # Me fijo si los numeros dicen lo q tendrían q decir
        self.assertEqual(lista_numeros_triangulares[0], 1)
        self.assertEqual(lista_numeros_triangulares[1], 3)
        self.assertEqual(lista_numeros_triangulares[2], 6)
        self.assertEqual(lista_numeros_triangulares[3], 10)
        self.assertEqual(lista_numeros_triangulares[4], 15)
        self.assertEqual(lista_numeros_triangulares[5], 21)
        self.assertEqual(lista_numeros_triangulares[6], 28)
        self.assertEqual(lista_numeros_triangulares[7], 36)
        self.assertEqual(lista_numeros_triangulares[8], 45)
        self.assertEqual(lista_numeros_triangulares[9], 55)
        
unittest.main()