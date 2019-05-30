import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from ej3 import contar_todas_las_vocales


class Test_contar_todas_las_vocales(unittest.TestCase):
    def test_contar_todas_las_vocales_int(self):
        self.assertEqual(contar_todas_las_vocales(1), TypeError)
        self.assertEqual(contar_todas_las_vocales(1000), TypeError)
        self.assertEqual(contar_todas_las_vocales(12837283), TypeError)
    
    def test_contar_todas_las_vocales_float(self):
        self.assertEqual(contar_todas_las_vocales(1.12837), TypeError)
        self.assertEqual(contar_todas_las_vocales(1000.128), TypeError)
        self.assertEqual(contar_todas_las_vocales(12837283.8127378), TypeError)

    def test_contar_todas_las_vocales_lista(self):
        self.assertEqual(contar_todas_las_vocales([1, 2, 3, 4]), TypeError)
        self.assertEqual(contar_todas_las_vocales(["soy", "lista"]), TypeError)

    def test_contar_todas_las_vocales_tupla(self):
        self.assertEqual(contar_todas_las_vocales((1, 2, 3, 4)), TypeError)
        self.assertEqual(contar_todas_las_vocales(("soy", "tupla")), TypeError)

    def test_contar_todas_las_vocales_string(self):
        self.assertEqual(contar_todas_las_vocales("Hola como estas"),
                                                 (2, 1, 0, 3, 0))
        self.assertEqual(contar_todas_las_vocales("HOlA COmo EstAs"),
                                                 (2, 1, 0, 3, 0))
        self.assertEqual(contar_todas_las_vocales("Me gusta el queso"),
                                                 (1, 3, 0, 1, 1))
        self.assertEqual(contar_todas_las_vocales("Me gUstA El quEsO"),
                                                 (1, 3, 0, 1, 1))
        self.assertEqual(contar_todas_las_vocales("Moon"), (0, 0, 0, 2, 0))
        self.assertEqual(contar_todas_las_vocales("MOon"), (0, 0, 0, 2, 0))
        self.assertEqual(contar_todas_las_vocales("AguanteLinux"),
                                                 (2, 1, 1, 0, 2))
        self.assertEqual(contar_todas_las_vocales("AgUAnteLinUx"),
                                                 (2, 1, 1, 0, 2))
        self.assertEqual(contar_todas_las_vocales("LinusBenedictTorvals"),
                                                 (1, 2, 2, 1, 1))
        self.assertEqual(contar_todas_las_vocales("TorvalsTeQuiero"),
                                                 (1, 2, 1, 2, 0))

        
unittest.main()