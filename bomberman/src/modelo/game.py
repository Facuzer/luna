from mapa import Mapa
from input_controller import Input_controller

class Game():
    def __init__(self):
        # Aca se supone que lee un archivo.
        map_tiles = None
        self.mapa = Mapa(map_tiles)
        # Aca lee otro archivo
        player_conf = None
        self.ic = Input_controller()
        # Aca lee donde esta parado el personaje.
        fila_pj = 1
        col_pj = 1
        celda_pj = self.mapa.get_celdas(fila_pj, col_pj)
        self.personaje = Personaje(self, celda_pj)
        # Aca lee donde está cada enemigo y los crea.
        pos_enemigos = [(1, 2), (2, 3), (5, 1)]
        self.lista_de_enemigos = []
        for pos_enemigo in pos_enemigos:
            self.lista_de_enemigos.append(Enemigo(pos_enemigo))
    
    def get_posicion_personaje():
        return self.personaje.get_posicion()

