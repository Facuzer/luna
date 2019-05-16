import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej1 import repetir_palabra

class Test_repetir_palabra(unittest.TestCase):
    def test_repetir_palabra_numeros(self):
        self.assertEqual(repetir_palabra(2), None)
        self.assertEqual(repetir_palabra(23871), None)
        self.assertEqual(repetir_palabra(12818.3232), None)
        self.assertEqual(repetir_palabra(0.0000001), None)
    
    def test_repetir_palabra_lista(self):
        self.assertEqual(repetir_palabra(["soy", "una", "lista"]), None)
    
    def test_repetir_palabra_tupla(self):
        self.assertEqual(repetir_palabra(("soy", "una", "tupla")), None)

    def test_repetir_palabra_vacio(self):
        self.assertEqual(repetir_palabra(""), None)

    def test_repetir_palabra_strings(self):
        self.assertEqual(repetir_palabra("hola"), "hola " * 1000)

unittest.main()