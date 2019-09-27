import pygame

class Vista():
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.dimensiones = (640, 480)
        self.fondo = None
        self.screen = pygame.display.set_mode(self.dimensiones)
        self.bomberman = None
        pygame.key.set_repeat(20)

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