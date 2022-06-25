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

def updateScreen():
    m = n = 3
    x = 70; y = 70
    for i in range(m):
        for j in range(n):
            if BOARD[i][j] == 1:
                font = pg.font.Font('freesansbold.ttf', 100)
                text = font.render('X', True, (225,225,225))
                WINDOW.blit(text,(x-45,y-45))
            elif BOARD[i][j] == 2:
                pg.draw.circle(WINDOW,(225,225,225),(x,y),40,10)
            x += 100
        y += 100
        x = 70

def renderWinnerScreen(winner):
    global WINDOW
    WINDOW=pg.display.set_mode((340,340))
    font = pg.font.Font('freesansbold.ttf', 20)
    text = font.render(str(winner)+ ' is the winner', True, (225,225,225))
    WINDOW.blit(text,(100,100))
    pg.display.update()
    pass



generateBoard()



def isWinning(board):
    #WINNING LOGIC 

    if (board[0][0] != 0) and (board[0][0] == board[1][1] and  board[1][1] == board[2][2]):
        # X - -
        # - X -
        # - - X
        return board[0][0]

    
    elif (board[0][2] != 0 ) and (board[0][2] == board[1][1] == board[2][0]):
        # - - X
        # - X -
        # X - -
        return board[0][2]

    
    for i in range(3):
        # X X X
        # - - - For all rows
        # - - - 
        
        if (board[i][0] != 0) and (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
    
    for i in range(3):
        # X - -
        # X - - For all columns
        # X - - 

        if (board[0][i] != 0) and (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]
    
    return -1


def isDraw():
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] == 0:
                return False
    return True

def renderDrawScreen():
    global WINDOW
    WINDOW=pg.display.set_mode((340,340))
    font = pg.font.Font('freesansbold.ttf', 20)
    text = font.render('The Game is a Draw', True, (225,225,225))
    WINDOW.blit(text,(100,100))
    pg.display.update()
    pass

def getBoxXY(vals):
    Xval = Yval = -1

    if 20 <= vals[0] <= 120:
        Yval = 0
    elif 120 <= vals[0] <= 220:
        Yval = 1
    elif 220 <= vals[0] <= 320:
        Yval = 2
    
    if 20 <= vals[1] <= 120:
        Xval = 0
    elif 120 <= vals[1] <= 220:
        Xval = 1
    elif 220 <= vals[1] <= 320:
        Xval = 2
    
    return Xval, Yval

while mainloop:
    
    for event in pg.event.get():
            if event.type==pg.QUIT:
                mainloop=False
    
    
    
    updateScreen()

    
    
    # Check for winner
    winner = isWinning(BOARD)
    if winner == -1:
        # GAME LOGIC
        left, middle, right = pg.mouse.get_pressed()
        if left:
            vals = pg.mouse.get_pos()
            pg.time.wait(500)
            x,y = getBoxXY(vals)
            if (x != -1) and (y != -1) and (BOARD[x][y] == 0):
                BOARD[x][y] = CURRENT_PLAYER
                if CURRENT_PLAYER == 1:
                    CURRENT_PLAYER = 2
                else:
                    CURRENT_PLAYER = 1
    else:
        renderWinnerScreen(winner)
        pg.time.delay(1000)
        mainloop = False

    # Check for Draw
    if isDraw():
        renderDrawScreen()
    
    pg.display.update()
    print(BOARD)

