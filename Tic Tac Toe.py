#Importing clear_output

from IPython.display import clear_output

#Printing instructions
def print_instructions():
    
    print('The board is setup to represent the numerical pad of a computer')
    print('Hence, numbers 7,8 and 9 correspond to the top row')
    print('Numbers 4,5 and 6 correspond to the middle row')
    print('Numbers 1,2 and 3 correspond to the bottom row\n')


#Printing the game board

def print_game(gamelist):
    
    clear_output() #Clears the Screen
    
    print(gamelist[7] + '|' + gamelist[8] + '|' + gamelist[9])
    print('-----')
    print(gamelist[4] + '|' + gamelist[5] + '|' + gamelist[6])
    print('-----')
    print(gamelist[1] + '|' + gamelist[2] + '|' + gamelist[3])


#Taking the player marker
def player_marker_input():
    
    marker = '' #Taking Input in this variable
    
    while marker.upper() not in ['X', 'O']:
        
        marker = input('\nPlayer 1, please choose which marker you want: ')
        
        if marker.upper() not in ['X', 'O']: #Output statement for user
            print('\nSorry, invalid choice. Try again!')
            
    player_1_marker = marker.upper()
    
    if player_1_marker == 'X': #Assigning player 2 the other marker
        player_2_marker = 'O'
    else:
        player_2_marker = 'X'
        
    print('\nPlayer 1 will go first')
        
    return (player_1_marker, player_2_marker)


 #Game win status
def game_board_status(gamelist):
    
    if gamelist[1] == gamelist[2] == gamelist[3] != '-': #checks bottom row
        return False, gamelist[1]
    
    elif gamelist[4] == gamelist[5] == gamelist[6] != '-': #checks middle row
        return False, gamelist[4]
    
    elif gamelist[7] == gamelist[8] == gamelist[9] != '-': #checks top row
        return False, gamelist[7]
    
    elif gamelist[1] == gamelist[4] == gamelist[7] != '-': #checks left column
        return False, gamelist[1]
    
    elif gamelist[2] == gamelist[5] == gamelist[8] != '-': #checks middle column
        return False, gamelist[2]
    
    elif gamelist[3] == gamelist[6] == gamelist[9] != '-': #checks right column
        return False, gamelist[3]
    
    elif gamelist[1] == gamelist[5] == gamelist[9] != '-': #checks right diagonal
        return False, gamelist[1]
    
    elif gamelist[3] == gamelist[5] == gamelist[7] != '-': #checks left diagonal
        return False, gamelist[3]
    
    elif '-' not in gamelist: #Hence board is full
        return False, '-'
    
    else: #Board not full and no one has won yet
        return True, '-'


#Taking player position input
def player_position_input(gamelist, player):
    
    choice = 'WRONG'   #Initialising choice
    
    if player %2 != 0:  #Hence, for player 1
    
        while choice not in range(1,10):

            try:
                choice = int(input('\nPlayer 1 please enter the desired position: ')) #Checking for correctness of input
            except ValueError:
                print('\nYour input is not a number. Please try again.')
                continue

            if choice not in range (1,10): #Output informing user of invalidity of choice
                print('\nYour position is out of bounds! Please try again.')
                continue

            if gamelist[choice] != '-':  #Checking for already filled position
                print('\nThat position is already occupied! Please try again.')
                choice = 'WRONG'
                
    else: #Hence, for player 2
        
        while choice not in range(1,10):

            try:
                choice = int(input('\nPlayer 2 please enter the desired position: ')) #Checking for correctness of input
            except ValueError:
                print('\nYour input is not a number. Please try again.')
                continue

            if choice not in range (1,10): #Output informing user of invalidity of choice
                print('\nYour position is out of bounds! Please try again.')
                continue

            if gamelist[choice] != '-':  #Checking for already filled position
                print('\nThat position is already occupied! Please try again.')
                choice = 'WRONG'
        
    return choice


#Updating Game Board
def update_game_board(gamelist, position, marker):
    
    gamelist[position] = marker #updates the position
    
    print_game(gamelist)
    
    return gamelist


#Do you want to play again?
def replay():
    
    return input('Do you want to play again? Enter yes or no.').lower().startswith('y')
    

#Game Logic

while True:
    print_instructions() #First print the instructions
    
    tictactoe = ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-'] #Initialise the board

    player1_marker, player2_marker = player_marker_input() #Take input for player markers

    game_status = True #Checks status of the game

    alternate = 1 #To alternate turns

    finish_marker = '-' #To decide who is the winner, if any

    position = 0 #Initializing the position

    print_game(tictactoe) #Print the board initially

    while game_status:

        position = player_position_input(tictactoe, alternate) #Take the input position

        if alternate %2 != 0: #Hence for player 1
            tictactoe = update_game_board(tictactoe, position, player1_marker)

        else: #Hence for player 2
            tictactoe = update_game_board(tictactoe, position, player2_marker)

        game_status, finish_marker = game_board_status(tictactoe) #Check game status

        alternate += 1 #Updating turn for next player

    if finish_marker == player1_marker:
        print('\nPlayer 1 has won the game')

    elif finish_marker == player2_marker:
        print('\nPlayer 2 has won the game')

    else:
        print('\nThe game was tied')
        
    
    if not replay():
        break




