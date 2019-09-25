from objeto import Objeto
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from obstaculo import Obstaculo


class Bomba(Obstaculo, Objeto):
    def __init__(self, nivel_explosion, delay, mapa):
        self.nivel_explosion = nivel_explosion
        self.delay = delay
        self.mapa = mapa
    
    def explotar(self):
        pass
        