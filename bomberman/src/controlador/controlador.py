import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from vista.vista import Vista
import pygame
from modelo.game import Game
path = "C:/Users/huergo/Desktop/luna/bomberman/"

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}

class Controlador():
    def __init__(self):
        # init de la vista y el juego.
        self.game = Game()
        self.vista = Vista(self.game)
        self.cargar_imagenes()
        self.main_loop()
    
    def cargar_imagenes(self):
        #self.vista.cargar_imagen_fondo(path + "img/fondo.png")
        self.vista.cargar_imagenes_bomberman(path, self.game.get_posicion_personaje())
        self.vista.cargar_imagenes_enemigo(path)
    
    def main_loop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.game.mover_bomberman(CONTROLES[str(event.key)])
                    
            # self.vista.recargar_fondo()
            self.vista.recargar_contenidos()
            self.vista.recargar_enemigos()
            self.vista.recargar_bomberman()


            pygame.display.flip()
    

controlador = Controlador()
                    

