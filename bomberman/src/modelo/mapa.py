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
        alto = 15
        largo = 15
        self.__init__(map_tiles, alto, largo)
        # Ahora voy a hacer un mapa default igual.


    def __init__(self, alto, largo):
        self.alto = alto
        self.largo = largo
        self.celdas = []
        for _ in range (0,self.alto):
            self.celdas.append([])
        # Primer fila
        for i in range(1, self.largo + 1):
            contenido = Pared_no_rompible()
            self.celdas[0].append(Celda(contenido, 1, i))
        # filas del medio
        for i in range(2, self.alto):
            contenido = Pared_no_rompible()
            self.celdas[i - 1].append(Celda(contenido, i, 1))
            for j in range(2, self.largo):
                if(i % 2 == 0):
                    # Dummy
                    contenido = Contenido_dummy()
                    self.celdas[i - 1].append(Celda(contenido, i, j))
                else:
                    # Paredes
                    if(j % 2 == 0):
                        contenido = Contenido_dummy()
                    else:
                        contenido = Pared_no_rompible()
                    self.celdas[i - 1].append(Celda(contenido, i, j))
            contenido = Pared_no_rompible()
            self.celdas[i - 1].append(Celda(contenido, i, self.largo))
        # Ultima fila
        for i in range(1, self.largo + 1):
            contenido = Pared_no_rompible()
            self.celdas[self.alto - 1].append(Celda(contenido, self.largo, i))

        