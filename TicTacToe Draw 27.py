from time import sleep

def printGameBoard(board):

    print("game = ", end = "")
    for x in range(len(board)):
        temp = 0
        print("[", end="")        
        for y in range(len(board)):
            if board[x][y] == 0:
                print("0", end="")
            elif board[x][y] == 1:
                print("O", end="")
            elif board[x][y] == 2:
                print("X", end="")
            
            if temp < 2:
                print(", ", end="")
                temp += 1
        
        print("],")
        print("       ", end="")
    
    print('\n', end="")    
    return None

def updateGame(t, currBoard, placePiece):
    currBoard[placePiece[0]][placePiece[1]] = t
    return None

def isEmpty(currBoard, placePiece):
    if currBoard[placePiece[0]][placePiece[1]] == 0:
        return True
    else:
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
    #sleep(2)
    print("To place your piece, please enter the row and column number in the following format: row,column")
    #sleep(2)
    
    # Initialize the game board
    gameInit = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    usrTurn = 1
    gameTurn = 0
    
    while gameTurn <= 8:
        usrPlace = usrCoordManip(input("Enter the coordinates where you would like to place your piece: "))
        
        if isEmpty(gameInit, usrPlace) == False:
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
    
    print("Draw by insufficent spaces")
        
    