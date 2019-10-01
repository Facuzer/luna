from visible import Visible
from contenido import Contenido

class Obstaculo_movil(Visible, Contenido):
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial.get_middle_pos())
        self.velocidad = 0
        self.celda_actual = celda_inicial
        self.mapa = mapa   
    
    def morir(self):
        pass

    def comprobar_mov(self):
        return True
    
    def _mover(self, mov_x, mov_y):
        pos_tentativa = (self._get_pos_x() + mov_x, self._get_pos_y() + mov_y)
        if self.mapa.comprobar_mov(pos_tentativa):
            self._set_pos(pos_tentativa)
            self.celda_actual = self.mapa.avisar_mov(self.pos, self.celda_actual, self)