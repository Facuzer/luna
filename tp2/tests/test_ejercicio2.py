import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ejercicios import *  # noqa
# Este es para probar las funciones auxiliareas que cree
# como las de validación de datos.


class Test_es_numerico(unittest.TestCase):
    def test_es_numerico(self):
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
    def test_es_positivo(self):
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
            self.asserEqual(es_positivo(1283128738912), True)
            self.asserEqual(es_positivo(-2312312312), False)
            self.assertEqual(es_positivo(0), True)

        def test_es_positivo_float(self):
            # Con float's
            self.assertEqual(es_positivo(1.111111), True)
            self.assertEqual(es_positivo(2326723.27637263723), True)
            self.assertEqual(es_positivo(-1231283.28378273872), False)
            self.assertEqual(es_positivo(-1.11111111), True)
            self.assertEqual(es_positivo(0.000000001), True)
            self.assertEqual(es_positivo(-0.000000001), False)


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
    pass


class Test_area_rectangulo_coord(unittest.TestCase):
    pass


class Test_area_y_perimetro_circulo(unittest.TestCase):
    pass


class Test_volumen_esfera(unittest.TestCase):
    pass


unittest.main()
