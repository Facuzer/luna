from modelo.contenidos.obstaculo_movil import Obstaculo_movil

class Personaje(Obstaculo_movil):
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial, mapa)
        self.velocidad = 10
        self.vidas = 3
        self.delay_bomba = 3
        self.nivel_explosion = 1
    
    def get_posicion(self):
        return self.pos

    def mover_arriba(self):
        self._mover(0,-self.velocidad)
    
    def mover_derecha(self):
        self._mover(self.velocidad, 0)
    
    def mover_abajo(self):
        self._mover(0,self.velocidad)
    
    def mover_izquierda(self):
        self._mover(-self.velocidad, 0)
    
    def poner_bomba(self):
        bomba = Bomba(self.nivel_explosion, self.delay_bomba, self.mapa)
        self.mapa.poner_bomba(bomba,self.celda_actual)
    
    def _set_celda_actual(self, celda_actual):
        self.celda_actual = celda_actual
    
    def _get_celda_actual(self, celda_actual):
        return self.celda_actual