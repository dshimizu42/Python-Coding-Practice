#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

print('Let\'s play rock, paper, scissors!')

quit == "no"

while quit != "enter":
    p1 = input('\nPlayer 1: Enter your move: ')
    p2 = input('Player 2: Enter your move: ')

    if p1 == p2:
        print('It\'s a tie')
    elif p1 == 'scissors':
        if p2 == 'paper':
            print('Player 1 is the winner!')
        elif p2 == 'rock':
            print('Player 2 is the winner!')
    elif p1 == 'paper':
        if p2 == 'scissors':
            print('Player 2 is the winner!')
        elif p2 == 'rock':
            print('Player 1 is the winner!')
    else:
        if p2 == 'scissors':
            print('Player 1 is the winner!')
        elif p2 == 'paper':
            print('Player 2 is the winner!')
    
    quit = input('Type "enter" to quit and "no" to continue:' )

print('Thank you for playing!')

