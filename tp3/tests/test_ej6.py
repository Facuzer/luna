import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej6 import obtener_vertice ,raiz, interseccion_entre_rectas

class Test_obtener_vertice(unittest.TestCase):
    def test_obtener_vertice_string(self):
        self.assertEqual(obtener_vertice("estos", "son", "numeros"), None)
        self.assertEqual(obtener_vertice("1", "2", "3"), None)
        self.assertEqual(obtener_vertice(1, "2", "3"), None)
        self.assertEqual(obtener_vertice("1", 2, "3"), None)
        self.assertEqual(obtener_vertice("1", "2", 3), None)
        self.assertEqual(obtener_vertice(1, 2, "3"), None)
        self.assertEqual(obtener_vertice("1", 2, 3), None)
        self.assertEqual(obtener_vertice("1", "2", "3"), None)
        self.assertEqual(obtener_vertice("1", "2", "3"), None)

    def test_obtener_vertice_lista(self):
        self.assertEqual(obtener_vertice([1, 2, 3], [1, 2, 3], [1, 2, 3]), None)
        self.assertEqual(obtener_vertice(1, [1, 2, 3], [1, 2, 3]), None)
        self.assertEqual(obtener_vertice([1, 2, 3], 2, [1, 2, 3]), None)
        self.assertEqual(obtener_vertice([1, 2, 3], [1, 2, 3], 3), None)


    def test_obtener_vertice_tupla(self):
        self.assertEqual(obtener_vertice((1, 2, 3), (1, 2, 3), (1, 2, 3)), None)
        self.assertEqual(obtener_vertice(1, (1, 2, 3), (1, 2, 3)), None)
        self.assertEqual(obtener_vertice((1, 2, 3), 2, (1, 2, 3)), None)
        self.assertEqual(obtener_vertice((1, 2, 3), (1, 2, 3), 3), None)

    def test_obtener_vertice_dar_a_cero(self):
        self.assertEqual(obtener_vertice(0, 10, 10), None)
        self.assertEqual(obtener_vertice(0, 283728, 120930912), None)
    
    def test_obtener_vertice_int(self):
        self.assertEqual(obtener_vertice(1, 0, 0), ("mínimo", (0, 0)))
        self.assertEqual(obtener_vertice(1, 10, 10), ("mínimo", (-5, -15)))
        self.assertEqual(obtener_vertice(32, 39, 1), 
                         ("mínimo", (-0.609375, 357.484375)))
        self.assertEqual(obtener_vertice(10, 10, 10), 
                         ("mínimo", (-0.5, 30)))
        self.assertEqual(obtener_vertice(-123, 10, 10), 
                         ('máximo', (0.04065040650406504, 35.40650406504065)))
        self.assertEqual(obtener_vertice(-1, 0, 0), ('máximo', (0, 0)))
        self.assertEqual(obtener_vertice(-1, 123, -10),
                         ('máximo', (61.5, 11336.75)))


    def test_obtener_vertice_float(self):
        self.assertEqual(obtener_vertice(1.5, 0.5, 10.001), 
                         ("mínimo", (-0.16666666666666666, 9.980166666666666)))
        self.assertEqual(obtener_vertice(1.0001, 0.01, 0), 
                         ("mínimo", (-0.004999500049995001, 
                                     -2.4995000499950007e-05)))
        self.assertEqual(obtener_vertice(-0.5, 0.1, -123), 
                         ("máximo", (0.1, -122.9875)))
        self.assertEqual(obtener_vertice(-1.12736, 123, 1.5),
                         ("máximo", (54.55222821458984, 10493.674070394549)))
    
class Test_raiz(unittest.TestCase):
    pass


class Test_interseccion_entre_rectas(unittest.TestCase):
    pass


unittest.main()