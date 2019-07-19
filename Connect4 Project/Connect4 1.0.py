xcoor= [x for x in range(1,8)]
xcoor

ycoor = [y for y in range(1,7)]
ycoor

def board():
    print("| {} | {} | {} | {} | {} | {} |".format(slots[1][6],slots[2][6],slots[3][6],slots[4][6],slots[5][6],slots[6][6]))
    print("| {} | {} | {} | {} | {} | {} |".format(slots[1][5],slots[2][5],slots[3][5],slots[4][5],slots[5][5],slots[6][5]))
    print("| {} | {} | {} | {} | {} | {} |".format(slots[1][4],slots[2][4],slots[3][4],slots[4][4],slots[5][4],slots[6][4]))
    print("| {} | {} | {} | {} | {} | {} |".format(slots[1][3],slots[2][3],slots[3][3],slots[4][3],slots[5][3],slots[6][3]))
    print("| {} | {} | {} | {} | {} | {} |".format(slots[1][2],slots[2][2],slots[3][2],slots[4][2],slots[5][2],slots[6][2]))
    print("| {} | {} | {} | {} | {} | {} |".format(slots[1][1],slots[2][1],slots[3][1],slots[4][1],slots[5][1],slots[6][1]))
    print("|===|===|===|===|===|===|")

board()

grid = [0]
for x in xcoor:
    for y in ycoor:
        grid.append((x,y))

len(grid)

slot1 = [0] + grid[1:7]

slot2 = [0] + grid[7:13]

slot3 = [0] + grid[13:19]

slot4 = [0] + grid[19:25]

slot5 = [0] + grid[25:31]

slot6 = [0] + grid[31:37]

slot7 = [0] + grid[37:43]

slots = [0,slot1,slot2,slot3,slot4,slot5,slot6,slot7]

slots[1][6]

# create an empty board

empty = [' ']*43
len(empty)

def board():
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[6],empty[12],empty[18],empty[24],empty[30],empty[36],empty[42]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[5],empty[11],empty[17],empty[23],empty[29],empty[35],empty[41]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[4],empty[10],empty[16],empty[22],empty[28],empty[34],empty[40]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[3],empty[9],empty[15],empty[21],empty[27],empty[33],empty[39]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[2],empty[8],empty[14],empty[20],empty[26],empty[32],empty[38]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[1],empty[7],empty[13],empty[19],empty[25],empty[31],empty[37]))
    print(" |===|===|===|===|===|===|")
board()

#y-coor needs to be as low as possible

empty = [' ']*36

grid = []
for x in xcoor:
    for y in ycoor:
        grid.append((x,y))

empty[0] = 'O'

board()

slot1 = grid[:6]
slot1

# slot[index][x or y]

slots = [0,slot1,slot2,slot3,slot4,slot5,slot6]

# First, choose a slot
# player_input is an integer
# slots[player_input]

player_input = 2

slots[player_input]

# the game piece needs to "fall" to the lowest space

# create depth list

player_marker = 'O'
player_input = 1

def create_depth(player_input):

        depth = []
        for x,y in slots[player_input]:
                depth.append(y)
        
        return depth

depth = create_depth(player_input)

min(depth)

# do a space check

def space_check():

        return empty[min(depth)] == ' '

space_check()

# if True 

emptyslots[player_input][min(depth)]

emptyslots[player_input][min(depth)] = 'X'

emptyslots[2][min(depth)] = "X"

empty[player_input] = emptyslots[2][min(depth)]

slots[player_input][min(depth)] = 'X'

slots[player_input][min(depth)]

# show board

board()

z = []
for gx,y in slot1:
        z.append(y)

min(z)

# these are in the same space
grid[7]
empty[7]

empty1 = grid[1:7]
empty1

empty2 = grid[7:13]
empty2

empty3 = grid[13:19]
empty3 

empty4 = grid[19:25]
empty4

empty5 = grid[25:31]
empty5

empty6 = grid[31:37]
empty6

emptyslots = [0,empty1,empty2,empty3,empty4,empty5,empty6]

empty1