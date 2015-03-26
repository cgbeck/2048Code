################################################################################################################
# Package Imports                                                                                              #
################################################################################################################
from pygame.locals import *
from definitions import *
import definitions
import pygame

################################################################################################################
# Class Definitions                                                                                            #
################################################################################################################

class Background():  # represents the player, not the game
    def __init__(self,color,width,height):
        """ The constructor of the class """
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # the background's position
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))