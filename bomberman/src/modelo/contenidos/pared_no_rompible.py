from objeto import Objeto

class Pared_no_rompible(Objeto):
    def __init__(self):
        self.ruta = "img/pared_no_rompible.png"
    
    def comprobar_mov(self):
        return False