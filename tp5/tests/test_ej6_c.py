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
                                         "hule tudu boin")
        self.assertEqual(cambiar_vocales("windows media center"),
                                         "wonduws midoe cintir")
        self.assertEqual(cambiar_vocales("Hoy dia Pleno"),
                                         "Huy doe Plinu")
        self.assertEqual(cambiar_vocales("sOY mUY feLIZ"),
                                                   "sUY mAY fiLOZ")
        self.assertEqual(cambiar_vocales("valenTIN schiaFFINO"),
                                                   "velinTON schoeFFONU")
        self.assertEqual(cambiar_vocales("hola señor"),
                                                   "hule siñur")
        self.assertEqual(cambiar_vocales("Futbol es de enrique"), 
                                                   "Fatbul is di inroqai")
        self.assertEqual(cambiar_vocales("Complete the Monument"),
                                                   "Cumpliti thi Munamint")
        self.assertEqual(cambiar_vocales("Hola"),
                                                   "Hule")
        self.assertEqual(cambiar_vocales("s"), "s")


unittest.main()
