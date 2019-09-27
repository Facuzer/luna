from objeto import Objeto

class Pared_no_rompible(Objeto):
    def __init__(self):
        pass
    
    def comprobar_mov(self):
        return False