import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej2 import calcular_fichas_domino


class Test_calcular_fichas_domino(unittest.TestCase):
    def test_calcular_fichas_domino(self):
        self.assertEqual(len(calcular_fichas_domino()), 28)
        self.assertIn((0, 0), calcular_fichas_domino())
        self.assertIn((1, 0), calcular_fichas_domino())
        self.assertIn((1, 1), calcular_fichas_domino())
        self.assertIn((2, 0), calcular_fichas_domino())
        self.assertIn((2, 1), calcular_fichas_domino())
        self.assertIn((2, 2), calcular_fichas_domino())
        self.assertIn((3, 0), calcular_fichas_domino())
        self.assertIn((3, 1), calcular_fichas_domino())
        self.assertIn((3, 2), calcular_fichas_domino())
        self.assertIn((3, 3), calcular_fichas_domino())
        self.assertIn((4, 0), calcular_fichas_domino())
        self.assertIn((4, 1), calcular_fichas_domino())
        self.assertIn((4, 2), calcular_fichas_domino())
        self.assertIn((4, 3), calcular_fichas_domino())
        self.assertIn((4, 4), calcular_fichas_domino())
        self.assertIn((5, 0), calcular_fichas_domino())
        self.assertIn((5, 1), calcular_fichas_domino())
        self.assertIn((5, 2), calcular_fichas_domino())
        self.assertIn((5, 3), calcular_fichas_domino())
        self.assertIn((5, 4), calcular_fichas_domino())
        self.assertIn((5, 5), calcular_fichas_domino())
        self.assertIn((6, 0), calcular_fichas_domino())
        self.assertIn((6, 1), calcular_fichas_domino())
        self.assertIn((6, 2), calcular_fichas_domino())
        self.assertIn((6, 3), calcular_fichas_domino())
        self.assertIn((6, 4), calcular_fichas_domino())
        self.assertIn((6, 5), calcular_fichas_domino())
        self.assertIn((6, 6), calcular_fichas_domino())


unittest.main()
