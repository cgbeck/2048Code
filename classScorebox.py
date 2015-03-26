################################################################################################################
# Package Imports                                                                                              #
################################################################################################################
from pygame.locals import *
from definitions import *
from math import *
import definitions
import pygame
import math

################################################################################################################
# Class Definitions                                                                                            #
################################################################################################################

class Scorebox():  # represents the player, not the game
    def __init__(self,color,width,height,x,y,val=0):
        """ The constructor of the class """
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # the box's position
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # self.val = val

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))