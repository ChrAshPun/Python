# create the board

def display_board(columns):

    print(" ------------------------------- ")
    print("|   | {} |   | {} |   | {} |   | {} |".format(columns[2][8],columns[4][8],columns[6][8],columns[8][8]))
    print("|-------------------------------|")   
    print("| {} |   | {} |   | {} |   | {} |   |".format(columns[1][7],columns[3][7],columns[5][7],columns[7][7]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(columns[2][6],columns[4][6],columns[6][6],columns[8][6]))
    print("|-------------------------------|")  
    print("| {} |   | {} |   | {} |   | {} |   |".format(columns[1][5],columns[3][5],columns[5][5],columns[7][5]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(columns[2][4],columns[4][4],columns[6][4],columns[8][4]))
    print("|-------------------------------|")
    print("| {} |   | {} |   | {} |   | {} |   |".format(columns[1][3],columns[3][3],columns[5][3],columns[7][3]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(columns[2][2],columns[4][2],columns[6][2],columns[8][2]))
    print("|-------------------------------|")
    print("| {} |   | {} |   | {} |   | {} |   |".format(columns[1][1],columns[3][1],columns[5][1],columns[7][1]))
    print(" ------------------------------- ")


# coordinates
columns = [0] + [[x for x in range(0,9)] for i in range(9)]

display_board(columns)

columns[1][3] = 'O'

# grid = ['#'] + [' ']*64

# grid with game pieces

'''
# create the board
def display_board(grid):

    print(" ------------------------------- ")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[58],grid[60],grid[62],grid[64]))
    print("|-------------------------------|")   
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[49],grid[51],grid[53],grid[55]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[42],grid[44],grid[46],grid[48]))
    print("|-------------------------------|")  
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[33],grid[35],grid[37],grid[39]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[26],grid[28],grid[30],grid[32]))
    print("|-------------------------------|")
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[17],grid[19],grid[21],grid[23]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[10],grid[12],grid[14],grid[16]))
    print("|-------------------------------|")
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[1],grid[3],grid[5],grid[7]))
    print(" ------------------------------- ")
'''
# grid with game pieces
grid = ['#'] + [[' ' for x in range(0,9)] for i in range(8)]

grid

# create the void spaces for x-coor 1,3,5,7
for index in [0,2,4,6,8]:
    for column in [1,3,5,7]:
        grid[column][index] = '#'

# create the void spaces for x-coor 2,4,6,8
for index in [0,1,3,5,7]:
    for column in [2,4,6,8]:
        grid[column][index] = '#'

# add 'O' pieces to the board
for index in range(1,4):
    for column in range(1,9):
        if grid[column][index] == '#':
            continue
        else:
            grid[column][index] = 'O'

# add 'X' pieces to board
for index in range(1,4):
    for column in range(1,9):
        if grid[column][-index] == '#':
            continue
        else:
            grid[column][-index] = 'x'

display_board(grid)

# show me which spaces on the board have 'O' pieces
for index in range(1,9):
    for column in range(1,9):
        if grid[column][index] == 'O':
            print(str(column)+ ' ' +str(index))
        else:
            pass

grid[0][2]

columns[1][1]
'''
It would take me a long time to have the program go through all 
the pieces that can move for that players turn.

I only need to find the pieces that are required to jump anyway.
'''
# have user select a piece by x & y coordinates

# choosing an x coordinate
while True:
    try:
        x = int(input("Pick an x coordinate: "))
    except ValueError:
        print("Please type an integer.")
    else:
        if x in range(1,9):
            break
        else:
            print("Choose a number between 1-8")
            continue

# choosing an y coordinate
while True:
    try:
        y = int(input("Pick an y coordinate: "))
    except ValueError:
        print("Please type an integer.")
    else:
        if y in range(1,9):
            break
        else:
            print("Choose a number between 1-8")
            continue

grid[1][4]
grid[1][3]
grid[8][4] = 'O'

display_board(grid)

x = 7
y = 3
# verify that the user pick a piece that can move forward.
# Else, make player choose another space
if grid[x][y] == 'O':
    print("Can move on to next step.")
else:
    print("Please pick another space.")

# if x == 1 (because these pieces can only move forward one way)
if x == 1 and y < 8:
    if grid[7][y+1] == ' ':
        print("This piece can move here.")
    else:
        print("This piece cannot move. Pick another space.")

# if x == 8 (because these pieces can only move forward one way)
if x == 8 and y < 8:
    if grid[7][y+1] == ' ':
        print("This piece can move here.")
    else:
        print("This piece cannot move. Pick another space.")

# every other x value
if x in range(1,8):
    if grid[x-1][y+1] == ' ' and grid[x+1][y+1] == ' ':
        print("This piece can move forward left or right.") 
    elif grid[x-1][y+1] == ' ':
        print("This piece can move left.")
    elif grid[x+1][y+1] == ' ':
        print("This piece can move right.")
    else:
        print("This piece cannot move. Pick another space.")


# so say the user input 1 & 1

# so program will check piece grid[1][1]

if x-coor == 1:
    if grid[column+1][index+1] == ' ':
        print("This space is available.")
    else:
        print("This space is not available.")








for index in o_locations:
    print("For piece " + str(index))
    print(str(coordinates[index+7]) + "value is " + str(grid[index+7]))
    print(str(coordinates[index+9]) + "value is " + str(grid[index+9]))

print("left forward diagonal value is " + )