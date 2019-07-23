import random
import os

# define clear_output()
def clear_output():

	os.system('clear')

# create 7 slots with 6 levels of depth
slot1 = [0] + [' ' for x in range(1,7)]
slot2 = [0] + [' ' for x in range(1,7)]
slot3 = [0] + [' ' for x in range(1,7)]
slot4 = [0] + [' ' for x in range(1,7)]
slot5 = [0] + [' ' for x in range(1,7)]
slot6 = [0] + [' ' for x in range(1,7)]
slot7 = [0] + [' ' for x in range(1,7)]

allslots = [0,slot1,slot2,slot3,slot4,slot5,slot6,slot7]

# create display_board()
def display_board():

    print('  1   2   3   4   5   6   7\n')

    print("| {} | {} | {} | {} | {} | {} | {} |".format(slot1[6],slot2[6],slot3[6],slot4[6],slot5[6],slot6[6],slot7[6]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slot1[5],slot2[5],slot3[5],slot4[5],slot5[5],slot6[5],slot7[5]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slot1[4],slot2[4],slot3[4],slot4[4],slot5[4],slot6[4],slot7[4]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slot1[3],slot2[3],slot3[3],slot4[3],slot5[3],slot6[3],slot7[3]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slot1[2],slot2[2],slot3[2],slot4[2],slot5[2],slot6[2],slot7[2]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slot1[1],slot2[1],slot3[1],slot4[1],slot5[1],slot6[1],slot7[1]))
    print("|===|===|===|===|===|===|===|")

# introduction
def intro():
    
    print("     Welcome to Connect4!\n")
    
    print("|   |   |   |   |   |   |   |")
    print("|   |   |   |   |   |   |   |")
    print("|   |   |   |   |   |   |   |")
    print("|   |   |   |   |   |   |   |")
    print("|   |   |   |   |   |   |   |")
    print("|   |   |   |   |   |   |   |")
    print("|===|===|===|===|===|===|===|")
    
    print('\nPlayer {} will go first!'.format(player))
    i = input("Press Enter to continue: ")

# check if slot is full
def check_slot(slot):

    # is slot full?
    return ' ' not in allslots[slot]

# choose an available slot
def player_choice(player):
    
    slot = 0
    
    while True:
        
        try:
            slot = int(input('\nPlayer {}\nChoose a slot: '.format(player)))
            # if slot in range
            if slot in [1,2,3,4,5,6,7]:
                # if slot if not full
                if not check_slot(slot):
                    return slot
                else:
                    print("Please choose a slot that is not full.")
    
            else:
                print("Please choose an available slot.")
                continue
                
        except ValueError:
            print("Please type a number.")

# drop the game piece to the lowest space
def find_depth(slot):   

    for index, value in enumerate(allslots[slot]):
        if value == ' ':
            depth.append(index)

    return min(depth)

# change the empty space to the player's marker
def place_marker(slot,y_value,player):
    allslots[slot][y_value] = player

def win_check(slot,y_value):

    # vertical Connect4
    return (all(x == player for x in allslots[slot][1:5]) or
    all(x == player for x in allslots[slot][2:6]) or
    all(x == player for x in allslots[slot][3:7]) or

    # horizontal Connect4
    player == slot1[y_value] == slot2[y_value] == slot3[y_value] == slot4[y_value] or
    player == slot2[y_value] == slot3[y_value] == slot4[y_value] == slot5[y_value] or
    player == slot3[y_value] == slot4[y_value] == slot5[y_value] == slot6[y_value] or
    player == slot4[y_value] == slot5[y_value] == slot6[y_value] == slot7[y_value] or

    # upward diagonal Connect4 for slot 1 
    player == slot1[3] == slot2[4] == slot3[5] == slot4[6] or
    player == slot1[2] == slot2[3] == slot3[4] == slot4[5] or
    player == slot1[1] == slot2[2] == slot3[3] == slot4[4] or
    # upward diagonal Connect4 for slot 2
    player == slot2[3] == slot3[4] == slot4[5] == slot5[6] or 
    player == slot2[2] == slot3[3] == slot4[4] == slot5[5] or
    player == slot2[1] == slot3[2] == slot4[3] == slot5[4] or
    # upward diagonal Connect4 for slot 3
    player == slot3[3] == slot4[4] == slot5[5] == slot6[6] or
    player == slot3[2] == slot4[3] == slot5[4] == slot6[5] or
    player == slot3[1] == slot4[2] == slot5[3] == slot6[4] or
    # upward diagonal Connect4 for slot 4
    player == slot4[3] == slot5[4] == slot6[5] == slot7[6] or
    player == slot4[2] == slot5[3] == slot6[4] == slot7[5] or
    player == slot4[1] == slot5[2] == slot6[3] == slot7[4] or

    # downward diagonal Connect4 for slot 1 
    player == slot1[6] == slot2[5] == slot3[4] == slot4[3] or
    player == slot1[5] == slot2[4] == slot3[3] == slot4[2] or
    player == slot1[4] == slot2[3] == slot3[2] == slot4[1] or
    # downward diagonal Connect4 for slot 2
    player == slot2[6] == slot3[5] == slot4[4] == slot5[3] or 
    player == slot2[5] == slot3[4] == slot4[3] == slot5[2] or
    player == slot2[4] == slot3[3] == slot4[2] == slot5[1] or
    # downward diagonal Connect4 for slot 3
    player == slot3[6] == slot4[5] == slot5[4] == slot6[3] or
    player == slot3[5] == slot4[4] == slot5[3] == slot6[2] or
    player == slot3[4] == slot4[3] == slot5[2] == slot6[1] or
    # downward diagonal Connect4 for slot 4
    player == slot4[6] == slot5[5] == slot6[4] == slot7[3] or
    player == slot4[5] == slot5[4] == slot6[3] == slot7[2] or
    player == slot4[4] == slot5[3] == slot6[2] == slot7[1])

def full_grid_check():
    
    return ' ' not in (slot1 + slot2 + slot3 + slot4 + slot5 + slot6 + slot7)

def continue_game():
    
    while True:

        x = input("Play again? Enter y or n: ")
            
        if x.lower() == 'y':
            game_on = False
            return True
        elif x.lower() == 'n':
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
    slot1 = [0] + [' ' for x in range(1,7)]
    slot2 = [0] + [' ' for x in range(1,7)]
    slot3 = [0] + [' ' for x in range(1,7)]
    slot4 = [0] + [' ' for x in range(1,7)]
    slot5 = [0] + [' ' for x in range(1,7)]
    slot6 = [0] + [' ' for x in range(1,7)]
    slot7 = [0] + [' ' for x in range(1,7)]

    allslots = [0,slot1,slot2,slot3,slot4,slot5,slot6,slot7]
    
    game_on = True
    clear_output()
    
    while game_on:

        # reset depth
        depth = []
        # show board, choose slot, place marker
        display_board()
        slot = player_choice(player)
        y_value = find_depth(slot)
        place_marker(slot,y_value,player)
    
        # check for a win
        if win_check(slot,y_value):
            clear_output()
            display_board()
            print('Player '+player+' wins!')
            game_on = False
        else:
            # check for a tie
            if full_grid_check():
                clear_output()
                display_board()
                print("It's a tie!")
                break
            else:
                # other player's turn
                toggle *= -1
                player = players[toggle]
                clear_output()
                
    # play again?
    play_game = continue_game()