import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from vista.vista import Vista
import pygame
from modelo.game import Game
path = "C:/Users/huergo/luna/bomberman/"

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}

class Controlador():
    def __init__(self):
        # init de la vista y el juego.
        self.game = Game()
    
    def cargar_imagenes(self):
        self.vista.cargar_imagen_fondo(path + "img/fondo.jpg")
        self.vista.cargar_imagen_bomberman(path + "img/bmsprite.jpg")
    
    def main_loop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: run = False

                if event.type == pygame.KEYDOWN:
                    

