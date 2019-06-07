import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej6_d import check_palindromo  # noqa


class Test_check_palindromo(unittest.TestCase):
    def test_check_palindromo_int(self):
        self.assertEqual(check_palindromo(1), TypeError)

    def test_check_palindromo_float(self):
        self.assertEqual(check_palindromo(1.12837), TypeError)

    def test_check_palindromo_lista(self):
        self.assertEqual(check_palindromo([1, 2, 3, 4]), TypeError)
        self.assertEqual(check_palindromo(["soy", "una", "tupla"]),
                         TypeError)

    def test_check_palindromo_tupla(self):
        self.assertEqual(check_palindromo((1, 2, 3, 4)), TypeError)
        self.assertEqual(check_palindromo(("soy", "tupla")), TypeError)

    def test_check_palindromo_string(self):
        self.assertEqual(check_palindromo("hola todo bien"), False)
        self.assertEqual(check_palindromo("anita lava la tina"), True)
        self.assertEqual(check_palindromo("AnITA lAva lA tIna"), True)
        self.assertEqual(check_palindromo("asdsa"), True)
        self.assertEqual(check_palindromo("sOY mUY feLIZ"), False)
        self.assertEqual(check_palindromo("Neuquen"), True)
        self.assertEqual(check_palindromo("NEuQuEn"), True)
        self.assertEqual(check_palindromo("Neuquén"), False)
        self.assertEqual(check_palindromo(""), True)
        self.assertEqual(check_palindromo("F"), True)
        self.assertEqual(check_palindromo("Hola"), False)
        self.assertEqual(check_palindromo("s"), True)


unittest.main()
