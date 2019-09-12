from celda import Celda
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'contenidos'))
from contenido_dummy import Contenido_dummy
from pared_no_rompible import Pared_no_rompible
from pared_rompible import Pared_rompible


class Mapa:
    def __init__(self, map_tiles):
        # Aca lee el mapa y crea todas las celdas.

        # Ahora voy a hacer un mapa default igual.
        self.alto = 14
        self.largo = 14
        self.celdas = []
        for _ in range(0, 14):
            self.celdas.append([])
        # Primer fila
        for i in range(0,14):
            pared_no_rompible = Pared_no_rompible()
            self.celdas[0].append(Celda(pared_no_rompible, 1, i + 1))
        # segunda fila
        pared_no_rompible = Pared_no_rompible()
        self.celdas[1].append(Celda(pared_no_rompible, 2, 1))
        for i in range(0,12):
            c_dummy = Contenido_dummy()
            self.celdas[1].append(Celda(c_dummy, 2, i + 2))
        pared_no_rompible = Pared_no_rompible()
        self.celdas[1].append(Celda(pared_no_rompible, 2, 14))
        # fila 3 a 12
        for i in range(1, 11):
            pared = True
            for j in range(0, 14):
                if pared:
                    pared_no_rompible = Pared_no_rompible()
                    self.celdas[i + 1].append(Celda(pared_no_rompible, i + 1, j + 1))
                else:
                    c_dummy = Contenido_dummy()
                    self.celdas[i + 1].append(Celda(c_dummy, i + 1, j + 1))
                pared = not pared
        # 13ava fila
        pared_no_rompible = Pared_no_rompible()
        self.celdas[12].append(Celda(pared_no_rompible, 12, 1))
        for i in range(0,12):
            c_dummy = Contenido_dummy()
            self.celdas[12].append(Celda(c_dummy, 13, i + 2))
        pared_no_rompible = Pared_no_rompible()
        self.celdas[12].append(Celda(pared_no_rompible, 13, 1))        
        # 14ava fila
        for i in range(0,14):
            pared_no_rompible = Pared_no_rompible()
            self.celdas[13].append(Celda(pared_no_rompible, 14, i + 1))
        
mt = None
mapa = Mapa(mt)



print("hola")

        