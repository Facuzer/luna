from obstaculo import Obstaculo
from visible import Visible
from contenido import Contenido

class Obstaculo_movil(Obstaculo, Visible, Contenido):
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial.get_middle_pos())
        self.velocidad = 0
        self.celda_actual = celda_inicial
        self.mapa = mapa   
    
    def morir(self):
        pass

    def comprobar_mov(self):
        return True
    
    def __mover(self, mov_x, mov_y):
        pos_tentativa = (self.__get_pos_x() + mov_x, self.__get_pos_y() + mov_y)
        if self.mapa.comprobar_mov(pos_tentativa):
            self.__set_pos(pos_tentativa)
            self.celda_actual = self.mapa.avisar_mov(self.pos, self.celda_actual, self)