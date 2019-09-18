from obstaculo import Obstaculo
from visible import Visible

class Obstaculo_movil(Obstaculo, Visible):
    def __init__(self, celda_inicial, mapa):
        self.velocidad = 0
        self.celda_actual = celda_inicial
        self.mapa = mapa