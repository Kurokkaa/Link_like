import pygame
from setting import *

class Level:
    def __init__(self):

        #recuperer la surface
        self.display_surface = pygame.display.get_surface()

        #les sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index,row in WORLD_MAP:
            print(row_index)
            print(row)

    def run(self):
        #dessinne le jeu
        pass

    #22:32