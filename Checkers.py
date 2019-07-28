# create the board

def display_board(grid):

    print(" ------------------------------- ")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[29],grid[30],grid[31],grid[32]))
    print("|-------------------------------|")   
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[25],grid[26],grid[27],grid[28]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[21],grid[22],grid[23],grid[24]))
    print("|-------------------------------|")  
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[17],grid[18],grid[19],grid[20]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[13],grid[14],grid[15],grid[16]))
    print("|-------------------------------|")
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[9],grid[10],grid[11],grid[12]))
    print("|-------------------------------|")
    print("|   | {} |   | {} |   | {} |   | {} |".format(grid[5],grid[6],grid[7],grid[8]))
    print("|-------------------------------|")
    print("| {} |   | {} |   | {} |   | {} |   |".format(grid[1],grid[2],grid[3],grid[4]))
    print(" ------------------------------- ")

# create the x and y coordinates

x_coor= [x for x in range(1,9)]
x_coor

y_coor = [y for y in range(1,9)]
y_coor

grid = []
for x in x_coor:
    for y in y_coor:
        grid.append((x,y))

grid[:8:2]
grid[9:16:2]
grid[16:24:2]
grid[25:32:2]
grid[32:39:2]
grid[41:48:2]
grid[48:55:2]
grid[57:64:2]

grid = [0] + grid[:8:2]+grid[9:16:2]+grid[16:24:2]+grid[25:32:2]+grid[32:39:2]+grid[41:48:2]+grid[48:55:2]+grid[57:64:2]

grid

display_board(grid)

len(grid)

empty_grid = [0] + [' ']*32
empty_grid

display_board(empty_grid)

# Player Class

o_team = [0] + ['O']*12

x_team = [0] + ['X']*12

for index, value in enumerate(o_team):
        empty_grid[index] = o_team[index]

for index, value in enumerate(x_team):
        empty_grid[-index] = x_team[index]

empty_grid

empty_grid[12]

empty_grid[12] = ' '
empty_grid[13] = 'O'

empty_grid[1]

# the x coordinate is this:
grid[1][0]
# the y coordinate is this:
grid[1][1]


# Men Class

# King Class

# check for jump function

# check for available move





