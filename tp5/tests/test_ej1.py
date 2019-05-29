import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from ej1 import verificar_contraseña

class Test_verificar_contraseña(unittest.TestCase):
    def test_verificar_contraseña_int(self):
        self.assertEqual(verificar_contraseña(1), TypeError)
        self.assertEqual(verificar_contraseña(1000), TypeError)
        self.assertEqual(verificar_contraseña(12837283), TypeError)
    
    def test_verificar_contraseña_float(self):
        self.assertEqual(verificar_contraseña(1.12837), TypeError)
        self.assertEqual(verificar_contraseña(1000.128), TypeError)
        self.assertEqual(verificar_contraseña(12837283.8127378), TypeError)

    def test_verificar_contraseña_lista(self):
        self.assertEqual(verificar_contraseña([1, 2, 3, 4]), TypeError)
        self.assertEqual(verificar_contraseña(["soy", "lista"]), TypeError)

    def test_verificar_contraseña_tupla(self):
        self.assertEqual(verificar_contraseña((1, 2, 3, 4)), TypeError)
        self.assertEqual(verificar_contraseña(("soy", "tupla")), TypeError)


    def test_verificar_contraseña_string(self):
        self.assertEqual(verificar_contraseña("FrederickMoon"), False)
        self.assertEqual(verificar_contraseña("Federico Luna"), False)
        self.assertEqual(verificar_contraseña("Fede"), False)
        self.assertEqual(verificar_contraseña("Luna"), False)
        self.assertEqual(verificar_contraseña("Moon"), False)
        self.assertEqual(verificar_contraseña("AguanteLinux"), False)
        self.assertEqual(verificar_contraseña("LinusBenedictTorvals"), False)
        self.assertEqual(verificar_contraseña("TorvalsTeQuiero"), False)
        self.assertEqual(verificar_contraseña("TorvalsCapo"), False)
        self.assertEqual(verificar_contraseña("WindowsCaca"), False)
        self.assertEqual(verificar_contraseña("Fmoon"), False)
        self.assertEqual(verificar_contraseña("FMoon"), False)
        self.assertEqual(verificar_contraseña("FMOON"), False)
        self.assertEqual(verificar_contraseña("FMOon"), False)
        self.assertEqual(verificar_contraseña("FMOon"), False)
        self.assertEqual(verificar_contraseña("fMoon"), True)

        

unittest.main()