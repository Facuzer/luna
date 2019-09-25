from obstaculo import Obstaculo
from visible import Visible
from contenido import Contenido

class Obstaculo_movil(Obstaculo, Visible, Contenido):
    def __init__(self, celda_inicial, mapa):
        self.velocidad = 0
        self.celda_actual = celda_inicial
        self.mapa = mapa

    def __mover(self, mov_x, mov_y):
        pos_tentativa = (self.pos[0] + mov_x, self.pos[1] + mov_y)
        if self.mapa.comprobar_mov(pos_tentativa):
            self.celda_actual = self.mapa.avisar_mov(self.pos, self.celda_actual, self)

        
        
        
    
    def morir(self):
        pass