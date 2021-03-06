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


class Test_modulo_de(unittest.TestCase):
    def test_modulo_de_string(self):
        self.assertEqual(modulo_de("Hola"), None)

    def test_modulo_de_positivo(self):
        self.assertEqual(modulo_de(10), 10)
        self.assertEqual(modulo_de(0.000001), 0.000001)
        self.assertEqual(modulo_de(1000), 1000)
        self.assertEqual(modulo_de(474747474), 474747474)
        self.assertEqual(modulo_de(0.2), 0.2)

    def test_modulo_de_negativo(self):
        self.assertEqual(modulo_de(-10), 10)
        self.assertEqual(modulo_de(-0.000001), 0.000001)
        self.assertEqual(modulo_de(-1000), 1000)
        self.assertEqual(modulo_de(-474747474), 474747474)
        self.assertEqual(modulo_de(-0.2), 0.2)

    def test_modulo_de_cero(self):
        self.assertEqual(modulo_de(0), 0)


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
        # Le doy algo que no es un rect??ngulo
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
    def test_area_y_perimetro_circulo_string(self):
        self.assertEqual(area_y_perimetro_circulo("Hola fede"), None)
        self.assertEqual(area_y_perimetro_circulo("10"), None)
        self.assertEqual(area_y_perimetro_circulo(""), None)

    def test_area_y_perimetro_circulo_lista(self):
        self.assertEqual(area_y_perimetro_circulo([1, 2, 3, 4]), None)
        self.assertEqual(area_y_perimetro_circulo([1]), None)

    def test_area_y_perimetro_circulo_tupla(self):
        self.assertEqual(area_y_perimetro_circulo((1, 2, 3, 4)), None)

    def test_area_y_perimetro_circulo_neg(self):
        self.assertEqual(area_y_perimetro_circulo(-10), None)
        self.assertEqual(area_y_perimetro_circulo(-0.00000001), None)

    def test_area_y_perimetro_circulo_cero(self):
        self.assertEqual(area_y_perimetro_circulo(0), None)

    def test_area_y_perimetro_circulo_int(self):
        self.assertEqual(area_y_perimetro_circulo(1),
                         (3.141592653589793, 6.283185307179586))
        self.assertEqual(area_y_perimetro_circulo(10),
                         (314.1592653589793, 62.83185307179586))
        self.assertEqual(area_y_perimetro_circulo(3232),
                         (32816523.939091947, 20307.254912804423))
        self.assertEqual(area_y_perimetro_circulo(878787),
                         (2426147050057.681, 5521581.5665404275))

    def test_area_y_perimetro_circulo_float(self):
        self.assertEqual(area_y_perimetro_circulo(0.1),
                         (0.031415926535897934, 0.6283185307179586))
        self.assertEqual(area_y_perimetro_circulo(1.78273872),
                         (9.984475763194439, 11.201277732044142))
        self.assertEqual(area_y_perimetro_circulo(10.1),
                         (320.4738665926948, 63.46017160251382))
        self.assertEqual(area_y_perimetro_circulo(20.2),
                         (1281.895466370779, 126.92034320502763))


class Test_volumen_esfera(unittest.TestCase):
    def test_volumen_esfera_string(self):
        self.assertEqual(volumen_esfera("10"), None)
        self.assertEqual(volumen_esfera("Hola fede"), None)
        self.assertEqual(volumen_esfera(""), None)

    def test_volumen_esfera_lista(self):
        self.assertEqual(volumen_esfera([1, 2, 3, 4]), None)
        self.assertEqual(volumen_esfera([1]), None)

    def test_volumen_esfera_tupla(self):
        self.assertEqual(volumen_esfera((1, 2, 3, 4)), None)

    def test_volumen_esfera_neg(self):
        self.assertEqual(volumen_esfera(-10), None)
        self.assertEqual(volumen_esfera(-0.00000001), None)

    def test_volumen_esfera_cero(self):
        self.assertEqual(volumen_esfera(0), None)

    def test_volumen_esfera_int(self):
        self.assertEqual(volumen_esfera(1),
                         4.1887902047863905)
        self.assertEqual(volumen_esfera(10),
                         4188.790204786391)
        self.assertEqual(volumen_esfera(3232),
                         141417340494.86023)
        self.assertEqual(volumen_esfera(8787),
                         2841911101314.909)

    def test_volumen_esfera_float(self):
        self.assertEqual(volumen_esfera(0.1),
                         0.004188790204786391)
        self.assertEqual(volumen_esfera(1.78273872),
                         23.7329487225977)
        self.assertEqual(volumen_esfera(10.1),
                         4315.714736781622)
        self.assertEqual(volumen_esfera(20.2),
                         34525.71789425298)


unittest.main()
