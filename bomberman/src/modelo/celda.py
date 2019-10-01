class Celda():
    def __init__(self, contenido, fila, columna, ppc):
        self.contenido = contenido
        self.fila = fila
        self.columna = columna
        self.ppc = ppc
    
    def get_middle_pos(self):
        ppc = self.ppc
        return [self.columna*ppc - ppc/2, self.fila*ppc - ppc/2]

    def ser_explotado(self):
        pass
    
    def ser_caminado(self, caminador):
        self.contenido.ser_caminado(caminador)

    def poner_bomba(self, bomba):
        self.contenido = bomba

    def comprobar_mov(self):
        return self.contenido.comprobar_mov()

    def get_pos(self):
        pos_x = (self.columna - 1) * self.ppc
        pos_y = (self.fila - 1) * self.ppc
        return [pos_x, pos_y]

    def get_ruta_contenido(self):
        return self.contenido.get_ruta()