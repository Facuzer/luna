import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej4 import comprobar_capitalizacion  # noqa


class Test_comprobar_capitalizacion(unittest.TestCase):
    def test_comprobar_capitalizacion_int(self):
        self.assertEqual(comprobar_capitalizacion(1, 1), TypeError)
        self.assertEqual(comprobar_capitalizacion(1000, "diez"), TypeError)
        self.assertEqual(comprobar_capitalizacion("veinte", 12837283),
                                                  TypeError)  # noqa

    def test_comprobar_capitalizacion_float(self):
        self.assertEqual(comprobar_capitalizacion(1.12837, 1.81273), TypeError)
        self.assertEqual(comprobar_capitalizacion(1000.128, "diez"), TypeError)
        self.assertEqual(comprobar_capitalizacion("diez", 283.818), TypeError)

    def test_comprobar_capitalizacion_lista(self):
        self.assertEqual(comprobar_capitalizacion([1, 2], [3, 4]), TypeError)
        self.assertEqual(comprobar_capitalizacion(["soy", "lista"],
                                                  ["Yo", "No"]), TypeError)

    def test_comprobar_capitalizacion_tupla(self):
        self.assertEqual(comprobar_capitalizacion((1, 2), (3, 4)), TypeError)
        self.assertEqual(comprobar_capitalizacion(("soy", "tupla"),
                                                  ("Yo no")), TypeError)

    def test_comprobar_capitalizacion_string(self):
        self.assertEqual(comprobar_capitalizacion("república argentina",
                                                  "REPÚBLICA ARGENTINA"), True)
        self.assertEqual(comprobar_capitalizacion("me gusta el queso",
                                                  "ME GUSTA EL QUESO"), True)
        self.assertEqual(comprobar_capitalizacion("Me GuSTa EL QuEsO",
                                                  "ME GUSTA EL QUESO"), True)
        self.assertEqual(comprobar_capitalizacion("Aguante rappi",
                                                  "AGUANTE RAPPi"), False)
        self.assertEqual(comprobar_capitalizacion("Soy valen",
                                                  "Soy fede"), False)
        self.assertEqual(comprobar_capitalizacion("Minecraft",
                                                  "MINECRAft"), False)
        self.assertEqual(comprobar_capitalizacion("HoLa",
                                                  "HoLA"), False)


unittest.main()
