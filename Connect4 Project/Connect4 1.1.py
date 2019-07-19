import random
import os

# define clear_output()
def clear_output():

	os.system('clear')

# create the x & y coordinates
xcoor= [x for x in range(1,8)]
xcoor

ycoor = [y for y in range(1,7)]
ycoor

# create the grid
grid = [0]
for x in xcoor:
    for y in ycoor:
        grid.append((x,y))

# create 7 slots with 6 levels of depth

slot1 = [0] + grid[1:7]
slot2 = [0] + grid[7:13]
slot3 = [0] + grid[13:19]
slot4 = [0] + grid[19:25]
slot5 = [0] + grid[25:31]
slot6 = [0] + grid[31:37]
slot7 = [0] + grid[37:43]

slots = [0,slot1,slot2,slot3,slot4,slot5,slot6,slot7]

# create the board with the grid coordinates
# don't think I need this...

def coor_board():
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slots[1][6],slots[2][6],slots[3][6],slots[4][6],slots[5][6],slots[6][6],slots[7][6]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slots[1][5],slots[2][5],slots[3][5],slots[4][5],slots[5][5],slots[6][5],slots[7][5]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slots[1][4],slots[2][4],slots[3][4],slots[4][4],slots[5][4],slots[6][4],slots[7][4]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slots[1][3],slots[2][3],slots[3][3],slots[4][3],slots[5][3],slots[6][3],slots[7][3]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slots[1][2],slots[2][2],slots[3][2],slots[4][2],slots[5][2],slots[6][2],slots[7][2]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(slots[1][1],slots[2][1],slots[3][1],slots[4][1],slots[5][1],slots[6][1],slots[7][1]))
    print("|===|===|===|===|===|===|")

# create an empty grid

empty = [' ']*43

# create 7 slots with 6 levels of depth

empty1 = [0] + [' ' for x in range(1,7)]
empty2 = [0] + [' ' for x in range(1,7)]
empty3 = [0] + [' ' for x in range(1,7)]
empty4 = [0] + [' ' for x in range(1,7)]
empty5 = [0] + [' ' for x in range(1,7)]
empty6 = [0] + [' ' for x in range(1,7)]
empty7 = [0] + [' ' for x in range(1,7)]

empty = [0,empty1,empty2,empty3,empty4,empty5,empty6,empty7]

'''
empty1 = [' ' for x in range(1,8)]
empty2 = [' ' for x in range(1,8)]
empty3 = [' ' for x in range(1,8)]
empty4 = [' ' for x in range(1,8)]
empty5 = [' ' for x in range(1,8)]
empty6 = [' ' for x in range(1,8)]
empty7 = [' ' for x in range(1,8)]
'''

# create display_board()
def display_board():

    print('  1   2   3   4   5   6   7\n')

    print("| {} | {} | {} | {} | {} | {} | {} |".format(empty[1][6],empty[2][6],empty[3][6],empty[4][6],empty[5][6],empty[6][6],empty[7][6]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(empty[1][5],empty[2][5],empty[3][5],empty[4][5],empty[5][5],empty[6][5],empty[7][5]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(empty[1][4],empty[2][4],empty[3][4],empty[4][4],empty[5][4],empty[6][4],empty[7][4]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(empty[1][3],empty[2][3],empty[3][3],empty[4][3],empty[5][3],empty[6][3],empty[7][3]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(empty[1][2],empty[2][2],empty[3][2],empty[4][2],empty[5][2],empty[6][2],empty[7][2]))
    print("| {} | {} | {} | {} | {} | {} | {} |".format(empty[1][1],empty[2][1],empty[3][1],empty[4][1],empty[5][1],empty[6][1],empty[7][1]))
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
    return ' ' not in empty[slot]

# choose a slot
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

    for index, value in enumerate(empty[slot]):
        if value == ' ':
            depth.append(index)

    return min(depth)

# drop game piece into slot

def place_marker(slot,y_value,player):
    empty[slot][y_value] = player

def win_check(slot,y_value):

    # vertical Connect4
    all(x == player for x in empty[slot][1:5])
    all(x == player for x in empty[slot][2:6])
    all(x == player for x in empty[slot][3:7])

    # horizontal Connect4
    player == empty[1][y_value] == empty[2][y_value] == empty[3][y_value] == empty[4][y_value]
    player == empty[2][y_value] == empty[3][y_value] == empty[4][y_value] == empty[5][y_value]
    player == empty[3][y_value] == empty[4][y_value] == empty[5][y_value] == empty[6][y_value]
    player == empty[4][y_value] == empty[5][y_value] == empty[6][y_value] == empty[7][y_value]










# create the x & y coordinates
xcoor= [x for x in range(1,8)]
ycoor = [y for y in range(1,7)]

 # create the grid
grid = [0]
for x in xcoor:
    for y in ycoor:
        grid.append((x,y))

# create 7 slots with 6 levels of depth
slot1 = [0] + grid[1:7]
slot2 = [0] + grid[7:13]
slot3 = [0] + grid[13:19]
slot4 = [0] + grid[19:25]
slot5 = [0] + grid[25:31]
slot6 = [0] + grid[31:37]
slot7 = [0] + grid[37:43]

slots = [0,slot1,slot2,slot3,slot4,slot5,slot6,slot7]

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
    # create an empty board
    empty = [' ']*43

    # create 7 slots with 6 levels of depth
    empty1 = [0] + [' ' for x in range(1,7)]
    empty2 = [0] + [' ' for x in range(1,7)]
    empty3 = [0] + [' ' for x in range(1,7)]
    empty4 = [0] + [' ' for x in range(1,7)]
    empty5 = [0] + [' ' for x in range(1,7)]
    empty6 = [0] + [' ' for x in range(1,7)]
    empty7 = [0] + [' ' for x in range(1,7)]

    empty = [0,empty1,empty2,empty3,empty4,empty5,empty6,empty7]
    
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
