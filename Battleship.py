import os
import operator
import random

def clear_output():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_board(a,b):

        print("   AI's Map\n")  
        print("    A   B   C   D   E            AI's Ships")
        print("   -------------------           -------------------")  
        print("5 | {} | {} | {} | {} | {} |          Battleship".format(b[1][5],b[2][5],b[3][5],b[4][5],b[5][5]))
        print("  |-------------------|          {}".format(ai_icon_battleship))
        print("4 | {} | {} | {} | {} | {} |          Cruiser 1".format(b[1][4],b[2][4],b[3][4],b[4][4],b[5][4]))
        print("  |-------------------|          {}".format(ai_icon_mediumship1))
        print("3 | {} | {} | {} | {} | {} |          Cruiser 2".format(b[1][3],b[2][3],b[3][3],b[4][3],b[5][3]))
        print("  |-------------------|          {}".format(ai_icon_mediumship2))
        print("2 | {} | {} | {} | {} | {} |          Submarine".format(b[1][2],b[2][2],b[3][2],b[4][2],b[5][2]))
        print("  |-------------------|          {}".format(ai_icon_smallship))
        print("1 | {} | {} | {} | {} | {} |".format(b[1][1],b[2][1],b[3][1],b[4][1],b[5][1]))
        print("  |-------------------|")
        print("  |||||||||||||||||||||          Player's Ships")
        print("  |-------------------|          -------------------")  
        print("5 | {} | {} | {} | {} | {} |          Battleship".format(a[1][5],a[2][5],a[3][5],a[4][5],a[5][5]))
        print("  |-------------------|          {}".format(icon_battleship))
        print("4 | {} | {} | {} | {} | {} |          Cruiser 1".format(a[1][4],a[2][4],a[3][4],a[4][4],a[5][4]))
        print("  |-------------------|          {}".format(icon_mediumship1))
        print("3 | {} | {} | {} | {} | {} |          Cruiser 2".format(a[1][3],a[2][3],a[3][3],a[4][3],a[5][3]))
        print("  |-------------------|          {}".format(icon_mediumship2))
        print("2 | {} | {} | {} | {} | {} |          Submarine".format(a[1][2],a[2][2],a[3][2],a[4][2],a[5][2]))
        print("  |-------------------|          {}".format(icon_smallship))
        print("1 | {} | {} | {} | {} | {} |".format(a[1][1],a[2][1],a[3][1],a[4][1],a[5][1]))
        print("   ------------------- ")
        print("    A   B   C   D   E\n")
        print("   Player's Map\n")

def hit_or_miss():
    
    call_out = True
    while call_out:
            
        x = str(input("Enter a coordinate: "))

        if len(x) != 2:
            continue
        else:
            # accept the input if the space on the hiddengrid is empty
            if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and hiddengrid[x_coor[x[0].upper()]][int(x[1])] == ' ':
                # if it's a hit
                if aigrid[x_coor[x[0].upper()]][int(x[1])] == 'O':
                    print("Player called out {}!".format(x[0].upper() + x[1]))
                    if x[0].upper() + x[1] in ai_largeship:
                        for index, value in enumerate(ai_largeship):

                            global ai_icon_battleship

                            if value == x[0].upper() + x[1]:
                                # remove the coordinate from the list
                                ai_largeship.remove(x[0].upper() + x[1])
                                # pop off one 'O' from the battleship icon
                                # ai_icon_battleship = ai_icon_battleship[:-2]
                                # mark an 'O' on the hidden grid
                                hiddengrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                                # if the list is empty, the ship has sunk
                                if not ai_largeship:
                                    print("Hit! AI's Battleship has sunk!")
                                    ai_icon_battleship = ''
                                    call_out = False
                                    break
                                else:
                                    print("Hit! Battleship!")
                                    call_out = False
                                    break
                            else:
                                continue
                    elif x[0].upper() + x[1] in ai_mediumship2:
                        for index, value in enumerate(ai_mediumship2):
                            
                            global ai_icon_mediumship2

                            if value == x[0].upper() + x[1]:
                                ai_mediumship2.remove(x[0].upper() + x[1])
                                # ai_icon_mediumship2 = ai_icon_mediumship2[:-2]
                                hiddengrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                                if not ai_mediumship2:
                                    print("Hit! AI's Cruiser #2 has sunk!")
                                    ai_icon_mediumship2 = ''
                                    call_out = False
                                    break
                                else:
                                    print("Hit! Cruiser #2!")
                                    call_out = False
                                    break
                            else:
                                continue
                    elif x[0].upper() + x[1] in ai_mediumship1:
                        for index, value in enumerate(ai_mediumship1):

                            global ai_icon_mediumship1

                            if value == x[0].upper() + x[1]:
                                ai_mediumship1.remove(x[0].upper() + x[1])
                                # ai_icon_mediumship1 = ai_icon_mediumship1[:-2]
                                hiddengrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                                if not ai_mediumship1:
                                    print("Hit! AI's Cruiser #1 has sunk!")
                                    ai_icon_mediumship1 = ''
                                    call_out = False
                                    break
                                else:
                                    print("Hit! Cruiser #1!")
                                    call_out = False
                                    break
                            else:
                                continue
                    elif x[0].upper() + x[1] in ai_smallship:
                        for index, value in enumerate(ai_smallship):

                            global ai_icon_smallship

                            if value == x[0].upper() + x[1]:
                                ai_smallship.remove(x[0].upper() + x[1])
                                # ai_icon_smallship = ai_icon_smallship[:-2]
                                hiddengrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                                print("Hit! AI's Submarine has sunk!")
                                ai_icon_smallship = ''
                                call_out = False
                                break
                            else:
                                continue
                else:
                    # if it isn't a hit, mark an 'X' on the hidden grid
                    hiddengrid[x_coor[x[0].upper()]][int(x[1])] = 'X'
                    print("Player called out {}!".format(x[0].upper() + x[1]))
                    print("Miss!")
                    call_out = False
                    break
            else:
                continue

def ai_hit_or_miss():

    call_out = True
    while call_out:

        x = random.choice(['A','B','C','D','E']) 
        y = random.choice(['1','2','3','4','5']) 
        
        # if the AI called out an empty space say "Miss!" and do not change mygrid
        if mygrid[x_coor[x]][int(y)] == ' ':
            print("AI called out {}!".format(x+y))
            print("Miss!")
            mygrid[x_coor[x]][int(y)] = 'X'
            break
        
        # if AI hit a ship
        elif mygrid[x_coor[x]][int(y)] == 'O':
            print("AI called out {}!".format(x+y))
            if x + y in largeship:
                for index, value in enumerate(largeship):

                    global icon_battleship

                    if value == x + y:
                        # remove the coordinate from the list
                        largeship.remove(x + y)
                        icon_battleship = icon_battleship[:-2]
                        # mark an 'O' on the hidden grid
                        mygrid[x_coor[x]][int(y)] = 'X'
                        # if the list is empty, the ship has sunk
                        if not largeship:
                            print("Hit! Player's Battleship has sunk!")
                            call_out = False
                            break
                        else:
                            print("Hit! Battleship!")
                            call_out = False
                            break
                    else:
                        continue
            elif x + y in mediumship2:
                for index, value in enumerate(mediumship2):

                    global icon_mediumship2

                    if value == x + y:
                        # remove the coordinate from the list
                        mediumship2.remove(x + y)
                        icon_mediumship2 = icon_mediumship2[:-2]
                        # mark an 'O' on the hidden grid
                        mygrid[x_coor[x]][int(y)] = 'X'
                        # if the list is empty, the ship has sunk
                        if not mediumship2:
                            print("Hit! Player's Cruiser #2 has sunk!")
                            call_out = False
                            break
                        else:
                            print("Hit! Cruiser #2!")
                            call_out = False
                            break
                    else:
                        continue
            elif x + y in mediumship1:
                for index, value in enumerate(mediumship1):

                    global icon_mediumship1

                    if value == x + y:
                        # remove the coordinate from the list
                        mediumship1.remove(x + y)
                        icon_mediumship1 = icon_mediumship1[:-2]
                        # mark an 'O' on the hidden grid
                        mygrid[x_coor[x]][int(y)] = 'X'
                        # if the list is empty, the ship has sunk
                        if not mediumship1:
                            print("Hit! Player's Cruiser #1 has sunk!")
                            call_out = False
                            break
                        else:
                            print("Hit! Cruiser #1!")
                            call_out = False
                            break
                    else:
                        continue
            elif x + y in smallship:
                for index, value in enumerate(smallship):

                    global icon_smallship

                    if value == x + y:
                        # remove the coordinate from the list
                        smallship.remove(x + y)
                        icon_smallship = icon_smallship[:-2]
                        # mark an 'O' on the hidden grid
                        mygrid[x_coor[x]][int(y)] = 'X'
                        print("Hit! Player's Submarine has sunk!")
                        call_out = False
                        break
                    else:
                        continue
        elif mygrid[x_coor[x]][int(y)] == 'X':
            continue

icon_battleship = ''
icon_mediumship2 = ''
icon_mediumship1 = ''
icon_smallship = ''

ai_icon_battleship = ''
ai_icon_mediumship2 = ''
ai_icon_mediumship1 = ''
ai_icon_smallship = ''

horizontal_or_vertical = ['h','v']

ai_x_coor = {1:'A',2:'B',3:'C',4:'D',5:'E'}
x_coor = {'A':1,'B':2,'C':3,'D':4,'E':5}

coordinates = [0] + [[x for x in [0,'1','2','3','4','5']] for x in [0,'A','B','C','D','E']]

mygrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]
aigrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]
hiddengrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]

intro = True
game_start = True

while game_start:

    # Introduction
    while intro:

        mygrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]
        aigrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]
        hiddengrid = [0] + [[0] + [' ' for x in range(5)] for x in range(5)]

        # reset all values
        largeship = []
        mediumship1 = []
        mediumship2 = []
        smallship = []

        icon_battleship = ''
        icon_mediumship2 = ''
        icon_mediumship1 = ''
        icon_smallship = ''

        ai_largeship = []
        ai_mediumship1 = []
        ai_mediumship2 = []
        ai_smallship = []

        ai_icon_battleship = ''
        ai_icon_mediumship2 = ''
        ai_icon_mediumship1 = ''
        ai_icon_smallship = ''

        clear_output()
        print("\nWelcome to Battleship!") 
        print("Place your battleships on the board.\n")
        x = input("Press Enter to Start: ")
        
        place_largeship = True
        break
    
    # ask player to place 4 battleships onto their board
    while place_largeship:
        
        largeship = []
        counter = 1
        
        # place the large battleship first
        # ask the player to input 3 coordinates for the large battleship and then break
        while len(largeship) < 3:
            
            clear_output()
            display_board(mygrid,hiddengrid)

            print("Your Battleship uses 3 coordinates.") 
            x = str(input("Enter coordinate " + str(counter) + " for the Battleship:"))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in largeship:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    icon_battleship += 'O '
                    display_board(mygrid,hiddengrid)
                    largeship.append(x[0].upper() + x[1])
                    counter += 1 
                    continue
                else:
                    continue

        largeship.sort()
        
        # check if the ship was placed vertically
        if largeship[0][0] == largeship[1][0] == largeship[2][0]:
            if int(largeship[0][1]) + 1 == int(largeship[1][1]) and int(largeship[1][1]) + 1 == int(largeship[2][1]):
                # print("This works.")
                place_largeship = False
                place_mediumship1 = True
                break
                
            else:
                # print("These coordinates are not next to each other.")
                mygrid[x_coor[largeship[0][0].upper()]][int(largeship[0][1])] = ' '
                mygrid[x_coor[largeship[1][0].upper()]][int(largeship[1][1])] = ' '
                mygrid[x_coor[largeship[2][0].upper()]][int(largeship[2][1])] = ' '
                icon_battleship = ''
                continue
                
        # check if the ship was placed horizontally
        elif largeship[0][1] == largeship[1][1] == largeship[2][1]:
            if x_coor[largeship[0][0].upper()] + 1 == x_coor[largeship[1][0].upper()] and x_coor[largeship[1][0].upper()]  + 1 == x_coor[largeship[2][0].upper()]:
                # print("This works.")
                place_largeship = False
                place_mediumship1 = True
                break
                
            else:
                # print("These coordinates are not next to each other.")
                mygrid[x_coor[largeship[0][0].upper()]][int(largeship[0][1])] = ' '
                mygrid[x_coor[largeship[1][0].upper()]][int(largeship[1][1])] = ' '
                mygrid[x_coor[largeship[2][0].upper()]][int(largeship[2][1])] = ' '
                icon_battleship = ''        
                continue
        else:
            # print("These coordinates are not next to each other.")
            # print("Place the battleship vertically or horizontally on the board.")
            mygrid[x_coor[largeship[0][0].upper()]][int(largeship[0][1])] = ' '
            mygrid[x_coor[largeship[1][0].upper()]][int(largeship[1][1])] = ' '
            mygrid[x_coor[largeship[2][0].upper()]][int(largeship[2][1])] = ' '
            icon_battleship = ''
            continue
            
    while place_mediumship1:
        
        mediumship1 = []
        counter = 1
                    
        while len(mediumship1) < 2:

            clear_output()
            display_board(mygrid,hiddengrid)
            print("Cruiser #1 uses 2 coordinates.")
            x = str(input("Enter coordinate " + str(counter) + " for Cruiser #1: "))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in mediumship1:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    icon_mediumship1 += 'O '
                    display_board(mygrid,hiddengrid)
                    mediumship1.append(x[0].upper() + x[1])
                    counter += 1 
                    continue
                else:
                    continue
        
        mediumship1.sort()

        # check if the ship was placed vertically
        if mediumship1[0][0] == mediumship1[1][0]:
            if int(mediumship1[0][1]) + 1 == int(mediumship1[1][1]):
                # print("This works.")
                place_mediumship1 = False
                place_mediumship2 = True
                break
            else:
                # print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship1[0][0].upper()]][int(mediumship1[0][1])] = ' '
                mygrid[x_coor[mediumship1[1][0].upper()]][int(mediumship1[1][1])] = ' '
                icon_mediumship1 = ''
                continue

        # check if the ship was placed horizontally
        elif mediumship1[0][1] == mediumship1[1][1]:
            if x_coor[mediumship1[0][0].upper()] + 1 == x_coor[mediumship1[1][0].upper()]:
                # print("This works.")
                place_mediumship1 = False
                place_mediumship2 = True
                break
            else:
                # print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship1[0][0].upper()]][int(mediumship1[0][1])] = ' '
                mygrid[x_coor[mediumship1[1][0].upper()]][int(mediumship1[1][1])] = ' '
                icon_mediumship1 = ''
                continue
        else:
            # print("These coordinates are not next to each other.")
            # print("Place the battleship vertically or horizontally on the board.")
            mygrid[x_coor[mediumship1[0][0].upper()]][int(mediumship1[0][1])] = ' '
            mygrid[x_coor[mediumship1[1][0].upper()]][int(mediumship1[1][1])] = ' '
            icon_mediumship1 = ''
            continue

    while place_mediumship2:
        
        mediumship2 = []
        counter = 1
                    
        while len(mediumship2) < 2:

            clear_output()
            display_board(mygrid,hiddengrid)
            print("Cruiser #2 uses 2 coordinates.")
            x = str(input("Enter coordinate " + str(counter) + " for Cruiser #2:"))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in mediumship2:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    icon_mediumship2 += 'O '
                    display_board(mygrid,hiddengrid)
                    mediumship2.append(x[0].upper() + x[1])
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
                # print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship2[0][0].upper()]][int(mediumship2[0][1])] = ' '
                mygrid[x_coor[mediumship2[1][0].upper()]][int(mediumship2[1][1])] = ' '
                icon_mediumship2 = ''
                continue

        # check if the ship was placed horizontally
        elif mediumship2[0][1] == mediumship2[1][1]:
            if x_coor[mediumship2[0][0].upper()] + 1 == x_coor[mediumship2[1][0].upper()]:
                place_mediumship2 = False
                place_smallship = True
                break
            else:
                # print("These coordinates are not next to each other.")
                mygrid[x_coor[mediumship2[0][0].upper()]][int(mediumship2[0][1])] = ' '
                mygrid[x_coor[mediumship2[1][0].upper()]][int(mediumship2[1][1])] = ' '
                icon_mediumship2 = ''
                continue
        else:
            # print("These coordinates are not next to each other.")
            # print("Place the battleship vertically or horizontally on the board.")
            mygrid[x_coor[mediumship2[0][0].upper()]][int(mediumship2[0][1])] = ' '
            mygrid[x_coor[mediumship2[1][0].upper()]][int(mediumship2[1][1])] = ' '
            icon_mediumship2 = ''
            continue

    while place_smallship:
        
        smallship = []
        counter = 1
        
        while len(smallship) < 1:

            clear_output()
            display_board(mygrid,hiddengrid)
            print("The Submarine uses 1 coordinate.")
            x = str(input("Enter coordinate " + str(counter) + " for the Submarine:"))

            if len(x) != 2:
                continue
            else:
                # accept the input if the space is empty
                if x[0].upper() in ['A','B','C','D','E'] and x[1] in ['1','2','3','4','5'] and mygrid[x_coor[x[0].upper()]][int(x[1])] == ' ' and x not in smallship:
                    mygrid[x_coor[x[0].upper()]][int(x[1])] = 'O'
                    icon_smallship += 'O '
                    display_board(mygrid,hiddengrid)
                    smallship.append(x[0].upper() + x[1])
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
                ai_icon_battleship = 'O O O '
                display_board(mygrid,hiddengrid)
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
                ai_icon_battleship = 'O O O '
                display_board(mygrid,hiddengrid)
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
                ai_icon_mediumship1 = 'O O '
                display_board(mygrid,hiddengrid)
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
                ai_icon_mediumship1 = 'O O '
                display_board(mygrid,hiddengrid)
                ai_place_mediumship1 = False
                ai_place_mediumship2 = True
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
                ai_icon_mediumship2 = 'O O '
                display_board(mygrid,hiddengrid)
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
                ai_icon_mediumship2 = 'O O '
                display_board(mygrid,hiddengrid)
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
                ai_icon_smallship = 'O '
                display_board(mygrid,hiddengrid)
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
                ai_icon_smallship = 'O '
                display_board(mygrid,hiddengrid)
                ai_place_smallship = False
                ai_game_start = False
                break
                
            else:
                continue
    
    clear_output()
    display_board(mygrid,hiddengrid)
    print("AI has placed their ships on their board!\n")
    print("Player goes first!")
    x = input("Press Enter to Continue: ")  

    playing = True

    while playing:

        clear_output()
        display_board(mygrid,hiddengrid)
        hit_or_miss() 
        x = input("Press Enter to Continue: ")  

        if not ai_largeship and not ai_mediumship1 and not ai_mediumship2 and not ai_smallship:
            print("All of AI's ships have sunk!")
            print("Congratulations! You won!\n")
            while True:

                x = input("Play again? Enter [y] or [n]: ")

                if x == 'y':
                    playing = False
                    intro = True
                    break
                elif x == 'n':
                    playing = False
                    game_start = False
                    break
                else:
                    continue
        else:

            clear_output()
            display_board(mygrid,hiddengrid)
            ai_hit_or_miss()
            x = input("Press Enter to Continue: ") 

            if not largeship and not mediumship1 and not mediumship2 and not smallship:
                print("All of Player's ships have sunk!")
                print("Game Over!\n")
                while True:

                    x = input("Play again? Enter [y] or [n]: ")

                    if x == 'y':
                        playing = False
                        intro = True
                        break
                    elif x == 'n':
                        playing = False
                        game_start = False
                        break
                    else:
                        continue
            else:
                continue

