# we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

import itertools

def checkWin(win):
    if len(win) == 1:
        if list(win)[0] == 2:
            print("Player 2 Wins!")
            return None
        elif list(win)[0] == 1:
            print("Player 1 Wins!")
            return None
    return None

def checkRowWin(board):
    
    for x in range(len(board)):
        rowWin = set()
        for y in range(len(board)):
            rowWin.add(board[x][y])
        checkWin(rowWin)
    return None

def checkColWin(board):
    
    for x in range(len(board)):
        colWin = set()
        for y in range(len(board)):
            colWin.add(board[y][x])
        checkWin(colWin)
    return None

def checkDiagWin(board):
    
    diagWinDown = set()
    
    for x, y in zip(range(len(board)), range(len(board))):
        diagWinDown.add(board[x][y])
 
    checkWin(diagWinDown)
    
    diagWinUp = set()
    
    for x, y in zip(range(0, 2), range(2, 0, -1)):
        diagWinUp.add(board[x][y])
    
    checkWin(diagWinUp)
    return None

if __name__=="__main__":
    
    testGame = [[2, 2, 0],[2, 1, 0],[2, 1, 1]]
    checkRowWin(testGame)
    checkColWin(testGame)
    checkDiagWin(testGame)
    
    