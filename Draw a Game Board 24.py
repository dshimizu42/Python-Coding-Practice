# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

def printHor(h):
    for x in range(h):
        print(" ---", end="")
    print('\n', end="")
    return None

def printVert(v):
    for y in range(v):
        print("|   ", end="")
    print('\n', end="")
    return None

def printBoxes(row, col):

    for a in range(row):
        printHor(col)
        printVert(col+1)
    
    printHor(col)
    
    return None

if __name__=="__main__":
    
    print("Let's draw a game board!\n")
    columns = int(input("Enter the height of the game board: "))
    rows = int(input("Enter the width of the game board: "))
    
    printBoxes(rows, columns)