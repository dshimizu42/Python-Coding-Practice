import itertools
from time import sleep

def checkWin(win):
    if len(win) == 1:
        if list(win)[0] == 2:
            print("Player 2 Wins!")
            return 1
        elif list(win)[0] == 1:
            print("Player 1 Wins!")
            return 1
        else:
            return 0
    return 0

def checkRowWin(board):
    
    for x in range(len(board)):
        rowWin = set()
        for y in range(len(board)):
            rowWin.add(board[x][y])
        if checkWin(rowWin) == 1:
            return 1
    return 0

def checkColWin(board):
    
    for x in range(len(board)):
        colWin = set()
        for y in range(len(board)):
            colWin.add(board[y][x])
        if checkWin(colWin) == 1:
            return 1
    return 0

def checkDiagWin(board):
    
    diagWinDown = set()
    
    for x, y in zip(range(len(board)), range(len(board))):
        diagWinDown.add(board[x][y])
 
    if checkWin(diagWinDown) == 1:
        return 1
    
    diagWinUp = set()
    
    for x, y in zip(range(0, 2), range(2, 0, -1)):
        diagWinUp.add(board[x][y])
    
    if checkWin(diagWinUp) == 1:
        return 1
    
    return 0

########

def printHor(h):
    for x in range(h):
        print(" ---", end="")
    print('\n', end="")
    return None

def printVert(v, a, game):
    print("| ", end = "")
    for y in range(v-1):
        if game[a][y] == 0:
            print("0", end="")
        elif game[a][y] == 1:
            print("O", end="")
        elif game[a][y] == 2:
            print("X", end="")
        print(" | ", end="")
    print('\n', end="")
    return None

def printGameBoard(game):
    
    row = 3
    col = 3
    
    for a in range(row):
        printHor(col)
        printVert(col+1, a, game)
    
    printHor(col)
    
    return None

#######
def updateGame(t, currBoard, placePiece):
    currBoard[placePiece[0]][placePiece[1]] = t
    return None

def isEmpty(currBoard, placePiece):
    if currBoard[placePiece[0]][placePiece[1]] == 0:
        return True
    else:
        return False

def outOfRange(piecePlace):
    
    for x in range(len(piecePlace)):
        if piecePlace[x] < 0:
            return True
        elif piecePlace[x] > 2:
            return True
    return False
    

def usrCoordManip(usrInput):
    coordManip = usrInput.split(",")
    
    for x in range(len(coordManip)):
        usrInput[x].strip()
    
    coordManip = list(map(int, coordManip))
    
    for x in range(len(coordManip)):
        coordManip[x] -= 1
    
    return coordManip

if __name__=="__main__":
    
    # Game information is listed below
    print("Welcome to Tic-Tac-Toe!")
    sleep(2)
    print("To place your piece, please enter the row and column number in the following format: row,column")
    sleep(2)
    
    # Initialize the game board
    gameInit = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    usrTurn = 1
    gameTurn = 0
    
    while gameTurn <= 8:
        usrPlace = usrCoordManip(input("Enter the coordinates where you would like to place your piece: "))
        
        if outOfRange(usrPlace) == True:
            print("Error: Space is out of range")
            continue
        elif isEmpty(gameInit, usrPlace) == False:
            print("Error: Space is occupied")
            continue
        else:
            if usrTurn == 1:
                updateGame(usrTurn, gameInit, usrPlace)
                usrTurn += 1
                gameTurn += 1
            else:
                updateGame(usrTurn, gameInit, usrPlace)
                usrTurn -= 1
                gameTurn += 1
        
        printGameBoard(gameInit)        

        if checkRowWin(gameInit) == 1:
            break
        if checkColWin(gameInit) == 1:
            break
        if checkDiagWin(gameInit) == 1:
            break
        
    if gameTurn > 8:
        print("Draw by insufficent spaces")