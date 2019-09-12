import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/modelo'))
from mapa import Mapa # noqa
from contenidos.contenido_dummy import Contenido_dummy
from contenidos.pared_no_rompible import Pared_no_rompible
from contenidos.pared_rompible import Pared_rompible


class Test_mapa(unittest.TestCase):
    def test_init(self):
        mapa = Mapa(None)
        self.assertEqual(len(mapa.celdas), 14)
        for i in range(0, 14):
            self.assertEqual(len(mapa.celdas[i]), 14)
        for i in (0, 13):
            for j in range(0, 14):
                self.assertEqual("Pared_no_rompible" in str(type(mapa.celdas[i][j].contenido)), True)
        for i in (1, 12):
            for j in (0, 13):
                self.assertEqual("Pared_no_rompible" in str(type(mapa.celdas[i][j].contenido)), True)
            for j in range(1, 12):
                self.assertEqual("Contenido_dummy" in str(type(mapa.celdas[i][j].contenido)), True)
        for j in (0, 13):
            for i in range(0, 13):
                self.assertEqual("Pared_no_rompible" in str(type(mapa.celdas[i][j].contenido)), True)
        

unittest.main()
    