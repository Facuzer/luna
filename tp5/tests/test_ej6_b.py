import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej6_b import solo_vocales  # noqa


class Test_solo_vocales(unittest.TestCase):
    def test_solo_vocales_int(self):
        self.assertEqual(solo_vocales(1), TypeError)

    def test_solo_vocales_float(self):
        self.assertEqual(solo_vocales(1.12837), TypeError)

    def test_solo_vocales_lista(self):
        self.assertEqual(solo_vocales([1, 2, 3, 4]), TypeError)
        self.assertEqual(solo_vocales(["soy", "una", "tupla"]),
                                               TypeError)

    def test_solo_vocales_tupla(self):
        self.assertEqual(solo_vocales((1, 2, 3, 4)), TypeError)
        self.assertEqual(solo_vocales(("soy", "tupla")), TypeError)

    def test_solo_vocales_string(self):
        self.assertEqual(solo_vocales("hola todo bien"),
                                         "oa oo ie")
        self.assertEqual(solo_vocales("windows media center"),
                                         "io eia ee")
        self.assertEqual(solo_vocales("ayer me aguante"),
                                                   "ae e auae")
        self.assertEqual(solo_vocales("amaneci muy almanaque"),
                                                   "aae u aaaue")
        self.assertEqual(solo_vocales(
                                        "avión hola aeropuerto ala delta"),
                                                   "aió oa aeoueo aa ea")
        self.assertEqual(solo_vocales("AGUANTE EL AGUA AZUL"), 
                                                   "AUAE E AUA AUL")
        self.assertEqual(solo_vocales("áááábbbbbbbcccccddd"),
                                                   "áááá")
        self.assertEqual(solo_vocales("íííóóóúúúfede"),
                                                  "íííóóóúúú")
        self.assertEqual(solo_vocales("Laaeiocaeioudaeotaem"),
                                                   "aaeioaeiouaeoae")

unittest.main()