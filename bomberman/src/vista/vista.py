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
        imagenesBmBack = []
        imagenesBmFront = []
        imagenesBmSide = []
        self.imagenesBm = {"back" : imagenesEnemyBack, "front" : imagenesEnemyFront, "side" : imagenesEnemySide}
        imagenesEnemyBack = []
        imagenesEnemyFront = []
        imagenesEnemySide = []
        self.imagenesEnemy = {"back" : imagenesEnemyBack, "front" : imagenesEnemyFront, "side" : imagenesEnemySide}
        pygame.key.set_repeat(10)

    def cargar_imagen_fondo(self, path_fondo):
        self.fondo = pygame.image.load(path_fondo)
        self.recargar_fondo()

    def cargar_imagenes_enemigo(self, path):
        self.cargar_imagenes_om(path, self.imagenesEnemy, "enemy", 6)
    
    def cargar_imagenes_bomberman(self, path, pos):
        self.cargar_imagenes_om(path, self.imagenesBm, "bman", 8)
        self.bomberman = self.imagenesEnemy["front"][0]
        self.pos_bomberman = pos
        self.recargar_bomberman()
    
    def cargar_imagenes_om(self, path, lista_om, nombre_om, lenght):
        for i in range(1, lenght + 1):
            imgP = path + "img/" + nombre_om + "/Back/" + "b0" + str(i) + ".png"
            lista_om["back"].append(pygame.image.load(imgP))
        for i in range(1, lenght + 1):
            imgP = path + "img/" + nombre_om + "/Front/" + "f0" + str(i) + ".png"
            lista_om["front"].append(pygame.image.load(imgP))
        for i in range(1, lenght + 1):
            imgP = path + "img/" + nombre_om + "/Side/" + "s0" + str(i) + ".png"
            lista_om["side"].append(pygame.image.load(imgP))

    def recargar_fondo(self):
        self.screen.blit(self.fondo, [0,0])
    
    def recargar_bomberman(self):
        rotar = False
        # calculo direccion
        direcc = self.game.get_direccion_bm()
        if direcc == "arriba":
            imagenesEnemy = self.imagenesEnemy["back"]
        elif direcc == "abajo":
            imagenesEnemy = self.imagenesEnemy["front"]
        else:
            if direcc == "izquierda":
                rotar = True
            imagenesEnemy = self.imagenesEnemy["side"]
        posImg = self.game.get_index_bm()
        self.bomberman = imagenesEnemy[posImg]
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

    def recargar_enemigos(self):
        for enemigo in self.game.get_lista_enemigos():
            rotar = False
            # calculo direccion
            direcc = self.enemigo.get_direccion()
            if direcc == "arriba":
                imagenesEnemy = self.imagenesEnemy["back"]
            elif direcc == "abajo":
                imagenesEnemy = self.imagenesEnemy["front"]
            else:
                if direcc == "izquierda":
                    rotar = True
                imagenesEnemy = self.imagenesEnemy["side"]
            posImg = self.enemigo.get_index_img()
            enemy = imagenesEnemy[posImg]
            # print(posImg)
            if rotar:
                enemy = pygame.transform.flip(self.bomberman, True, False)
            pos_enemy = self.enemigo.get_posicion()
            pos_enemy = (int(pos_enemy[0]), int(pos_enemy[1]))
            rect = self.enemy.get_rect()
            rect.centerx = pos_enemy[0]
            rect.centery = pos_enemy[1] - 35
            self.screen.blit(self.bomberman, rect)

    def recargar_contenidos(self):

        celdas = self.game.get_all_celdas() 
        for fila in celdas:
            for celda in fila:
                self.screen.blit(pygame.image.load(path + celda.get_ruta_contenido()), celda.get_pos())
