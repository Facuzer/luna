from obstaculo_movil import Obstaculo_movil

class Personaje(Obstaculo_movil):
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial, mapa)
        self.velocidad = 10
        self.vidas = 3
    
    def mover_arriba(self):
        pass
    
    def mover_derecha(self):
        pass
    
    def mover_abajo(self):
        pass
    
    def mover_izquierda(self):
        pass
    
    def poner_bomba(self):
        pass
    
    def __set_celda_actual(self, celda_actual):
        self.celda_actual = celda_actual
    
    def __get_celda_actual(self, celda_actual):
        return self.celda_actual