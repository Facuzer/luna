import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from contenido import Contenido

class Power_up(Contenido):
    def __init__(self):
        pass

    def comprobar_mov(self):
        return True