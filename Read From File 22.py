if __name__=="__main__":
    
    # Python Dictionaries are formatted like so: Keys, Values
    # This is how to create an empty dictionary
    starWarsDic = {}

    with open('nameslist22.txt', 'r') as open_file: # This line reads the specified file
        line = open_file.readline() # This code reads the first line of the code
        while line:
            line = line.strip() #Delete the newline character from the end of each line
          
            if not line in starWarsDic: # Checks if the line that was read is NOT in the dictionary
                starWarsDic.update({line: 0}) # If not in the dictionary, it updates the dictionar with the line and a value of 0
            
            star = starWarsDic[line] # This code takes the value from the appropriate key from the dictionary
            star += 1 # Adds one to the value
            starWarsDic[line] = star # updates the value in the dictionary at the appropriate key
            
            line = open_file.readline() # Move to read the next line

    open_file.close() # Closing the file
    
    # Printing all pairs in the dictionary
    for pair in starWarsDic.items():
        print(pair)