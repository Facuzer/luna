import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ejercicios import *  # noqa


# Empiezo con las funciones auxiliares que cree yo.
class Test_es_numerico(unittest.TestCase):
    def test_es_numerico_string(self):
        # Con string?
        self.assertEqual(es_numerico("Hola fede"), False)
        self.assertEqual(es_numerico(""), False)
        self.assertEqual(es_numerico("1234"), False)

    def test_es_numerico_lista(self):
        # Con una lista?
        self.assertEqual(es_numerico(["no", "soy", "un", "numero"]), False)
        self.assertEqual(es_numerico([1, 2, 3]), False)

    def test_es_numerico_tupla(self):
        # Con una tupla?
        self.assertEqual(es_numerico(("soy", "una", "tupla")), False)
        self.assertEqual(es_numerico((1, 2, 3)), False)

    def test_es_numerico_int(self):
        # Con int's
        self.assertEqual(es_numerico(5), True)
        self.assertEqual(es_numerico(12387283), True)

    def test_es_numerico_float(self):
        # Con float's
        self.assertEqual(es_numerico(1.111111), True)
        self.assertEqual(es_numerico(2326723.27637263723), True)


class Test_es_positivo(unittest.TestCase):
    def test_es_positivo_string(self):
        # Con string?
        self.assertEqual(es_positivo("Hola fede"), None)
        self.assertEqual(es_positivo(""), None)
        self.assertEqual(es_positivo("1234"), None)
        self.assertEqual(es_positivo("-1234"), None)

    def test_es_positivo_lista(self):
        # Con una lista?
        self.assertEqual(es_positivo(["1234"]), None)
        self.assertEqual(es_positivo(["diez", "veinte", "dos", "tres"]), None)
        self.assertEqual(es_positivo([1, 2, 3]), None)
        self.assertEqual(es_positivo([-1, -2, -3]), None)

    def test_es_positivo_tupla(self):
        # Con una tupla?
        self.assertEqual(es_positivo(("1234", 1234)), None)
        self.assertEqual(es_positivo(("diez", "veinte", "dos", "tres")), None)
        self.assertEqual(es_positivo((1, 2, 3)), None)
        self.assertEqual(es_positivo((-1, -2, -3)), None)

    def test_es_positivo_int(self):
        # Con int's
        self.assertEqual(es_positivo(5), True)
        self.assertEqual(es_positivo(-5), False)
        self.assertEqual(es_positivo(1283128738912), True)
        self.assertEqual(es_positivo(-2312312312), False)
        self.assertEqual(es_positivo(0), True)

    def test_es_positivo_float(self):
        # Con float's
        self.assertEqual(es_positivo(1.111111), True)
        self.assertEqual(es_positivo(2326723.27637263723), True)
        self.assertEqual(es_positivo(-1231283.28378273872), False)
        self.assertEqual(es_positivo(-1.11111111), False)
        self.assertEqual(es_positivo(0.000000001), True)
        self.assertEqual(es_positivo(-0.000000001), False)


# Y aca ya van todas las del enunciado.
class Test_perimetro_rectangulo(unittest.TestCase):
    def test_perimetro_rectangulo_string(self):
        # Si meto un string en un campo? si meto en los dos?
        self.assertEqual(perimetro_rectangulo("hola fede", 1), None)
        self.assertEqual(perimetro_rectangulo(1, "hola fede"), None)
        self.assertEqual(perimetro_rectangulo("hola fede", "hola fede"), None)

    def test_perimetro_rectangulo_neg(self):
        # Si meto un negativo en un campo? si meto un negativo
        # en los dos?
        self.assertEqual(perimetro_rectangulo(-1, 2), None)
        self.assertEqual(perimetro_rectangulo(-2, 1), None)
        self.assertEqual(perimetro_rectangulo(-2, -2), None)

    def test_perimetro_rectangulo_cero(self):
        # Si meto un 0 en un campo? si meto en los dos?
        self.assertEqual(perimetro_rectangulo(0, 3), None)
        self.assertEqual(perimetro_rectangulo(3, 0), None)
        self.assertEqual(perimetro_rectangulo(0, 0), None)

    def test_perimetro_rectangulo_lista(self):
        # Que pasa si meto una lista/tupla
        self.assertEqual(perimetro_rectangulo((1, 2, 3), (1, 2, 3)), None)
        self.assertEqual(perimetro_rectangulo([1, 2, 3], [1, 2, 3]), None)
        self.assertEqual(perimetro_rectangulo(["hola", "hola", 3], [1, 2, 3]), None)

    def test_perimetro_rectangulo_int(self):
        # Valores int
        self.assertEqual(perimetro_rectangulo(1, 1), 4)
        self.assertEqual(perimetro_rectangulo(5, 5), 20)
        self.assertEqual(perimetro_rectangulo(179, 1), 360)
        self.assertEqual(perimetro_rectangulo(100, 100), 400)

    def test_perimetro_rectangulo_float(self):
        # Valores float
        self.assertEqual(perimetro_rectangulo(1.1, 1.2), 4.6)
        self.assertEqual(perimetro_rectangulo(1.12381273897, 1.28309182983), 4.8138091376)


class Test_area_rectangulo(unittest.TestCase):
    def test_area_rectangulo_string(self):
        self.assertEqual(area_rectangulo("Hola", "Hola"), None)
        self.assertEqual(area_rectangulo("hola", 2), None)
        self.assertEqual(area_rectangulo(2, "hola"), None)
        self.assertEqual(area_rectangulo("15", "30"), None)

    def test_area_rectangulo_neg(self):
        self.assertEqual(area_rectangulo(-15, -10), None)
        self.assertEqual(area_rectangulo(-15, 10), None)
        self.assertEqual(area_rectangulo(10, -15), None)

    def test_area_rectangulo_cero(self):
        self.assertEqual(area_rectangulo(0, 0), None)
        self.assertEqual(area_rectangulo(10, 0), None)
        self.assertEqual(area_rectangulo(0, 10), None)

    def test_area_rectangulo_lista(self):
        self.assertEqual(area_rectangulo([1, 2, 3], [4, 5, 6]), None)
        self.assertEqual(area_rectangulo([1, 2, 3], 10), None)
        self.assertEqual(area_rectangulo(1, [1, 2, 3]), None)

    def test_area_rectangulo_tupla(self):
        self.assertEqual(area_rectangulo((1, 2, 3), (4, 5, 6)), None)
        self.assertEqual(area_rectangulo((1, 2, 3), 10), None)
        self.assertEqual(area_rectangulo(1, (1, 2, 3)), None)

    def test_area_rectangulo_int(self):
        self.assertEqual(area_rectangulo(10, 10), 100)
        self.assertEqual(area_rectangulo(123, 56), 6888)
        self.assertEqual(area_rectangulo(25, 5), 125)
        self.assertEqual(area_rectangulo(31, 1), 31)

    def test_area_rectangulo_float(self):
        self.assertEqual(area_rectangulo(1.25, 1.50), 1.875)
        self.assertEqual(area_rectangulo(2.75, 1.1111), 3.055525)
        self.assertEqual(area_rectangulo(1.6236372, 2.377373), 3.8599912410756)
        self.assertEqual(area_rectangulo(0.0001, 0.0002), 0.00000002)


class Test_area_rectangulo_coord(unittest.TestCase):
    def test_area_rectangulo_coord_string(self):
        self.assertEqual(area_rectangulo_coord("1", "2", "3", "4",
                                               "5", "6", "7", "8"), None)
        self.assertEqual(area_rectangulo_coord(1, 2, "3", "4",
                                               "5", "6", "7", "8"), None)
        self.assertEqual(area_rectangulo_coord("1", "2", 3, 4,
                                               "5", "6", "7", "8"), None)
        self.assertEqual(area_rectangulo_coord("1", "2", "3", "4",
                                               5, 6, "7", "8"), None)
        self.assertEqual(area_rectangulo_coord("1", "2", "3", "4",
                                               "5", "6", 7, 8), None)

    def test_area_rectangulo_coord_lista(self):
        self.assertEqual(area_rectangulo_coord([1, 2], [3, 4],
                                               [5, 6], [7, 8],
                                               [7, 8], [9, 10],
                                               [10, 11], [12, 13]), None)
        self.assertEqual(area_rectangulo_coord(1, 2,
                                               [5, 6], [7, 8],
                                               [7, 8], [9, 10],
                                               [10, 11], [12, 13]), None)
        self.assertEqual(area_rectangulo_coord([1, 2], [3, 4],
                                               3, 4,
                                               [7, 8], [9, 10],
                                               [10, 11], [12, 13]), None)
        self.assertEqual(area_rectangulo_coord([1, 2], [3, 4],
                                               [5, 6], [7, 8],
                                               5, 6,
                                               [10, 11], [12, 13]), None)
        self.assertEqual(area_rectangulo_coord([1, 2], [3, 4],
                                               [5, 6], [7, 8],
                                               [7, 8], [9, 10],
                                               7, 8), None)

    def test_area_rectangulo_coord_tupla(self):
        self.assertEqual(area_rectangulo_coord((1, 2), (3, 4),
                                               (5, 6), (7, 8),
                                               (7, 8), (9, 10),
                                               (10, 11), (12, 13)), None)
        self.assertEqual(area_rectangulo_coord(1, 2,
                                               (5, 6), (7, 8),
                                               (7, 8), (9, 10),
                                               (10, 11), (12, 13)), None)
        self.assertEqual(area_rectangulo_coord((1, 2), (3, 4),
                                               3, 4,
                                               (7, 8), (9, 10),
                                               (10, 11), (12, 13)), None)
        self.assertEqual(area_rectangulo_coord((1, 2), (3, 4),
                                               (5, 6), (7, 8),
                                               5, 6,
                                               (10, 11), (12, 13)), None)
        self.assertEqual(area_rectangulo_coord((1, 2), (3, 4),
                                               (5, 6), (7, 8),
                                               (7, 8), (9, 10),
                                               7, 8), None)

    def test_area_rectangulo_coord_no_dar_rectangulo(self):
        # Le doy algo que no es un rectángulo
        self.assertEqual(area_rectangulo_coord(1, 2,
                                               4, 10,
                                               5, 6,
                                               7, 8), None)
        # Le doy puntos iguales
        self.assertEqual(area_rectangulo_coord(1, 2,
                                               1, 2,
                                               5, 6,
                                               5, 2), None)
        # Le doy todos los puntos iguales
        self.assertEqual(area_rectangulo_coord(0, 0,
                                               0, 0,
                                               0, 0,
                                               0, 0), None)

    def test_area_rectangulo_coord_int(self):
        self.assertEqual(area_rectangulo_coord(1, 2,
                                               1, 6,
                                               5, 6,
                                               5, 2), 16)
        self.assertEqual(area_rectangulo_coord(1, 2,
                                               1, 100,
                                               5, 100,
                                               5, 2), 392)

    def test_area_rectangulo_coord_float(self):
        self.assertEqual(area_rectangulo_coord(1.5, 1.5,
                                               1.5, 4,
                                               5.5, 4,
                                               5.5, 1.5), 10)


class Test_area_y_perimetro_circulo(unittest.TestCase):
    pass


class Test_volumen_esfera(unittest.TestCase):
    pass


unittest.main()
