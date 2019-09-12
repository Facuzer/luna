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
        self.celdas.append([], [], [], [], [], [],
                    [], [], [], [], [], [],[])
        # Primer fila
        for _ in range(0,14):
            pared_no_rompible = Pared_no_rompible()
            self.celdas[0].append(Celda(pared_no_rompible))
        # segunda fila
        pared_no_rompible = Pared_no_rompible()
        self.celdas[1].append(Celda(pared_no_rompible))
        for _ in range(0,13):
            c_dummy = Contenido_dummy()
            self.celdas[0].append(Celda(c_dummy))
        # fila 3 a 11
        for i in range(2, 11):
            pared = True
            for _ in range(0, 14):
                if pared:
                    pared_no_rompible = Pared_no_rompible()
                    self.celdas[i].append(Celda(pared_no_rompible))
                else:
                    c_dummy = Contenido_dummy()
                    self.celdas[i].append(Celda(c_dummy))
                pared = not pared
        # 12ava fila
        pared_no_rompible = Pared_no_rompible()
        self.celdas[1].append(Celda(pared_no_rompible))
        for _ in range(0,13):
            c_dummy = Contenido_dummy()
            self.celdas[0].append(Celda(c_dummy))
        # Ultima fila
        for _ in range(0,14):
            pared_no_rompible = Pared_no_rompible()
            self.celdas[0].append(Celda(pared_no_rompible))
        



        

        