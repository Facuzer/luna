class Celda():
    def __init__(self, contenido, fila, columna):
        self.contenido = contenido
        self.fila = fila
        self.columna = columna
    
    def ser_explotado(self):
        pass
    
    def ser_caminado(self, caminador):
        self.contenido.ser_caminado(caminador)

    def poner_bomba(self, bomba):
        pass