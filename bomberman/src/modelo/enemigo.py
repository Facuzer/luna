from obstaculo_movil import Obstaculo_movil

class Enemigo(Obstaculo_movil):
    def mover_arriba(self):
        self.mover(0,-self.velocidad)

    def mover_derecha(self):
        self.mover(self.velocidad, 0)
    
    def mover_abajo(self):
        self.mover(0,self.velocidad)
    
    def mover_izquierda(self):
        self.mover(-self.velocidad, 0)

    def _mover_random(self):
        pass