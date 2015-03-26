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
# Global Variable Definitions                                                                                  #
################################################################################################################
pygame.font.init()
font = pygame.font.SysFont('Ariel', 80, bold=True, italic=False)

################################################################################################################
# Class Definitions                                                                                            #
################################################################################################################

class Tile():  # represents the player, not the game
    def __init__(self,color,width,height,x,y,val=0):
        """ The constructor of the class """
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # the tile's position
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.val = val

    def getColor(self,isgameover):
        # calculate the color of the passed in tile
        if isgameover:
            x = self.val
            if x == 0:
                hue = (200,200,200)
            else:
                hue = (255/sqrt(x),255/sqrt(x),255/sqrt(x))
            return hue
        else:
            x = self.val
            if x == 0:
                hue = (200,200,200)
            else:
                hue = (255/sqrt(x),0,0)
            return hue

    def showValue(self,x,y,w,h):
        # find and then print the value of each tile
        tileVal = self.val
        # if 0 dont print anything
        if tileVal == 0:
            pass
        else:
            # otherwise print the value centered on the tile
            val = str(tileVal)
            label = font.render(val,True,(255,255,255))
            labelRect = label.get_rect()
            area = font.size(val)  
            labelRect.center = (x+w/2-area[0]/2, y+h/2-area[1]/2)
            screen.blit(label, (labelRect.center))

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))