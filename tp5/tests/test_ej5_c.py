import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej6_c import cambiar_vocales  # noqa


class Test_cambiar_vocales(unittest.TestCase):
    def test_cambiar_vocales_int(self):
        self.assertEqual(cambiar_vocales(1), TypeError)

    def test_cambiar_vocales_float(self):
        self.assertEqual(cambiar_vocales(1.12837), TypeError)

    def test_cambiar_vocales_lista(self):
        self.assertEqual(cambiar_vocales([1, 2, 3, 4]), TypeError)
        self.assertEqual(cambiar_vocales(["soy", "una", "tupla"]),
                                               TypeError)

    def test_cambiar_vocales_tupla(self):
        self.assertEqual(cambiar_vocales((1, 2, 3, 4)), TypeError)
        self.assertEqual(cambiar_vocales(("soy", "tupla")), TypeError)

    def test_cambiar_vocales_string(self):
        self.assertEqual(cambiar_vocales("hola todo bien"),
                                         "")
        self.assertEqual(cambiar_vocales("windows media center"),
                                         "")
        self.assertEqual(cambiar_vocales("ayer me aguante"),
                                                   "ayer aguante")
        self.assertEqual(cambiar_vocales("amaneci muy almanaque"),
                                                   "amaneci almanaque")
        self.assertEqual(cambiar_vocales("avión hola aeropuerto ala delta"),
                                                   "avión aeropuerto ala")
        self.assertEqual(cambiar_vocales("aguante el agua azul"), 
                                                   "aguante agua azul")
        self.assertEqual(cambiar_vocales("aclaro a clara que me aclare"),
                                                   "aclaro a aclare")

unittest.main()
