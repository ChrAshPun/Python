xcoor= [x for x in range(0,7)]
xcoor

ycoor = [y for y in range(0,6)]
ycoor

def board():
    print("| {} |  {}   {}   {}   {}   {}".format(grid[5],grid[11],grid[17],grid[23],grid[29],grid[35]))
    print("| {} |  {}   {}   {}   {}   {}".format(grid[4],grid[10],grid[16],grid[22],grid[28],grid[34]))
    print("| {} |  {}   {}   {}   {}   {}".format(grid[3],grid[9],grid[15],grid[21],grid[27],grid[33]))
    print("| {} |  {}   {}   {}   {}   {}".format(grid[2],grid[8],grid[14],grid[20],grid[26],grid[32]))
    print("| {} |  {}   {}   {}   {}   {}".format(grid[1],grid[7],grid[13],grid[19],grid[25],grid[31]))
    print("| {} |  {}   {}   {}   {}   {}".format(grid[0],grid[6],grid[12],grid[18],grid[24],grid[30]))
    print('')
board()

xy = tuple(zip(x,y))
xy

c = []
for x in x:
    c = (x,y)

grid = []
for x in xcoor:
    for y in ycoor:
        grid.append((x,y))

grid

def coordinate(self,x,y):
    self.x = x
    self.y = y

slot1 = grid[:6]
slot1

slot2 = grid[6:12]
slot2

slot3 = grid[12:18]
slot3

slot4 = grid[18:24]
slot4

slot5 = grid[24:30]
slot5

slot6 = grid[30:36]
slot6

empty = [' ']*36
empty

def board():
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[5],empty[11],empty[17],empty[23],empty[29],empty[35]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[4],empty[10],empty[16],empty[22],empty[28],empty[34]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[3],empty[9],empty[15],empty[21],empty[27],empty[33]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[2],empty[8],empty[14],empty[20],empty[26],empty[32]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[1],empty[7],empty[13],empty[19],empty[25],empty[31]))
    print(" | {} | {} | {} | {} | {} | {} |".format(empty[0],empty[6],empty[12],empty[18],empty[24],empty[30]))
    print(" |===|===|===|===|===|===|")
board()