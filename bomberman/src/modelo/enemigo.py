from obstaculo_movil import Obstaculo_movil

class Enemigo(Obstaculo_movil):
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial, mapa)
        self.velocidad = 6

    def _mover_random(self):
        pass