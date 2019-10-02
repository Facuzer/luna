from modelo.contenidos.obstaculo_movil import Obstaculo_movil

class Personaje(Obstaculo_movil):
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial, mapa)
        self.velocidad = 10
        self.vidas = 3
        self.delay_bomba = 3
        self.img_index = 0
        self.nivel_explosion = 1
        self.direccion = "abajo"
    
    def get_posicion(self):
        return self.pos

    def mover_arriba(self):
        self._mover(0,-self.velocidad)
        self._cambiar_index("arriba")
        self.direccion = "arriba"
    
    def mover_derecha(self):
        self._mover(self.velocidad, 0)
        self._cambiar_index("derecha")
        self.direccion = "derecha"
    
    def mover_abajo(self):
        self._mover(0,self.velocidad)
        self._cambiar_index("abajo")
        self.direccion = "abajo"

    
    def mover_izquierda(self):
        self._mover(-self.velocidad, 0)
        self._cambiar_index("izquierda")
        self.direccion = "izquierda"
    
    def _cambiar_index(self, direccionLlamado):
        if self.direccion != direccionLlamado:
            self.img_index = 0
        else:
            if self.img_index == 7:
                self.img_index = 0
            else:
                self.img_index += 1
    
    def poner_bomba(self):
        bomba = Bomba(self.nivel_explosion, self.delay_bomba, self.mapa)
        self.mapa.poner_bomba(bomba,self.celda_actual)
    
    def _set_celda_actual(self, celda_actual):
        self.celda_actual = celda_actual
    
    def _get_celda_actual(self, celda_actual):
        return self.celda_actual
    
    def get_direccion(self):
        return self.direccion
    
    def get_index_img(self):
        return self.img_index