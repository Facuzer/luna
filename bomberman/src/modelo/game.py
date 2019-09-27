from modelo.mapa import Mapa
from modelo.personaje import Personaje
from modelo.input_controller import Input_controller
from modelo.enemigo import Enemigo

class Game():
    def __init__(self):
        # Aca se supone que lee un archivo.
        map_tiles = None
        self.mapa = Mapa(map_tiles)
        # Aca lee otro archivo
        player_conf = None
        self.ic = Input_controller(player_conf)
        # Aca lee donde esta parado el personaje.
        fila_pj = 1
        col_pj = 1
        celda_pj = self.mapa.get_celda(fila_pj, col_pj)
        self.personaje = Personaje(celda_pj, self.mapa)
        # Aca lee donde está cada enemigo y los crea.
        pos_enemigos = [(2, 2), (2, 3), (5, 1)]
        self.lista_de_enemigos = []
        for pos_enemigo in pos_enemigos:
            self.lista_de_enemigos.append(Enemigo(self.mapa.get_celda(pos_enemigo[0], pos_enemigo[1]), self.mapa))
    
    def get_posicion_personaje(self):
        return self.personaje.get_posicion()
    
    def mover_bomberman(self, direccion):
        if (direccion == [-1, 0]):
            self.personaje.mover_izquierda()
        elif (direccion ==  [1, 0]):
            self.personaje.mover_derecha()
        elif (direccion == [0, -1]):
            self.personaje.mover_abajo()
        elif (direccion == [0, 1]):
            self.personaje.mover_arriba()

