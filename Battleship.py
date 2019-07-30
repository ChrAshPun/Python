def display_board(a,b):
    
    print("    1   2   3   4   5")
    print("   ------------------- ")  
    print("A | {} | {} | {} | {} | {} |".format(b[1][5],b[2][5],b[3][5],b[4][5],b[5][5]))
    print("  |-------------------|")
    print("B | {} | {} | {} | {} | {} |".format(b[1][4],b[2][4],b[3][4],b[4][4],b[5][4]))
    print("  |-------------------|")
    print("C | {} | {} | {} | {} | {} |".format(b[1][3],b[2][3],b[3][3],b[4][3],b[5][3]))
    print("  |-------------------|")
    print("D | {} | {} | {} | {} | {} |".format(b[1][2],b[2][2],b[3][2],b[4][2],b[5][2]))
    print("  |-------------------|")
    print("E | {} | {} | {} | {} | {} |".format(b[1][1],b[2][1],b[3][1],b[4][1],b[5][1]))
    print("  |-------------------|")
    print("  |||||||||||||||||||||")
    print("  |-------------------|")  
    print("A | {} | {} | {} | {} | {} |".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
    print("  |-------------------|")
    print("B | {} | {} | {} | {} | {} |".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
    print("  |-------------------|")
    print("C | {} | {} | {} | {} | {} |".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
    print("  |-------------------|")
    print("D | {} | {} | {} | {} | {} |".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
    print("  |-------------------|")
    print("E | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
    print("   ------------------- ")
    print("    1   2   3   4   5")


coordinates = [0] + [[x for x in [0,'E','D','C','B','A']] for x in range(5)]

coordinates[1][5]

display_board(mygrid,aigrid)

mygrid = [[' ' for x in range(6)] for x in range(6)]

aigrid = [[' ' for x in range(6)] for x in range(6)]

display_board(coordinates,coordinates)

# pick a coordinate and place a marker

while True:
    x = input("Enter a coordinate: ")

    if len(x) != 2:
        continue
    else:
        if x[0].upper() in ['E','D','C','B','A'] and x[1] in [1,2,3,4,5]:
            print(x)
            break
        else:
            continue



