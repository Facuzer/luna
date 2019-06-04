import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej5_a import primera_letra_palabra  # noqa


class Test_primera_letra_palabra(unittest.TestCase):
    def test_primera_letra_palabra_int(self):
        self.assertEqual(primera_letra_palabra(1), TypeError)

    def test_primera_letra_palabra_float(self):
        self.assertEqual(primera_letra_palabra(1.12837), TypeError)

    def test_primera_letra_palabra_lista(self):
        self.assertEqual(primera_letra_palabra([1, 2, 3, 4]), TypeError)
        self.assertEqual(primera_letra_palabra(["soy", "una", "tupla"]),
                                               TypeError)


    def test_primera_letra_palabra_tupla(self):
        self.assertEqual(primera_letra_palabra((1, 2, 3, 4)), TypeError)
        self.assertEqual(primera_letra_palabra(("soy", "tupla")), TypeError)

    def test_primera_letra_palabra_string(self):
        self.assertEqual(primera_letra_palabra("Universal Serie Bus"), "USB")
        self.assertEqual(primera_letra_palabra("Windows Media Center"), "WMC")
        self.assertEqual(primera_letra_palabra("Hoy Dia Pleno"), "HDP")
        self.assertEqual(primera_letra_palabra("W"), "W")
        self.assertEqual(primera_letra_palabra("Valentin Schiaffino"), "VS")
        self.assertEqual(primera_letra_palabra("hola todo bien"), "HTB")
        self.assertEqual(primera_letra_palabra("Futbol es de enrique"), "FEDE")
        self.assertEqual(primera_letra_palabra("Complete the Monument"), "CTM")
        self.assertEqual(primera_letra_palabra("Hola"), "H")
        self.assertEqual(primera_letra_palabra("s"), "S")


unittest.main()
