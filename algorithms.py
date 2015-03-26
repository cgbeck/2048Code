################################################################################################################
# Package Imports                                                                                              #
################################################################################################################
import random
import math

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
    # global points
    # The above code using rotate function to transfer the matrix into upward cases
    # global points
    for j in range(4):
        mlist=olist[j]
        nlist=clean(mlist)
        i=0
        for i in range(len(nlist)-1):
            if nlist[i]==nlist[i+1]:
                nlist[i]+=nlist[i+1]
                # points += int(nlist[i])
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