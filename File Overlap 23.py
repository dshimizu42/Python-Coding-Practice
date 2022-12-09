def readFile(fileName):
    numsList = []
    
    with open(fileName, 'r') as open_file:
        line = open_file.readline()
        while line:
            line = line.strip()
            numsList.append(int(line))
            line = open_file.readline()

    open_file.close()
    return numsList

if __name__=="__main__":
    
    primeNums = readFile('primenumbers 23.txt')
    happyNums = readFile('happynumbers 23.txt')
    
    overlap = []
    
    for element in primeNums:
        if element in happyNums:
            overlap.append(element)
    
    print(overlap)
    