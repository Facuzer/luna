import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej5_c import solo_palabras_con_a  # noqa


class Test_solo_palabras_con_a(unittest.TestCase):
    def test_solo_palabras_con_a_int(self):
        self.assertEqual(solo_palabras_con_a(1), TypeError)

    def test_solo_palabras_con_a_float(self):
        self.assertEqual(solo_palabras_con_a(1.12837), TypeError)

    def test_solo_palabras_con_a_lista(self):
        self.assertEqual(solo_palabras_con_a([1, 2, 3, 4]), TypeError)
        self.assertEqual(solo_palabras_con_a(["soy", "una", "tupla"]),
                                               TypeError)

    def test_solo_palabras_con_a_tupla(self):
        self.assertEqual(solo_palabras_con_a((1, 2, 3, 4)), TypeError)
        self.assertEqual(solo_palabras_con_a(("soy", "tupla")), TypeError)

    def test_solo_palabras_con_a_string(self):
        self.assertEqual(solo_palabras_con_a("hola todo bien"),
                                         "")
        self.assertEqual(solo_palabras_con_a("windows media center"),
                                         "")
        self.assertEqual(solo_palabras_con_a("ayer me aguante"),
                                                   "ayer aguante")
        self.assertEqual(solo_palabras_con_a("amaneci muy almanaque"),
                                                   "amaneci almanaque")
        self.assertEqual(solo_palabras_con_a(
                                        "avión hola aeropuerto ala delta"),
                                                   "avión aeropuerto ala")
        self.assertEqual(solo_palabras_con_a("aguante el agua azul"), 
                                                   "aguante agua azul")
        self.assertEqual(solo_palabras_con_a("aclaro a clara que me aclare"),
                                                   "aclaro a aclare")
        self.assertEqual(solo_palabras_con_a("soy árabe"),
                                                  "árabe")
        self.assertEqual(solo_palabras_con_a("SOY ÁRABE"),
                                                   "ÁRABE")
        self.assertEqual(solo_palabras_con_a("Aguante la aguante"), "Aguante aguante")

unittest.main()
