import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from ej2 import contar_vocales


class Test_contar_vocales(unittest.TestCase):
    def test_contar_vocales_int(self):
        self.assertEqual(contar_vocales(1), TypeError)
        self.assertEqual(contar_vocales(1000), TypeError)
        self.assertEqual(contar_vocales(12837283), TypeError)
    
    def test_contar_vocales_float(self):
        self.assertEqual(contar_vocales(1.12837), TypeError)
        self.assertEqual(contar_vocales(1000.128), TypeError)
        self.assertEqual(contar_vocales(12837283.8127378), TypeError)

    def test_contar_vocales_lista(self):
        self.assertEqual(contar_vocales([1, 2, 3, 4]), TypeError)
        self.assertEqual(contar_vocales(["soy", "lista"]), TypeError)

    def test_contar_vocales_tupla(self):
        self.assertEqual(contar_vocales((1, 2, 3, 4)), TypeError)
        self.assertEqual(contar_vocales(("soy", "tupla")), TypeError)

    def test_contar_vocales_string(self):
        self.assertEqual(contar_vocales("FrederickMoon"), "e")
        self.assertEqual(contar_vocales("Federico Luna"), "e")
        self.assertEqual(contar_vocales("Fede"), "e")
        self.assertEqual(contar_vocales("Luna"), "a")
        self.assertEqual(contar_vocales("Moon"), None)
        self.assertEqual(contar_vocales("AguanteLinux"), None)
        self.assertEqual(contar_vocales("LinusBenedictTorvals"), "e")
        self.assertEqual(contar_vocales("TorvalsTeQuiero"), "e")
        self.assertEqual(contar_vocales("TorvalsCapo"), "a")
        self.assertEqual(contar_vocales("WindowsCaca"), "a")
        self.assertEqual(contar_vocales("Fmoon"), None)
        self.assertEqual(contar_vocales("FMoon"), None)
        self.assertEqual(contar_vocales("FMOON"), None)
        self.assertEqual(contar_vocales("FMOon"), None)
        self.assertEqual(contar_vocales("FMOon"), None)
        self.assertEqual(contar_vocales("fMoon"), None)

        
unittest.main()