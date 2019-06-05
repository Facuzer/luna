import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej5_b import capitalizar_primera_letra  # noqa


class Test_capitalizar_primera_letra(unittest.TestCase):
    def test_capitalizar_primera_letra_int(self):
        self.assertEqual(capitalizar_primera_letra(1), TypeError)

    def test_capitalizar_primera_letra_float(self):
        self.assertEqual(capitalizar_primera_letra(1.12837), TypeError)

    def test_capitalizar_primera_letra_lista(self):
        self.assertEqual(capitalizar_primera_letra([1, 2, 3, 4]), TypeError)
        self.assertEqual(capitalizar_primera_letra(["soy", "una", "tupla"]),
                                               TypeError)

    def test_capitalizar_primera_letra_tupla(self):
        self.assertEqual(capitalizar_primera_letra((1, 2, 3, 4)), TypeError)
        self.assertEqual(capitalizar_primera_letra(("soy", "tupla")), TypeError)

    def test_capitalizar_primera_letra_string(self):
        self.assertEqual(capitalizar_primera_letra("hola todo bien"),
                                                   "Hola Todo Bien")
        self.assertEqual(capitalizar_primera_letra("windows media center"),
                                                   "Windows Media Center")
        self.assertEqual(capitalizar_primera_letra("Hoy dia Pleno"),
                                                   "Hoy Dia Pleno")
        self.assertEqual(capitalizar_primera_letra("sOY mUY feLIZ"),
                                                   "SOY MUY FeLIZ")
        self.assertEqual(capitalizar_primera_letra("valenTIN schiaFFINO"),
                                                   "ValenTIN SchiaFFINO")
        self.assertEqual(capitalizar_primera_letra("hola señor"),
                                                   "Hola Señor")
        self.assertEqual(capitalizar_primera_letra("Futbol es de enrique"), 
                                                   "Futbol Es De Enrique")
        self.assertEqual(capitalizar_primera_letra("Complete the Monument"),
                                                   "Complete The Monument")
        self.assertEqual(capitalizar_primera_letra("Hola"),
                                                   "Hola")
        self.assertEqual(capitalizar_primera_letra("s"), "S")


unittest.main()
