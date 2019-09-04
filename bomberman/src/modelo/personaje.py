from obstaculo_movil import Obstaculo_movil

class Personaje(Obstaculo_movil):
    def __init__(self, mapa, celda_inicial):
        self.mapa = mapa
        self.celda_actual = celda_inicial
        return self