################################################################################################################
# Package Imports                                                                                              #
################################################################################################################
from pygame.locals import *
import pygame

################################################################################################################
# Global Variable Definitions                                                                                  #
################################################################################################################
clock = pygame.time.Clock()
pygame.font.init()
tileList = []
global olist

# font initialization
scorefont = pygame.font.SysFont('Ariel', 50, bold=True, italic=False)
titlefont = pygame.font.SysFont('Ariel', 40, bold=True, italic=False)
GameOver = pygame.font.SysFont('Ariel', 140, bold=True, italic=False)
font = pygame.font.SysFont('Ariel', 80, bold=True, italic=False)


# Color Definitions
WHITE = (255, 255, 255)
GREY = (119, 136, 153)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# screen size
screenWidth = 600
screenHeight = 700

# calculate tile size
tileW = screenWidth/5
tileH = (screenHeight-100)/5

# calculate tile spacing
xSpace = tileW/5
ySpace = tileH/5
xTiles = 4
yTiles = 4
Tiles = xTiles*yTiles

screen = pygame.display.set_mode((screenWidth, screenHeight))