import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.ej5 import matriz_identidad


class Test_matriz_identidad(unittest.TestCase):
    def test_matriz_identidad_string(self):
        self.assertEqual(matriz_identidad("Hola fede"), None)
        self.assertEqual(matriz_identidad("15"), None)

    def test_matriz_identidad_lista(self):
        self.assertEqual(matriz_identidad([1, 2, 3]), None)
        self.assertEqual(matriz_identidad(["hola", 2, 3]), None)
        self.assertEqual(matriz_identidad(["hola", "hola", "hola"]), None)

    def test_matriz_identidad_tupla(self):
        self.assertEqual(matriz_identidad((1, 2, 3)), None)
        self.assertEqual(matriz_identidad(("hola", 2, 3)), None)
        self.assertEqual(matriz_identidad(("hola", "hola", "hola")), None)

    def test_matriz_identidad_neg(self):
        self.assertEqual(matriz_identidad(-1), None)
        self.assertEqual(matriz_identidad(-0.00001), None)
        self.assertEqual(matriz_identidad(-128371287), None)
        

    def test_matriz_identidad_float(self):
        self.assertEqual(matriz_identidad(0.9999999999999), None)
        self.assertEqual(matriz_identidad(0.1), None)
        self.assertEqual(matriz_identidad(1.1), None)
        self.assertEqual(matriz_identidad(32.23872837), None)
        
    def test_matriz_identidad_mayor_50(self):
        self.assertEqual(matriz_identidad(51), None)
        self.assertEqual(matriz_identidad(50.00000001), None)
        self.assertEqual(matriz_identidad(5978283478374), None)

    def test_matriz_identidad_cinco(self):
        # Testeo la primera matriz con 5
        matriz = matriz_identidad(5)
        # Tiene que tener n² + n objetos, ya que por cada salto de linea
        # le agrego un "_" a la matriz
        self.assertEqual(len(matriz), 30)
        # Ahora me quiero fijar cuantos unos hay, si está bien tendria que
        # haber n 1's
        total_unos = 0
        for valor in matriz:
            if isinstance(valor, int):
                total_unos += valor
        self.assertEqual(total_unos, 5)
        # Ahora me quiero fijar si están bien en su posición los unos.
        # Para hacer esto voy a recorrer la lista y fijarme si cada n + 2
        # (le sumo 1 ya que uso mi valor centinela "_" y 1 mas por la
        # iteracion de más) hay un 1. 
        aux = 7
        for valor in matriz:
            if isinstance(valor, int):
                if valor == 1:
                   self.assertEqual(aux, 7)
                   aux = 0
            aux+=1

    def test_matriz_identidad_diecisiete(self):
        # Testeo la matriz con 17
        matriz = matriz_identidad(17)
        # Tiene que tener n² + n objetos, ya que por cada salto de linea
        # le agrego un "_" a la matriz
        self.assertEqual(len(matriz), 306)
        # Ahora me quiero fijar cuantos unos hay, si está bien tendria que
        # haber n 1's
        total_unos = 0
        for valor in matriz:
            if isinstance(valor, int):
                total_unos += valor
        self.assertEqual(total_unos, 17)
        # Ahora me quiero fijar si están bien en su posición los unos.
        # Para hacer esto voy a recorrer la lista y fijarme si cada n + 2
        # (le sumo 1 ya que uso mi valor centinela "_" y 1 mas por la
        # iteracion de más) hay un 1. 
        aux = 19
        for valor in matriz:
            if isinstance(valor, int):
                if valor == 1:
                   self.assertEqual(aux, 19)
                   aux = 0
            aux+=1
        
    def test_matriz_identidad_cuarenta_y_nueve(self):
        # Testeo la matriz con 49, n = 49
        matriz = matriz_identidad(49)
        # Tiene que tener n² + n objetos, ya que por cada salto de linea
        # le agrego un "_" a la matriz
        self.assertEqual(len(matriz), 2450)
        # Ahora me quiero fijar cuantos unos hay, si está bien tendria que
        # haber n 1's
        total_unos = 0
        for valor in matriz:
            if isinstance(valor, int):
                total_unos += valor
        self.assertEqual(total_unos, 49)
        # Ahora me quiero fijar si están bien en su posición los unos.
        # Para hacer esto voy a recorrer la lista y fijarme si cada n + 2
        # (le sumo 1 ya que uso mi valor centinela "_" y 1 mas por la
        # iteracion de más) hay un 1. 
        aux = 51
        for valor in matriz:
            if isinstance(valor, int):
                if valor == 1:
                   self.assertEqual(aux, 51)
                   aux = 0
            aux+=1


unittest.main()