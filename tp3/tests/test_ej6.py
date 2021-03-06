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
    def test_raiz(self):
        self.assertEqual(raiz("estos", "son", "numeros"), None)
        self.assertEqual(raiz("1", "2", "3"), None)
        self.assertEqual(raiz(1, "2", "3"), None)
        self.assertEqual(raiz("1", 2, "3"), None)
        self.assertEqual(raiz("1", "2", 3), None)
        self.assertEqual(raiz(1, 2, "3"), None)
        self.assertEqual(raiz("1", 2, 3), None)
        self.assertEqual(raiz("1", "2", "3"), None)
        self.assertEqual(raiz("1", "2", "3"), None)

    def test_raiz_lista(self):
        self.assertEqual(raiz([1, 2, 3], [1, 2, 3], [1, 2, 3]), None)
        self.assertEqual(raiz(1, [1, 2, 3], [1, 2, 3]), None)
        self.assertEqual(raiz([1, 2, 3], 2, [1, 2, 3]), None)
        self.assertEqual(raiz([1, 2, 3], [1, 2, 3], 3), None)


    def test_raiz_tupla(self):
        self.assertEqual(raiz((1, 2, 3), (1, 2, 3), (1, 2, 3)), None)
        self.assertEqual(raiz(1, (1, 2, 3), (1, 2, 3)), None)
        self.assertEqual(raiz((1, 2, 3), 2, (1, 2, 3)), None)
        self.assertEqual(raiz((1, 2, 3), (1, 2, 3), 3), None)

    def test_raiz_dar_a_cero(self):
        self.assertEqual(raiz(0, 10, 10), None)
        self.assertEqual(raiz(0, 283728, 120930912), None)
    
    def test_raiz_real(self):
        # int's
        self.assertEqual(raiz(1, 0, 0), 0)
        self.assertEqual(raiz(12837, 123, -8923), 
                         (0.8289495603087264, -0.8385312382708671))
        self.assertEqual(raiz(928, 8, -876), 
                         (0.9672780949522991, -0.9758987846074716))
        self.assertEqual(raiz(-10, 15, 20),
                         (-0.8507810593582121, 2.350781059358212))
        # float's
        self.assertEqual(raiz(10.5, -5.1, -10.25575),
                         (1.2605593031549533, -0.7748450174406675))
        self.assertEqual(raiz(3.5, -8.5, -1.5), 
                         (2.5938005654162835, -0.16522913684485477))
        self.assertEqual(raiz(-1.555, 10, 128.85),
                              (-6.438619608003603, 12.869487775206176))
        # cero
        self.assertEqual(raiz(10, 0, 0), 0)
        pass

    def test_raiz_imaginaria(self):
        self.assertEqual(raiz(10, 10, 10), 
                         ('0.3660254037844387i', '-1.3660254037844388i'))
        self.assertEqual(raiz(1.5, 2, 10.001),
                         ('1.8279052182243838i', '-3.1612385515577173i'))
        self.assertEqual(raiz(-15, 10, -15),
                         ('-0.6094757082487301i', '1.2761423749153968i'))


class Test_interseccion_entre_rectas(unittest.TestCase):
    def test_interseccion_entre_rectas_string(self):
        self.assertEqual(interseccion_entre_rectas(
            "no", "soy", "mucho", "texto"), None)
        self.assertEqual(interseccion_entre_rectas("1", "2", "3", "4"), None)
        self.assertEqual(interseccion_entre_rectas(1, "2", "3", "4"), None)
        self.assertEqual(interseccion_entre_rectas("1", 2, "3", "4"), None)
        self.assertEqual(interseccion_entre_rectas("1", "2", 3, "4"), None)
        self.assertEqual(interseccion_entre_rectas("1", "2", "3", 4), None)
        self.assertEqual(interseccion_entre_rectas(1, 2, "3", "4"), None)
        self.assertEqual(interseccion_entre_rectas(1, 2, 3, "4"), None)
        
    def test_interseccion_entre_rectas_lista(self):
        self.assertEqual(interseccion_entre_rectas(
                         [1, 2, 3], [1, 2], [1, 2], [1]), None)

    def test_interseccion_entre_rectas_tupla(self):
        self.assertEqual(interseccion_entre_rectas(
                         (1, 2, 3), (1, 2), (1, 2), (1)), None)

    def test_interseccion_entre_rectas_pendientes_cero(self):
        self.assertEqual(interseccion_entre_rectas(0, 1, 0, 1), None)
        self.assertEqual(interseccion_entre_rectas(1, 1, 0, 1), None)
        self.assertEqual(interseccion_entre_rectas(0, 1, 1, 1), None)


    def test_interseccion_entre_rectas_pendientes_iguales(self):
        self.assertEqual(interseccion_entre_rectas(1, 5, 1, 123), None)

    def test_interseccion_entre_rectas_int(self):
        self.assertEqual(interseccion_entre_rectas(10, 1, 20, 5), -0.4)
        self.assertEqual(interseccion_entre_rectas(1, 5, 20, 21),
                         -0.8421052631578947)
        self.assertEqual(interseccion_entre_rectas(-12, 5, -20, 4), -0.125)
        self.assertEqual(interseccion_entre_rectas(-15, 13, -22, 12),
                         -0.14285714285714285)
        self.assertEqual(interseccion_entre_rectas(-123, 431, -23, 34), 3.97)


    def test_interseccion_entre_rectas_float(self):
        self.assertEqual(interseccion_entre_rectas(1.5, 2.4, 1.123, 1.18312),
                         -3.2277984084880638)
        self.assertEqual(interseccion_entre_rectas(3.123, 1.3, 2.5, 1.18237),
                         -0.18881219903691826)
        self.assertEqual(interseccion_entre_rectas(-4.123, -4.1231231235, 5.123, 
                                                   9.123),
                         -1.4326328275470472)
        self.assertEqual(interseccion_entre_rectas(-42.237657233, -4-12837, 1.12736, 2912832), -67466.20171463036)
        self.assertEqual(interseccion_entre_rectas(1.1273612763, 1.8913789273, 1.1287382, 2.12837), -172.1163436289339)


unittest.main()