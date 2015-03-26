################################################################################################################
# Package Imports                                                                                              #
################################################################################################################

from GUIbuild import *
import definitions

# ################################################################################################################
# # Function Definitions                                                                                         #
# ################################################################################################################

# def generateTiles(tileNumber,xtiles,ytiles,width,height,xspace,yspace,alist,isGameOver = False):
#     # this function generates the colored tiles that make up the game image
#     for col in range(xtiles):
#         for row in range(ytiles):
#             baseColor = (WHITE)
#             # create base tile
#             tile = Tile(baseColor, width, height, 0, 0, alist[col][row])
#             # get new tile info
#             c = tile.getColor(isGameOver)
#             x = xspace*col + width*col + xspace
#             y = yspace*row + height*row + yspace
#             # create new tile
#             newtile = Tile(c, width, height, x, y, alist[row][col])
#             # print the tile
#             newtile.draw(screen)
#             tile.showValue(x,y,width,height)
#             # tileList.append(newtile)

# def boxTitles(xspace,yspace):
#     # create objects for titles
#     curScore = titlefont.render('Current Score',True,(255,255,255))
#     highScore = titlefont.render('High Score',True,(255,255,255))
#     # find position for the titles
#     curscoreRect = curScore.get_rect()  
#     area1 = titlefont.size('Current Score')
#     curscoreRect.center = (xspace+((screenWidth-4*xspace)/4)-area1[0]/2 + xspace/2, 600)
#     highscoreRect = highScore.get_rect()  
#     area2 = titlefont.size('High Score')
#     highscoreRect.center = (3*xspace+((screenWidth-4*xspace)/4)-area2[0]/2 + (screenWidth-4*xspace)/2 - xspace/2, 600)
#     # print titles
#     screen.blit(curScore, (curscoreRect.center))
#     screen.blit(highScore, (highscoreRect.center))

# def showScoreboxes(xspace,yspace):
#     color = (100,100,100)
#     y = screenHeight-100
#     width = (screenWidth-4*xspace)/2 + xspace/2
#     height = 100 - yspace
#     curScorebox = Scorebox(color,width,height,xspace,y)
#     screen.blit(curScorebox.image, (curScorebox.x,curScorebox.y))
#     highScorebox = Scorebox(color,width,height,2*xspace+width,y)
#     screen.blit(highScorebox.image, (highScorebox.x,highScorebox.y))
#     boxTitles(xspace,yspace)

# def findScore(alist,xtiles,ytiles):
#     # find the score in the game so far by iterating
#     # through the matrix of values and adding them
#     score = 0
#     for i in range(xtiles):
#         for j in range(ytiles):
#             score = score + alist[i][j]
#     return score

# def printScore(alist,xtiles,ytiles,xspace, yspace):
#     # print the score so far
#     pointsStr = str(findScore(alist,xtiles,ytiles))
#     # create a object of the score
#     score = scorefont.render(pointsStr,True,(255,255,255))
#     # score = scorefont.render(pointsStr,True,(255,255,255))
#     # find position for the score
#     scoreRect = score.get_rect()  
#     area = font.size(pointsStr)
#     scoreRect.center = (150 - area[0]/2 + xspace/2, 625+(50-yspace/2-area[1]/2))
#     # print score
#     screen.blit(score, (scoreRect.center))

# def printHighScore(alist,xtiles,ytiles,xspace,yspace):
#     # print highscore
#     pointsStr = str(findHighScore(alist))
#     # create a object of the score
#     score = scorefont.render(pointsStr,True,(255,255,255))
#     # find position for the score
#     scoreRect = score.get_rect()  
#     area = font.size(pointsStr)
#     scoreRect.center = (4*xspace + 3*(screenWidth-4*xspace)/4 - area[0]/2 - xspace/2, 625+(50-yspace/2-area[1]/2))
#     # print score
#     screen.blit(score, (scoreRect.center))

# def printEnd():
#     # print game over
#     endGame = 'Game Over'
#     # create a object of the score
#     gameOver = GameOver.render(endGame,True,(255,0,0))
#     # find position for the score
#     gameOverRect = gameOver.get_rect()  
#     area = GameOver.size(endGame)
#     gameOverRect.center = (screenWidth/2 - area[0]/2, (screenHeight-100)/2-area[1]/2)
#     # scoreRect.center = (0,0)
#     # print score
#     screen.blit(gameOver, (gameOverRect.center))

# def loadScores():
#     filename = './scores.txt'
#     data_file = open(filename,'r')
#     scorelist = load(data_file)
#     data_file.close()
#     return scorelist

# def saveScore(alist,blist,xtiles,ytiles):
#     finalscore = findScore(blist,xtiles,ytiles)
#     alist.append(finalscore)
#     filename = './scores.txt'
#     data_file = open(filename,'w')
#     dump(scoreList,data_file)
#     data_file.close()

# def findHighScore(alist):
#     return max(alist)

# def end_game():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit() # quit the screen
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 sys.exit() # quit the screen

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

################################################################################################################
# Final Initialization                                                                                         #
################################################################################################################
pygame.init()

################################################################################################################
# Run Main Loop                                                                                                #
################################################################################################################

olist = [[0]*4,[0]*4,[0]*4,[0]*4]
background = Background(WHITE,screenWidth,screenHeight)
# saveScore(scoreList,xTiles,yTiles)
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


