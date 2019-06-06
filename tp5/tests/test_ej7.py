import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej7 import consulta, alta, modificacion  # noqa


class Test_consulta(unittest.TestCase):
    def setUp(self):
        self.dicc = {"fede" : "1187656789",
                     "valen" : "1131334144",
                     "pacio" : "1157645012",
                     "heras" : "1168485566"}

    def test_consulta_int(self):
        self.assertEqual(consulta(dicc, 10), TypeError)

    def test_consulta_float(self):
        self.assertEqual(consulta(dicc, 10.5), TypeError)

    def test_consulta_lista(self):
        self.assertEqual(consulta(dicc, [1, 2, 3, 4]), TypeError)
        self.assertEqual(consulta(dicc, ["soy", "una", "tupla"]), TypeError)

    def test_consulta_tupla(self):
        self.assertEqual(consulta(dicc, (1, 2, 3, 4)), TypeError)
        self.assertEqual(consulta(dicc, ("soy", "tupla")), TypeError)

    def test_consulta_string(self):
        self.assertEqual(consulta(dicc, "fede"), "1187656789")
        self.assertEqual(consulta(dicc, "valen"), "1131334144")
        self.assertEqual(consulta(dicc, "pacio"), "1157645012")
        self.assertEqual(consulta(dicc, "heras"), "1168485566")
        self.assertEqual(consulta(dicc, "malvasio"), None)
        self.assertEqual(consulta(dicc, "Vallarino"), None)


class Test_alta(unittest.TestCase):
    def setUp(self):
        self.dicc = {"fede" : "1187656789",
                     "valen" : "1131334144",
                     "pacio" : "1157645012",
                     "heras" : "1168485566"}

    def test_alta_int(self):
        self.assertEqual(alta(dicc, 1, 1), TypeError)
        self.assertEqual(alta(dicc, "valen", 1), TypeError)
        self.assertEqual(alta(dicc, 1, "valen"), TypeError)


    def test_alta_float(self):
        self.assertEqual(alta(dicc, 1.123, 1.123), TypeError)
        self.assertEqual(alta(dicc, "valen", 1.123), TypeError)
        self.assertEqual(alta(dicc, 1.321, "valen"), TypeError)

    def test_alta_lista(self):
        self.assertEqual(alta(dicc, [1, 2], "hola"), TypeError)
        self.assertEqual(alta(dicc, "hola", [1, 2]), TypeError)
        self.assertEqual(alta(dicc, [1, 2], [1, 2]), TypeError)
        

    def test_alta_tupla(self):
        self.assertEqual(alta(dicc, (1, 2), (1, 2)), TypeError)
        self.assertEqual(alta(dicc, "valen", (1, 2)), TypeError)
        self.assertEqual(alta(dicc, (1, 2), "valen"), TypeError)

    def test_alta_string(self):
        # alta normal
        dicc_aux = alta(dicc, "malvasio", "1145678912")
        self.assertEqual(consulta(dicc_aux, "malvasio"), "1145678912")
        self.assertCountEqual(dicc_aux, 5)
        # alta ya existente
        self.assertEqual(alta("valen"), None)
        self.assertEqual(alta("pacio"), None)


class Test_modificacion(unittest.TestCase):
    def setUp(self):
        self.dicc = {"fede" : "1187656789",
                     "valen" : "1131334144",
                     "pacio" : "1157645012",
                     "heras" : "1168485566"}

    def test_modificacion_int(self):
        self.assertEqual(modificacion(dicc, 1, 1), TypeError)
        self.assertEqual(modificacion(dicc, "hola", 1), TypeError)
        self.assertEqual(modificacion(dicc, 1, "hola"), TypeError)

    def test_modificacion_float(self):
        self.assertEqual(modificacion(dicc, 1.123, 1.123), TypeError)
        self.assertEqual(modificacion(dicc, "hola", 1.123), TypeError)
        self.assertEqual(modificacion(dicc, 1.123, "hola"), TypeError)

    def test_modificacion_lista(self):
        self.assertEqual(modificacion(dicc, [1, 2], [1, 2]), TypeError)
        self.assertEqual(modificacion(dicc, "hola", [1, 2]), TypeError)
        self.assertEqual(modificacion(dicc, [1, 2], "hola"), TypeError)

    def test_modificacion_tupla(self):
        self.assertEqual(modificacion(dicc, (1, 2), (1, 2)), TypeError)
        self.assertEqual(modificacion(dicc, (1, 2), "hola"), TypeError)
        self.assertEqual(modificacion(dicc, "hola", (1, 2)), TypeError)        

    def test_modificacion_string(self):
        # No existe el registro
        self.assertEqual(modificacion(dicc, "malvasio", "1131334144"), None)
        # Existe
        diccAux = modificacion(dicc, "valen", "1131334145")
        self.assertEqual(consulta(diccAux, "valen", "1131334145"))


unittest.main()