import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from visible import Visible
from contenido import Contenido

class Objeto(Visible, Contenido):
    def __init__(self):
        pass
    
    
