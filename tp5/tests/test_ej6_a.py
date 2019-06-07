import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from ej6_a import solo_consonantes  # noqa


class Test_solo_consonantes(unittest.TestCase):
    def test_solo_consonantes_int(self):
        self.assertEqual(solo_consonantes(1), TypeError)

    def test_solo_consonantes_float(self):
        self.assertEqual(solo_consonantes(1.12837), TypeError)

    def test_solo_consonantes_lista(self):
        self.assertEqual(solo_consonantes([1, 2, 3, 4]), TypeError)
        self.assertEqual(solo_consonantes(["soy", "una", "tupla"]), TypeError)

    def test_solo_consonantes_tupla(self):
        self.assertEqual(solo_consonantes((1, 2, 3, 4)), TypeError)
        self.assertEqual(solo_consonantes(("soy", "tupla")), TypeError)

    def test_solo_consonantes_string(self):
        self.assertEqual(solo_consonantes("hola todo bien"), "hl td bn")
        self.assertEqual(solo_consonantes("windows media center"),
                         "wndws md cntr")
        self.assertEqual(solo_consonantes("ayer me aguante"),
                         "yr m gnt")
        self.assertEqual(solo_consonantes("amaneci muy almanaque"),
                         "mnc my lmnq")
        self.assertEqual(solo_consonantes(
                         "avión hola aeropuerto ala delta"),
                         "vn hl rprt l dlt")
        self.assertEqual(solo_consonantes("AGUANTE EL AGUA AZUL"),
                         "GNT L G ZL")
        self.assertEqual(solo_consonantes("áááábbbbbbbcccccddd"),
                         "bbbbbbbcccccddd")
        self.assertEqual(solo_consonantes("íííóóóúúúfede"), "fd")
        self.assertEqual(solo_consonantes("Laaeiocaeioudaeotaem"), "Lcdtm")

unittest.main()
