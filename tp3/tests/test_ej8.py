import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej8 import anio_en_numeros_romanos


class Test_anio_en_numeros_romanos(unittest.TestCase):
    def test_anio_en_numeros_romanos_string(self):
        self.assertEqual(anio_en_numeros_romanos("Quince"), None)
        self.assertEqual(anio_en_numeros_romanos("Diecisiete"), None)
        self.assertEqual(anio_en_numeros_romanos("Hola Frederick Moon"), None)

    def test_anio_en_numeros_romanos_float(self):
        self.assertEqual(anio_en_numeros_romanos(0.00000000001), None)
        self.assertEqual(anio_en_numeros_romanos(1.18927387), None)
        self.assertEqual(anio_en_numeros_romanos(1.1), None)
        self.assertEqual(anio_en_numeros_romanos(52.1298378), None)
        self.assertEqual(anio_en_numeros_romanos(1000000.0213), None)

    def test_anio_en_numeros_romanos_lista(self):
        self.assertEqual(anio_en_numeros_romanos(["Ciento", "Veinticuatro"]), None)

    def test_anio_en_numeros_romanos_tupla(self):
        self.assertEqual(anio_en_numeros_romanos(("Ciento", "Veinticuatro")), None)
        

    def test_anio_en_numeros_romanos_neg(self):
        self.assertEqual(anio_en_numeros_romanos(0), None)
        self.assertEqual(anio_en_numeros_romanos(-12736), None)
        self.assertEqual(anio_en_numeros_romanos(-76213.78123), None)
        self.assertEqual(anio_en_numeros_romanos(-0.000000001), None)

    def test_anio_en_numeros_romanos_mayor(self):
        self.assertEqual(anio_en_numeros_romanos(1000001), None)
        self.assertEqual(anio_en_numeros_romanos(1891237891273912), None)

    def test_anio_en_numeros_romanos_int(self):
        self.assertEqual(anio_en_numeros_romanos(1), "I")
        self.assertEqual(anio_en_numeros_romanos(2), "II")
        self.assertEqual(anio_en_numeros_romanos(3), "III")
        self.assertEqual(anio_en_numeros_romanos(4), "IV")
        self.assertEqual(anio_en_numeros_romanos(5), "V")
        self.assertEqual(anio_en_numeros_romanos(6), "VI")
        self.assertEqual(anio_en_numeros_romanos(7), "VII")
        self.assertEqual(anio_en_numeros_romanos(8), "VIII")
        self.assertEqual(anio_en_numeros_romanos(9), "IX")
        self.assertEqual(anio_en_numeros_romanos(10), "X")
        self.assertEqual(anio_en_numeros_romanos(20), "XX")
        self.assertEqual(anio_en_numeros_romanos(30), "XXX")
        self.assertEqual(anio_en_numeros_romanos(40), "XL")
        self.assertEqual(anio_en_numeros_romanos(50), "L")
        self.assertEqual(anio_en_numeros_romanos(60), "LX")
        self.assertEqual(anio_en_numeros_romanos(70), "LXX")
        self.assertEqual(anio_en_numeros_romanos(80), "LXXX")
        self.assertEqual(anio_en_numeros_romanos(90), "XC")
        self.assertEqual(anio_en_numeros_romanos(100), "C")
        self.assertEqual(anio_en_numeros_romanos(200), "CC")
        self.assertEqual(anio_en_numeros_romanos(300), "CCC")
        self.assertEqual(anio_en_numeros_romanos(400), "CD")
        self.assertEqual(anio_en_numeros_romanos(500), "D")
        self.assertEqual(anio_en_numeros_romanos(600), "DC")
        self.assertEqual(anio_en_numeros_romanos(700), "DCC")
        self.assertEqual(anio_en_numeros_romanos(800), "DCCC")
        self.assertEqual(anio_en_numeros_romanos(900), "CM")
        self.assertEqual(anio_en_numeros_romanos(1000), "M")
        self.assertEqual(anio_en_numeros_romanos(2000), "MM")
        self.assertEqual(anio_en_numeros_romanos(3000), "MMM")
        self.assertEqual(anio_en_numeros_romanos(4000), "I\u0305V\u0305")
        self.assertEqual(anio_en_numeros_romanos(5000), "V\u0305")
        self.assertEqual(anio_en_numeros_romanos(6000), "V\u0305I\u0305")
        self.assertEqual(anio_en_numeros_romanos(7000), "V\u0305I\u0305I\u0305")
        self.assertEqual(anio_en_numeros_romanos(8000), 
                         "V\u0305I\u0305I\u0305I\u0305")
        self.assertEqual(anio_en_numeros_romanos(9000), "I\u0305X\u0305")
        self.assertEqual(anio_en_numeros_romanos(10000), "X\u0305")
        self.assertEqual(anio_en_numeros_romanos(20000), "X\u0305X\u0305")
        self.assertEqual(anio_en_numeros_romanos(30000), 
                         "X\u0305X\u0305X\u0305")
        self.assertEqual(anio_en_numeros_romanos(40000), "X\u0305L\u0305")
        self.assertEqual(anio_en_numeros_romanos(50000), "L\u0305")
        self.assertEqual(anio_en_numeros_romanos(60000), "L\u0305X\u0305")
        self.assertEqual(anio_en_numeros_romanos(70000), 
                         "L\u0305X\u0305X\u0305")
        self.assertEqual(anio_en_numeros_romanos(80000), 
                         "L\u0305X\u0305X\u0305X\u0305")
        self.assertEqual(anio_en_numeros_romanos(90000), 
                         "X\u0305C\u0305")
        self.assertEqual(anio_en_numeros_romanos(100000),"C\u0305")
        self.assertEqual(anio_en_numeros_romanos(200000), "C\u0305C\u0305")
        self.assertEqual(anio_en_numeros_romanos(300000),
                         "C\u0305C\u0305C\u0305")
        self.assertEqual(anio_en_numeros_romanos(400000), "C\u0305D\u0305")
        self.assertEqual(anio_en_numeros_romanos(500000), "D\u0305")
        self.assertEqual(anio_en_numeros_romanos(600000), "D\u0305C\u0305")
        self.assertEqual(anio_en_numeros_romanos(700000),
                         "D\u0305C\u0305C\u0305")
        self.assertEqual(anio_en_numeros_romanos(800000),
                         "D\u0305C\u0305C\u0305C\u0305")
        self.assertEqual(anio_en_numeros_romanos(900000), "C\u0305M\u0305")
        self.assertEqual(anio_en_numeros_romanos(1000000), "M\u0305")

unittest.main()
