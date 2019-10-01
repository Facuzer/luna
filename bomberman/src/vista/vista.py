import pygame
path = "C:/Users/huergo/luna/bomberman/"

class Vista():
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.dimensiones = (600, 600)
        self.fondo = None
        self.screen = pygame.display.set_mode(self.dimensiones)
        self.bomberman = None
        pygame.key.set_repeat(10)

    def cargar_imagen_fondo(self, path_fondo):
        self.fondo = pygame.image.load(path_fondo)
        self.recargar_fondo()

    def cargar_imagen_bomberman(self, sprite_path, pos):
        self.bomberman = pygame.image.load(sprite_path)
        self.pos_bomberman = pos
        self.recargar_bomberman()

    def recargar_fondo(self):
        self.screen.blit(self.fondo, [0,0])
    
    def recargar_bomberman(self):
        self.screen.blit(self.bomberman, self.game.get_posicion_personaje())

    def recargar_contenidos(self):
        celdas = self.game.get_all_celdas() 
        for fila in celdas:
            for celda in fila:
                self.screen.blit(pygame.image.load(path + celda.get_ruta_contenido()), celda.get_pos())
