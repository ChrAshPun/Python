import random
import os

def clear_output():

	os.system('clear')

def intro():
    
    print('Welcome to Tic Tac Toe!\n')
    
    print('     |     |     ')
    print('  T  |  I  |  C  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  T  |  A  |  C  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  T  |  O  |  E  ')
    print('     |     |     ')
    
    print('\nPlayer {} will go first!'.format(player))
    i = input("Press Enter to continue: ")

def display_board(board,available):
    
    print ('\n     |     |          '+available[7]+'|'+available[8]+'|'+available[9]+'')
    print('  '+board[7]+'  '+'|'+'  '+board[8]+'  '+'|'+'  '+board[9]+'       -----')
    print ('     |     |          '+available[4]+'|'+available[5]+'|'+available[6]+'')
    print('-----------------     -----')
    print ('     |     |          '+available[1]+'|'+available[2]+'|'+available[3]+'')
    print('  '+board[4]+'  '+'|'+'  '+board[5]+'  '+'|'+'  '+board[6]+'')     
    print ('     |     |     ')
    print('-----------------')
    print ('     |     |     ')
    print('  '+board[1]+'  '+'|'+'  '+board[2]+'  '+'|'+'  '+board[3]+'')
    print ('     |     |     ')

def space_check(board, position):
    
    #check if space is empty
    return board[position] == ' '

def player_choice(board,player):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Player {}\nChoose a space: '.format(player)))
        except ValueError:
            print("Please choose an integer.")
        else:
            print("Please choose an available space.")
        
    return position

def place_marker(available,board,marker,position):
    board[position] = marker
    available[position] = ' '

def win_check(board,mark):

    return ((board[7] ==  board[8] ==  board[9] == mark) or # across the top
    (board[4] ==  board[5] ==  board[6] == mark) or # across the middle
    (board[1] ==  board[2] ==  board[3] == mark) or # across the bottom
    (board[7] ==  board[4] ==  board[1] == mark) or # down the middle
    (board[8] ==  board[5] ==  board[2] == mark) or # down the middle
    (board[9] ==  board[6] ==  board[3] == mark) or # down the right side
    (board[7] ==  board[5] ==  board[3] == mark) or # diagonal
    (board[9] ==  board[5] ==  board[1] == mark)) # diagonal

def full_board_check(board):
    
    # check for empty spaces
    return ' ' not in board[1:]

def continue_game():
    
    while True:

        x = input("Play again? Enter y or n: ")
            
        if x.lower()=='y':
            return True
        elif x.lower()=='n':
            print("Thanks for playing!")
            break
        else:
            print("Sorry, please try again.")
            continue

# players[1] == 'X' and players[-1] == 'O'
players = [0,'X','O']
play_game = True

while play_game:

    # randomly pick player that goes first
    toggle = random.choice((-1,1))
    player = players[toggle]
    clear_output()
    intro()
    
    # reset variables
    board = [' '] * 10   # a list of empty spaces
    available = [str(num) for num in range(0,10)]
    
    game_on = True
    clear_output()
    
    while game_on:
        
        # show board, choose position, place marker
        display_board(board,available)
        position = player_choice(board,player)
        place_marker(available,board,player,position)
    
        # check for a win
        if win_check(board, player):
            clear_output()
            display_board(board,available)
            print('Player '+player+' wins!')
            game_on = False
        else:
            # check for a tie
            if full_board_check(board):
                clear_output()
                display_board(board,available)
                print("It's a tie!")
                break
            else:
                # other player's turn
                toggle *= -1
                player = players[toggle]
                clear_output()
                
    # play again?
    play_game = continue_game()