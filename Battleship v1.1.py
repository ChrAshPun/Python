def display_board(a,b):
    
    if place_largeship:
    
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
        print("5 | {} | {} | {} | {} | {} |     Large Battleship".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
        print("  |-------------------|     O O O")
        print("4 | {} | {} | {} | {} | {} |     Medium Battleship 1".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
        print("  |-------------------|     O O")
        print("3 | {} | {} | {} | {} | {} |     Medium Battleship 2".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
        print("  |-------------------|     O O")
        print("2 | {} | {} | {} | {} | {} |     Small Battleship".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
        print("  |-------------------|     O")
        print("1 | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
        print("   ------------------- ")
        print("    A   B   C   D   E")
    elif place_mediumship1:
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
        print("5 | {} | {} | {} | {} | {} |     ".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
        print("  |-------------------|          ")
        print("4 | {} | {} | {} | {} | {} |     Medium Battleship 1".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
        print("  |-------------------|     O O")
        print("3 | {} | {} | {} | {} | {} |     Medium Battleship 2".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
        print("  |-------------------|     O O")
        print("2 | {} | {} | {} | {} | {} |     Small Battleship".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
        print("  |-------------------|     O")
        print("1 | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
        print("   ------------------- ")
        print("    A   B   C   D   E")
    elif place_mediumship2:
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
        print("5 | {} | {} | {} | {} | {} |     ".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
        print("  |-------------------|          ")
        print("4 | {} | {} | {} | {} | {} |     ".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
        print("  |-------------------|          ")
        print("3 | {} | {} | {} | {} | {} |     Medium Battleship 2".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
        print("  |-------------------|     O O")
        print("2 | {} | {} | {} | {} | {} |     Small Battleship".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
        print("  |-------------------|     O")
        print("1 | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
        print("   ------------------- ")
        print("    A   B   C   D   E")
    elif place_smallship:
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
        print("5 | {} | {} | {} | {} | {} |     ".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
        print("  |-------------------|          ")
        print("4 | {} | {} | {} | {} | {} |     ".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
        print("  |-------------------|          ")
        print("3 | {} | {} | {} | {} | {} |     ".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
        print("  |-------------------|          ")
        print("2 | {} | {} | {} | {} | {} |     Small Battleship".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
        print("  |-------------------|     O")
        print("1 | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
        print("   ------------------- ")
        print("    A   B   C   D   E")
    else:
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
        print("5 | {} | {} | {} | {} | {} |     ".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
        print("  |-------------------|          ")
        print("4 | {} | {} | {} | {} | {} |     ".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
        print("  |-------------------|          ")
        print("3 | {} | {} | {} | {} | {} |     ".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
        print("  |-------------------|          ")
        print("2 | {} | {} | {} | {} | {} |     ".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
        print("  |-------------------|          ")
        print("1 | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
        print("   ------------------- ")
        print("    A   B   C   D   E")

import random 

horizontal_or_vertical = ['h','v']

ai_x_coor = {1:'A',2:'B',3:'C',4:'D',5:'E'}

x_coor = {'A':1,'B':2,'C':3,'D':4,'E':5}

coordinates = [0] + [[x for x in [0,'1','2','3','4','5']] for x in [0,'A','B','C','D','E']]

mygrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]

aigrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]

def check_vertical_placement(largeship):
    
    while True:
        if int(largeship[0][1]) + 1 == int(largeship[1][1]) and int(largeship[1][1]) + 1 == int(largeship[2][1]):
            print("This works.")
            break
        else:
            print("These coordinates are not next to each other.")
            largeship = []
            lship1 = 1
            continue

def check_horizontal_placement(largeship):
    
    while True:
        if x_coor[largeship[0][0].upper()] + 1 == x_coor[largeship[1][0].upper()] and x_coor[largeship[1][0].upper()]  + 1 == x_coor[largeship[2][0].upper()]:
            print("This works.")
            break
        else:
            print("These coordinates are not next to each other.")
            largeship = []
            lship1 = 1
            continue

intro = True
game_start = True

while game_start:

    # Introduction
    while intro:
        print("\nWelcome to Battleship!") 
        print("Place your battleships onto the board.")
        
        place_largeship = True
        break
    
    # ask player to place 4 battleships onto their board
    while place_largeship:
        
        largeship = []
        counter = 1
        
        # place the large battleship first
        # ask the player to input 3 coordinates for the large battleship and then break
        while len(largeship) < 3:
            
            x = str(input("Enter coordinate " + str(counter) + " for the large ship:"))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in largeship:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    display_board(mygrid,aigrid)
                    largeship.append(x)
                    counter += 1 
                    continue
                else:
                    continue

        largeship.sort()
        
        # check if the ship was placed vertically
        if largeship[0][0] == largeship[1][0] == largeship[2][0]:
            if int(largeship[0][1]) + 1 == int(largeship[1][1]) and int(largeship[1][1]) + 1 == int(largeship[2][1]):
                print("This works.")
                place_largeship = False
                place_mediumship1 = True
                break
                
            else:
                print("These coordinates are not next to each other.")
                mygrid[x_coor[largeship[0][0].upper()]][int(largeship[0][1])] = ' '
                mygrid[x_coor[largeship[1][0].upper()]][int(largeship[1][1])] = ' '
                mygrid[x_coor[largeship[2][0].upper()]][int(largeship[2][1])] = ' '
                continue
                
        # check if the ship was placed horizontally
        elif largeship[0][1] == largeship[1][1] == largeship[2][1]:
            if x_coor[largeship[0][0].upper()] + 1 == x_coor[largeship[1][0].upper()] and x_coor[largeship[1][0].upper()]  + 1 == x_coor[largeship[2][0].upper()]:
                print("This works.")
                place_largeship = False
                place_mediumship1 = True
                break
                
            else:
                print("These coordinates are not next to each other.")
                mygrid[x_coor[largeship[0][0].upper()]][int(largeship[0][1])] = ' '
                mygrid[x_coor[largeship[1][0].upper()]][int(largeship[1][1])] = ' '
                mygrid[x_coor[largeship[2][0].upper()]][int(largeship[2][1])] = ' '
                continue
        else:
            print("These coordinates are not next to each other.")
            print("Place the battleship vertically or horizontally on the board.")
            mygrid[x_coor[largeship[0][0].upper()]][int(largeship[0][1])] = ' '
            mygrid[x_coor[largeship[1][0].upper()]][int(largeship[1][1])] = ' '
            mygrid[x_coor[largeship[2][0].upper()]][int(largeship[2][1])] = ' '
            continue
            
    while place_mediumship1:
        
        mediumship1 = []
        counter = 1
                    
        while len(mediumship1) < 2:

            x = str(input("Enter coordinate " + str(counter) + " for the first medium ship:"))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in mediumship1:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    display_board(mygrid,aigrid)
                    mediumship1.append(x)
                    counter += 1 
                    continue
                else:
                    continue
        
        mediumship1.sort()

        # check if the ship was placed vertically
        if mediumship1[0][0] == mediumship1[1][0]:
            if int(mediumship1[0][1]) + 1 == int(mediumship1[1][1]):
                print("This works.")
                place_mediumship1 = False
                place_mediumship2 = True
                break
            else:
                print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship1[0][0].upper()]][int(mediumship1[0][1])] = ' '
                mygrid[x_coor[mediumship1[1][0].upper()]][int(mediumship1[1][1])] = ' '
                continue

        # check if the ship was placed horizontally
        elif mediumship1[0][1] == mediumship1[1][1]:
            if x_coor[mediumship1[0][0].upper()] + 1 == x_coor[mediumship1[1][0].upper()]:
                print("This works.")
                place_mediumship1 = False
                place_mediumship2 = True
                break
            else:
                print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship1[0][0].upper()]][int(mediumship1[0][1])] = ' '
                mygrid[x_coor[mediumship1[1][0].upper()]][int(mediumship1[1][1])] = ' '
                continue
        else:
            print("These coordinates are not next to each other.")
            print("Place the battleship vertically or horizontally on the board.")
            mygrid[x_coor[mediumship1[0][0].upper()]][int(mediumship1[0][1])] = ' '
            mygrid[x_coor[mediumship1[1][0].upper()]][int(mediumship1[1][1])] = ' '
            continue

    while place_mediumship2:
        
        mediumship2 = []
        counter = 1
        print(largeship)
        print(mediumship1)
        print(mediumship2)
                    
        while len(mediumship2) < 2:

            x = str(input("Enter coordinate " + str(counter) + " for the second medium ship:"))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in mediumship2:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    display_board(mygrid,aigrid)
                    mediumship2.append(x)
                    counter += 1 
                    continue
                else:
                    continue
        
        mediumship2.sort()

        # check if the ship was placed vertically
        if mediumship2[0][0] == mediumship2[1][0]:
            if int(mediumship2[0][1]) + 1 == int(mediumship2[1][1]):
                place_mediumship2 = False
                place_smallship = True
                break
            else:
                print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship2[0][0].upper()]][int(mediumship2[0][1])] = ' '
                mygrid[x_coor[mediumship2[1][0].upper()]][int(mediumship2[1][1])] = ' '
                continue

        # check if the ship was placed horizontally
        elif mediumship2[0][1] == mediumship2[1][1]:
            if x_coor[mediumship2[0][0].upper()] + 1 == x_coor[mediumship2[1][0].upper()]:
                place_mediumship2 = False
                place_smallship = True
                break
            else:
                print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship2[0][0].upper()]][int(mediumship2[0][1])] = ' '
                mygrid[x_coor[mediumship2[1][0].upper()]][int(mediumship2[1][1])] = ' '
                continue
        else:
            print("These coordinates are not next to each other.")
            print("Place the battleship vertically or horizontally on the board.")
            mygrid[x_coor[mediumship2[0][0].upper()]][int(mediumship2[0][1])] = ' '
            mygrid[x_coor[mediumship2[1][0].upper()]][int(mediumship2[1][1])] = ' '
            continue

    while place_smallship:
        
        smallship = []
        counter = 1
        
        while len(smallship) < 1:

            x = str(input("Enter coordinate " + str(counter) + " for the small ship:"))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in smallship:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    display_board(mygrid,aigrid)
                    smallship.append(x)
                    place_smallship = False
                    ai_place_largeship = True
                    break
                else:
                    continue

    # this is the AI part
    while ai_place_largeship:
        
        ai_largeship = []
        orientation = random.choice(horizontal_or_vertical)
        
        # place the large battleship first
        # ask the player to input 3 coordinates for the large battleship and then break
        if orientation == 'h':
            
            x = random.randint(1,3)
            y = random.choice(['1','2','3','4','5'])       
            
            ai_largeship.append(ai_x_coor[x] + y)
            ai_largeship.append(ai_x_coor[x+1] + y)
            ai_largeship.append(ai_x_coor[x+2] + y)         

            if aigrid[x][int(y)] == aigrid[x+1][int(y)] == aigrid[x+2][int(y)] == ' ':
                aigrid[x][int(y)] = 'O'
                aigrid[x+1][int(y)] = 'O'
                aigrid[x+2][int(y)] = 'O'
                display_board(mygrid, aigrid)
                ai_place_largeship = False
                ai_place_mediumship1 = True
                break
        
            else:
                continue
        
        else:

            x = random.choice(['A','B','C','D','E'])
            y = random.choice([1,2,3])  

            ai_largeship.append(x + str(y))
            ai_largeship.append(x + str(y+1))
            ai_largeship.append(x + str(y+2)) 
            
            if aigrid[x_coor[x]][y] == aigrid[x_coor[x]][y+1] == aigrid[x_coor[x]][y+2] == ' ':
                aigrid[x_coor[x]][y] = 'O'
                aigrid[x_coor[x]][y+1] = 'O'
                aigrid[x_coor[x]][y+2] = 'O'
                display_board(mygrid, aigrid)
                ai_place_largeship = False
                ai_place_mediumship1 = True
                break
                
            else:
                continue
                
    while ai_place_mediumship1:
        
        ai_mediumship1 = []
        orientation = random.choice(horizontal_or_vertical)
        
        # place the large battleship first
        # ask the player to input 3 coordinates for the large battleship and then break
        if orientation == 'h':
            
            x = random.randint(1,3)
            y = random.choice(['1','2','3','4','5'])       
            
            ai_mediumship1.append(ai_x_coor[x] + y)
            ai_mediumship1.append(ai_x_coor[x+1] + y)     

            if aigrid[x][int(y)] == aigrid[x+1][int(y)] == ' ':
                aigrid[x][int(y)] = 'O'
                aigrid[x+1][int(y)] = 'O'
                display_board(mygrid, aigrid)
                ai_place_mediumship1 = False
                ai_place_mediumship2 = True
                break
        
            else:
                continue
        
        else:

            x = random.choice(['A','B','C','D','E'])
            y = random.choice([1,2,3])  

            ai_mediumship1.append(x + str(y))
            ai_mediumship1.append(x + str(y+1))
            
            if aigrid[x_coor[x]][y] == aigrid[x_coor[x]][y+1] == ' ':
                aigrid[x_coor[x]][y] = 'O'
                aigrid[x_coor[x]][y+1] = 'O'
                display_board(mygrid, aigrid)
                place_mediumship1 = False
                place_mediumship2 = True
                break
                
            else:
                continue
                
    while ai_place_mediumship2:
        
        ai_mediumship2 = []
        orientation = random.choice(horizontal_or_vertical)
        
        # place the large battleship first
        # ask the player to input 3 coordinates for the large battleship and then break
        if orientation == 'h':
            
            x = random.randint(1,3)
            y = random.choice(['1','2','3','4','5'])       
            
            ai_mediumship2.append(ai_x_coor[x] + y)
            ai_mediumship2.append(ai_x_coor[x+1] + y)     

            if aigrid[x][int(y)] == aigrid[x+1][int(y)] == ' ':
                aigrid[x][int(y)] = 'O'
                aigrid[x+1][int(y)] = 'O'
                display_board(mygrid, aigrid)
                ai_place_mediumship2 = False
                ai_place_smallship = True
                break
        
            else:
                continue
        
        else:

            x = random.choice(['A','B','C','D','E'])
            y = random.choice([1,2,3])  

            ai_mediumship2.append(x + str(y))
            ai_mediumship2.append(x + str(y+1))
            
            if aigrid[x_coor[x]][y] == aigrid[x_coor[x]][y+1] == ' ':
                aigrid[x_coor[x]][y] = 'O'
                aigrid[x_coor[x]][y+1] = 'O'
                display_board(mygrid, aigrid)
                ai_place_mediumship2 = False
                ai_place_smallship = True
                break
                
            else:
                continue
                
    while ai_place_smallship:
        
        ai_smallship = []
        orientation = random.choice(horizontal_or_vertical)
        
        # place the large battleship first
        # ask the player to input 3 coordinates for the large battleship and then break
        if orientation == 'h':
            
            x = random.randint(1,3)
            y = random.choice(['1','2','3','4','5'])       
            
            ai_smallship.append(ai_x_coor[x] + y)   

            if aigrid[x][int(y)] == ' ':
                aigrid[x][int(y)] = 'O'
                display_board(mygrid, aigrid)
                ai_place_smallship = False
                ai_game_start = False
                break
        
            else:
                continue
        
        else:

            x = random.choice(['A','B','C','D','E'])
            y = random.choice([1,2,3])  

            ai_smallship.append(x + str(y))
            
            if aigrid[x_coor[x]][y] == ' ':
                aigrid[x_coor[x]][y] = 'O'
                display_board(mygrid, aigrid)
                ai_place_smallship = False
                ai_game_start = False
                break
                
            else:
                continue