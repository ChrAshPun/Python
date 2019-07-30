def display_board(a,b):
    
    print("    A   B   C   D   E")
    print("   ------------------- ")  
    print("5 | {} | {} | {} | {} | {} |".format(b[1][5],b[2][5],b[3][5],b[4][5],b[5][5]))
    print("  |-------------------|")
    print("4 | {} | {} | {} | {} | {} |".format(b[1][4],b[2][4],b[3][4],b[4][4],b[5][4]))
    print("  |-------------------|")
    print("3 | {} | {} | {} | {} | {} |".format(b[1][3],b[2][3],b[3][3],b[4][3],b[5][3]))
    print("  |-------------------|")
    print("2 | {} | {} | {} | {} | {} |".format(b[1][2],b[2][2],b[3][2],b[4][2],b[5][2]))
    print("  |-------------------|")
    print("1 | {} | {} | {} | {} | {} |".format(b[1][1],b[2][1],b[3][1],b[4][1],b[5][1]))
    print("  |-------------------|")
    print("  |||||||||||||||||||||")
    print("  |-------------------|")  
    print("5 | {} | {} | {} | {} | {} |".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
    print("  |-------------------|")
    print("4 | {} | {} | {} | {} | {} |".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
    print("  |-------------------|")
    print("3 | {} | {} | {} | {} | {} |".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
    print("  |-------------------|")
    print("2 | {} | {} | {} | {} | {} |".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
    print("  |-------------------|")
    print("1 | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
    print("   ------------------- ")
    print("    A   B   C   D   E")


coordinates = [0] + [[x for x in [0,'1','2','3','4','5']] for x in [0,'A','B','C','D','E']]

coordinates[1][5]

mygrid = [[' ' for x in range(6)] for x in range(6)]

aigrid = [[' ' for x in range(6)] for x in range(6)]

display_board(mygrid,aigrid)

display_board(coordinates,coordinates)

x_coor = {'A':1,'B':2,'C':3,'D':4,'E':5}

largeship = []

while True:
    x = str(input("Enter the first coordinate: "))

    if len(x) != 2:
        continue
    else:
        if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ':
            mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
            largeship.append(x)
            break
        else:
            continue

largeship[0][1] == largeship[1][1] == largeship[2][1]

def check_horizontal():
    
    if x_coor[largeship[0][0].upper()] + 1 == x_coor[largeship[1][0].upper()] and x_coor[largeship[1][0].upper()]  + 1 == x_coor[largeship[2][0].upper()]:
        print("This works.")
    else:
        print("These coordinates are not next to each other.")

list.sort()