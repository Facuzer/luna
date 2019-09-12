from contenido import Contenido
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from obstaculo import Obstaculo
class Bomba(Obstaculo, Contenido):
    def __init__(self):
        pass