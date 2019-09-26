class Celda():
    def __init__(self, contenido, fila, columna):
        self.contenido = contenido
        self.fila = fila
        self.columna = columna
    
    def get_middle_pos(self):
        ppc = 20
        return [self.columna*ppc - ppc/2, self.fila*ppc - ppc/2]

    def ser_explotado(self):
        pass
    
    def ser_caminado(self, caminador):
        self.contenido.ser_caminado(caminador)

    def poner_bomba(self, bomba):
        self.contenido = bomba