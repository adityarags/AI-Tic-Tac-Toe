from re import X
import pygame as pg
from pygame.locals import *

pg.init()

BOARD = []

mainloop = True
CURRENT_PLAYER = 1
for i in range(3):
    BOARD.append([])
    for j in range(3):
        BOARD[i].append(0)


WINDOW=pg.display.set_mode((340,340))
pg.display.set_caption("Tic Tac Toe") 

def generateBoard():
    #INITIAL BOARD
    m = n = 3
    x = 20; y = 20
    for i in range(m):
        for j in range(n):
            pg.draw.rect(WINDOW,(225,225,225),(x,y,100,100),1)
            x += 100
        y += 100
        x = 20

def renderWinnerScreen(winner):
    #WINNER SCREEN
    pass

generateBoard()

def isWinning(board):
    #WINNING LOGIC 
    if (board[0][0] == board[1][1] == board[2][2]):
        # X - -
        # - X -
        # - - X
        return board[0][0]

    
    elif (board[0][2] == board[1][1] == board[2][0]):
        # - - X
        # - X -
        # X - -
        winning = board[0][2]

    
    for i in range(3):
        # X X X
        # - - - For all rows
        # - - - 
        
        if(board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
    
    for i in range(3):
        # X - -
        # X - - For all columns
        # X - - 

        if(board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]
    
    return -1




while mainloop:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            mainloop=False
    if CURRENT_PLAYER == 1:
        CURRENT_PLAYER = 2
    else:
        CURRENT_PLAYER = 1
    
    winner = isWinning(BOARD)
    if winner != -1:
        # GAME LOGIC
        pass
    else:
        #RENDER WINNER SCREEN
        renderWinnerScreen(winner)
    pg.display.update()