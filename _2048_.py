################################################################################################################
# Package Imports                                                                                              #
################################################################################################################
from pickle import dump,load
from pygame.locals import *
from math import *
import pygame
import random
import time
import math
import sys
import os

################################################################################################################
# Global Variable Definitions                                                                                  #
################################################################################################################
clock = pygame.time.Clock()
pygame.font.init()
tileList = []
global olist
scoreList = [2,4,6]

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

# start points at 0
points=0

################################################################################################################
# Class Definitions                                                                                            #
################################################################################################################

def move(olist, direction):
    # The basic structure in this function is to move all the numbers in the matrix upward.
    # rotate() function helps to transfer other direction request cases into upward moving case.
    if direction == 'up':
        pass
    elif direction == 'down':
        olist = uptodown(olist)
    elif direction == 'right':
        olist = rotate(olist)
    elif direction == 'left':
        olist = rotate(olist)
        olist = rotate(olist)
        olist = rotate(olist)
    global points
    # The above code using rotate function to transfer the matrix into upward cases
    # global points
    for j in range(4):
        mlist=olist[j]
        nlist=clean(mlist)
        i=0
        for i in range(len(nlist)-1):
            if nlist[i]==nlist[i+1]:
                nlist[i]+=nlist[i+1]
                points += int(nlist[i])
                nlist[i+1]=0
        nlist=clean(nlist)
        #check if every two cells have the same number. if so, adding them up.
        x=0
        for x in range(4-len(nlist)):
            nlist.append(0)
            #fullfill the rest of the space in the matrix by 0s.
        olist[j]=nlist
    if direction == 'down':
        olist = uptodown(olist)
    elif direction == 'right':
        olist = rotate(olist)
        olist = rotate(olist)
        olist = rotate(olist)
    elif direction == 'left':
        olist = rotate(olist)
    #The above code using rotate function to transfer other direction request cases back
    return olist

def clean(mlist):
    # This function erase all the 0s in the matrix and only leave "real" numbers there.
    nlist = []
    for item in mlist:
        if item != 0:
            nlist.append(item)
    return nlist

def uptodown(qlist):
    #This function flip the matrix upside down
    newlist=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(qlist)):
        for j in range(len(qlist[i])):
            newlist[i][len(qlist)-j-1]=qlist[i][j]
    return newlist

def rotate(qlist):
    #This function  rotates the matrix in 90 degree everytime when being called.
    newlist=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(qlist)):
        for j in range(len(qlist[i])):
            newlist[j][len(qlist)-i-1]=qlist[i][j]
    return newlist

def check_if_doubles(olist):
    #Goes through a list and checks if there is still a move left
    still_move = False
    for i in range(len(olist)):
        for j in range(1,len(olist[i])):
            if olist[i][j] == olist[i][j-1]:
                still_move = True
    #Checks columns
    templist = rotate(olist)
    for i in range(len(templist)):
        for j in range(1,len(templist[i])):
            if templist[i][j] == templist[i][j-1]:
                still_move = True
    
    return still_move


def rand_add(glist):
    #Randomly replaces a 0 with a 2 in a list
    possible_i = []
    for i in range(len(glist)):
        for j in range(len(glist[i])):
            #For each row and each column
            if glist[i][j] == 0:
                #If the space has a zero save te index
                possible_i.append((i,j))
    if len(possible_i) > 0:
        #Get random index of possible zeroes IF there are zeroes
        index = possible_i[int(random.random()*len(possible_i))]
        glist[index[0]][index[1]] = random.randint(1,2)*2   #Add in the next
        return glist, True
    else:
        #If no zeroes to add, see if can still make a move
        still_move = check_if_doubles(glist)
        if still_move:
            return glist, True
        else:
            return glist, False

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


################################################################################################################
# Function Definitions                                                                                         #
################################################################################################################

def generateTiles(tileNumber,xtiles,ytiles,width,height,xspace,yspace,alist,isGameOver = False):
    # this function generates the colored tiles that make up the game image
    for col in range(xtiles):
        for row in range(ytiles):
            baseColor = (WHITE)
            # create base tile
            tile = Tile(baseColor, width, height, 0, 0, alist[col][row])
            # get new tile info
            c = tile.getColor(isGameOver)
            x = xspace*col + width*col + xspace
            y = yspace*row + height*row + yspace
            # create new tile
            newtile = Tile(c, width, height, x, y, alist[row][col])
            # print the tile
            newtile.draw(screen)
            tile.showValue(x,y,width,height)
            # tileList.append(newtile)

def boxTitles(xspace,yspace):
    # create objects for titles
    curScore = titlefont.render('Current Score',True,(255,255,255))
    highScore = titlefont.render('High Score',True,(255,255,255))
    # find position for the titles
    curscoreRect = curScore.get_rect()  
    area1 = titlefont.size('Current Score')
    curscoreRect.center = (xspace+((screenWidth-4*xspace)/4)-area1[0]/2 + xspace/2, 600)
    highscoreRect = highScore.get_rect()  
    area2 = titlefont.size('High Score')
    highscoreRect.center = (3*xspace+((screenWidth-4*xspace)/4)-area2[0]/2 + (screenWidth-4*xspace)/2 - xspace/2, 600)
    # print titles
    screen.blit(curScore, (curscoreRect.center))
    screen.blit(highScore, (highscoreRect.center))

def showScoreboxes(xspace,yspace):
    color = (100,100,100)
    y = screenHeight-100
    width = (screenWidth-4*xspace)/2 + xspace/2
    height = 100 - yspace
    curScorebox = Scorebox(color,width,height,xspace,y)
    screen.blit(curScorebox.image, (curScorebox.x,curScorebox.y))
    highScorebox = Scorebox(color,width,height,2*xspace+width,y)
    screen.blit(highScorebox.image, (highScorebox.x,highScorebox.y))
    boxTitles(xspace,yspace)

def findScore(alist,xtiles,ytiles):
    # find the score in the game so far by iterating
    # through the matrix of values and adding them
    score = 0
    for i in range(xtiles):
        for j in range(ytiles):
            score = score + alist[i][j]
    return score

def printScore(alist,xtiles,ytiles,xspace, yspace):
    # print the score so far
    pointsStr = str(findScore(alist,xtiles,ytiles))
    # create a object of the score
    score = scorefont.render(pointsStr,True,(255,255,255))
    # score = scorefont.render(pointsStr,True,(255,255,255))
    # find position for the score
    scoreRect = score.get_rect()  
    area = font.size(pointsStr)
    scoreRect.center = (150 - area[0]/2 + xspace/2, 625+(50-yspace/2-area[1]/2))
    # print score
    screen.blit(score, (scoreRect.center))

def printHighScore(alist,xtiles,ytiles,xspace,yspace):
    # print highscore
    pointsStr = str(findHighScore(alist))
    # create a object of the score
    score = scorefont.render(pointsStr,True,(255,255,255))
    # find position for the score
    scoreRect = score.get_rect()  
    area = font.size(pointsStr)
    scoreRect.center = (4*xspace + 3*(screenWidth-4*xspace)/4 - area[0]/2 - xspace/2, 625+(50-yspace/2-area[1]/2))
    # print score
    screen.blit(score, (scoreRect.center))

def printEnd():
    # print game over
    endGame = 'Game Over'
    # create a object of the score
    gameOver = GameOver.render(endGame,True,(255,0,0))
    # find position for the score
    gameOverRect = gameOver.get_rect()  
    area = GameOver.size(endGame)
    gameOverRect.center = (screenWidth/2 - area[0]/2, (screenHeight-100)/2-area[1]/2)
    # scoreRect.center = (0,0)
    # print score
    screen.blit(gameOver, (gameOverRect.center))

def loadScores():
    filename = './scores.txt'
    data_file = open(filename,'r')
    scorelist = load(data_file)
    data_file.close()
    return scorelist

def saveScore(alist,blist,xtiles,ytiles):
    finalscore = findScore(blist,xtiles,ytiles)
    alist.append(finalscore)
    filename = './scores.txt'
    data_file = open(filename,'w')
    dump(scoreList,data_file)
    data_file.close()

def findHighScore(alist):
    return max(alist)

def end_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() # quit the screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit() # quit the screen



################################################################################################################
# Final Initialization                                                                                         #
################################################################################################################

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

################################################################################################################
# Run Main Loop                                                                                                #
################################################################################################################

olist = [[0]*4,[0]*4,[0]*4,[0]*4]
background = Background(WHITE,screenWidth,screenHeight)
saveScore(scoreList,olist,xTiles,yTiles)
scoreList = loadScores()
findHighScore(scoreList)
update = rand_add(olist)

if __name__=="__main__":

    while True:
        #Add in random 2 (if space available)
        background.draw(screen)
        generateTiles(Tiles,xTiles,yTiles,tileW,tileH,xSpace,ySpace,olist)
        showScoreboxes(xSpace,ySpace)
        printScore(olist,xTiles,yTiles,xSpace,ySpace)
        printHighScore(scoreList,xTiles,yTiles,xSpace,ySpace)
        pygame.display.flip()

        #Basic run function of user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # quit the screen
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit() # quit the screen
                if event.key == pygame.K_UP:
                    olist = move(olist,'up')
                    update = rand_add(olist)
                    # if update[1]:
                    #     olist = move(olist,'up')
                elif event.key == pygame.K_DOWN:
                    olist = move(olist,'down')
                    update = rand_add(olist)
                elif event.key == pygame.K_LEFT:
                    olist = move(olist,'left')
                    update = rand_add(olist)
                elif event.key == pygame.K_RIGHT:
                    olist = move(olist,'right')
                    update = rand_add(olist)

        if update[1] != True:
            # print("****Game Over****")
            saveScore(scoreList,olist,xTiles,yTiles)
            break

    while 1:
        background.draw(screen)
        generateTiles(Tiles,xTiles,yTiles,tileW,tileH,xSpace,ySpace,olist,True)
        showScoreboxes(xSpace,ySpace)
        printEnd()
        printScore(olist,xTiles,yTiles,xSpace,ySpace)
        printHighScore(scoreList,xTiles,yTiles,xSpace,ySpace)
        pygame.display.flip()
        end_game()


