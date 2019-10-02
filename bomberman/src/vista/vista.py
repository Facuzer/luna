import pygame
path = "C:/Users/huergo/Desktop/luna/bomberman/"


class Vista():
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.dimensiones = (675, 675)
        self.fondo = None
        self.screen = pygame.display.set_mode(self.dimensiones)
        self.bomberman = None
        imagenesBack = []
        imagenesFront = []
        imagenesSide = []
        self.imagenes = {"back" : imagenesBack, "front" : imagenesFront, "side" : imagenesSide}
        pygame.key.set_repeat(10)

    def cargar_imagen_fondo(self, path_fondo):
        self.fondo = pygame.image.load(path_fondo)
        self.recargar_fondo()

    def cargar_imagenes_bomberman(self, path, pos):
        for i in range(1, 9):
            imgP = path + "img/bman/Back/" + "b0" + str(i) + ".png"
            self.imagenes["back"].append(pygame.image.load(imgP))
        for i in range(1, 9):
            imgP = path + "img/bman/Front/" + "f0" + str(i) + ".png"
            self.imagenes["front"].append(pygame.image.load(imgP))
        for i in range(1, 9):
            imgP = path + "img/bman/Side/" + "s0" + str(i) + ".png"
            self.imagenes["side"].append(pygame.image.load(imgP))
        self.bomberman = self.imagenes["front"][0]
        self.pos_bomberman = pos
        self.recargar_bomberman()

    def recargar_fondo(self):
        self.screen.blit(self.fondo, [0,0])
    
    def recargar_bomberman(self):
        rotar = False
        # calculo direccion
        direcc = self.game.get_direccion_bm()
        if direcc == "arriba":
            imagenes = self.imagenes["back"]
        elif direcc == "abajo":
            imagenes = self.imagenes["front"]
        else:
            if direcc == "izquierda":
                rotar = True
            imagenes = self.imagenes["side"]
        posImg = self.game.get_index_bm()
        self.bomberman = imagenes[posImg]
        # print(posImg)
        if rotar:
            self.bomberman = pygame.transform.flip(self.bomberman, True, False)
        pos_bomb = self.game.get_posicion_personaje()
        pos_bomb = (int(pos_bomb[0]), int(pos_bomb[1]))
        rect = self.bomberman.get_rect()
        rect.centerx = pos_bomb[0]
        rect.centery = pos_bomb[1] - 35
        self.screen.blit(self.bomberman, rect)
        # pygame.draw.circle(self.screen, pygame.Color(230, 95, 0), pos_bomb, 5)

    def recargar_contenidos(self):

        celdas = self.game.get_all_celdas() 
        for fila in celdas:
            for celda in fila:
                self.screen.blit(pygame.image.load(path + celda.get_ruta_contenido()), celda.get_pos())
