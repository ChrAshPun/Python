import os
import random

def clear_output():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_matches():
    
    c=[]
    for x in range(0,11):
        for index, value in enumerate(fu_c):
            if value == fu_c[x]:
                c.append(index)
    d = c[::2]
    e = c[1::2]
    return tuple(zip(d,e))

def Intro():
    
    # intro cards will be different every time
    # faceup_intro
    fu_i = ['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ']
    random.shuffle(fu_i)

    print("WELCOME TO MEMORY GAME\n".rjust(34))

    print(" -------     -------     -------     ------- ")
    print("| {}    |   | {}    |   | {}    |   | {}    |".format(fu_i[0],fu_i[1],fu_i[2],fu_i[3]))
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fu_i[0],fu_i[1],fu_i[2],fu_i[3]))
    print(" -------     -------     -------     ------- ")
    print("\nCan you beat an AI with perfect memory?")
    i = input("\nPress Enter to begin: ")

class Player:
    
    def __init__(self,points=0):
        self.points = 0
    
    def add_point(self):
        self.points += 1

def reset_fd_c():

    for index, value in enumerate(fd_c):
        if value == 'P1':
            pass
        elif value == 'AI':
            pass
        else:
            fd_c[index] = '  '

def facedown_cards():
    
    print(" -------     -------     -------     -------               Score")
    print("| {}    |   | {}    |   | {}    |   | {}    |".format(fd_c[0],fd_c[1],fd_c[2],fd_c[3]))
    print("|       |   |       |   |       |   |       |              Player One: {}".format(player_one.points))
    print("|       |   |       |   |       |   |       |              AI: {}".format(player_ai.points))
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[0],fd_c[1],fd_c[2],fd_c[3]))
    print(" -------     -------     -------     -------               0 |1 |2 |3 ")
    print(" -------     -------     -------     -------               -----------")
    print("| {}    |   | {}    |   | {}    |   | {}    |              4 |5 |6 |7 ".format(fd_c[4],fd_c[5],fd_c[6],fd_c[7]))
    print("|       |   |       |   |       |   |       |              -----------")
    print("|       |   |       |   |       |   |       |              8 |9 |10|11")
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[4],fd_c[5],fd_c[6],fd_c[7]))
    print(" -------     -------     -------     ------- ")
    print(" -------     -------     -------     ------- ")
    print("| {}    |   | {}    |   | {}    |   | {}    |".format(fd_c[8],fd_c[9],fd_c[10],fd_c[11]))
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[8],fd_c[9],fd_c[10],fd_c[11]))
    print(" -------     -------     -------     ------- \n")

def first_choice():
    
    while True:
        
        try:
            first_index = int(input("Flip a card: "))
            if first_index in range(0,12):
                if fd_c[first_index] == 'P1' or fd_c[first_index] == 'AI':
                    print("Choose another card")
                    continue
                else:
                    return first_index
            else:
                continue
        except ValueError:
            continue

def first_faceup():
    
    fd_c[first_index] = fu_c[first_index]
    
    print(" -------     -------     -------     -------               Score")
    print("| {}    |   | {}    |   | {}    |   | {}    |".format(fd_c[0],fd_c[1],fd_c[2],fd_c[3]))
    print("|       |   |       |   |       |   |       |              Player One: {}".format(player_one.points))
    print("|       |   |       |   |       |   |       |              AI: {}".format(player_ai.points))
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[0],fd_c[1],fd_c[2],fd_c[3]))
    print(" -------     -------     -------     -------               0 |1 |2 |3 ")
    print(" -------     -------     -------     -------               -----------")
    print("| {}    |   | {}    |   | {}    |   | {}    |              4 |5 |6 |7 ".format(fd_c[4],fd_c[5],fd_c[6],fd_c[7]))
    print("|       |   |       |   |       |   |       |              -----------")
    print("|       |   |       |   |       |   |       |              8 |9 |10|11")
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[4],fd_c[5],fd_c[6],fd_c[7]))
    print(" -------     -------     -------     ------- ")
    print(" -------     -------     -------     ------- ")
    print("| {}    |   | {}    |   | {}    |   | {}    |".format(fd_c[8],fd_c[9],fd_c[10],fd_c[11]))
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[8],fd_c[9],fd_c[10],fd_c[11]))
    print(" -------     -------     -------     ------- \n")

def second_choice():
    
    while True:
        
        try:
            second_index = int(input("Flip a second card: "))
            if second_index in range(0,12):
                if fd_c[second_index] == 'P1' or fd_c[second_index] == 'AI':
                    print("Choose another card")
                    continue
                elif second_index == first_index:
                    print("Choose another card")
                    continue                   
                else:
                    return second_index              
            else:
                continue             
        except ValueError:
            continue  

def second_faceup():
    
    fd_c[first_index] = fu_c[first_index]
    fd_c[second_index] = fu_c[second_index]   
    
    print(" -------     -------     -------     -------               Score")
    print("| {}    |   | {}    |   | {}    |   | {}    |".format(fd_c[0],fd_c[1],fd_c[2],fd_c[3]))
    print("|       |   |       |   |       |   |       |              Player One: {}".format(player_one.points))
    print("|       |   |       |   |       |   |       |              AI: {}".format(player_ai.points))
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[0],fd_c[1],fd_c[2],fd_c[3]))
    print(" -------     -------     -------     -------               0 |1 |2 |3 ")
    print(" -------     -------     -------     -------               -----------")
    print("| {}    |   | {}    |   | {}    |   | {}    |              4 |5 |6 |7 ".format(fd_c[4],fd_c[5],fd_c[6],fd_c[7]))
    print("|       |   |       |   |       |   |       |              -----------")
    print("|       |   |       |   |       |   |       |              8 |9 |10|11")
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[4],fd_c[5],fd_c[6],fd_c[7]))
    print(" -------     -------     -------     ------- ")
    print(" -------     -------     -------     ------- ")
    print("| {}    |   | {}    |   | {}    |   | {}    |".format(fd_c[8],fd_c[9],fd_c[10],fd_c[11]))
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|       |   |       |   |       |   |       |")
    print("|     {}|   |     {}|   |     {}|   |     {}|".format(fd_c[8],fd_c[9],fd_c[10],fd_c[11]))
    print(" -------     -------     -------     ------- \n")

def update_sets():
    
    if first_index in revealed:
        revealed.remove(first_index)
    if second_index in revealed:
        revealed.remove(second_index)
    
    if first_index in available:
        available.remove(first_index)
    if second_index in available:
        available.remove(second_index)

def add_to_revealed():
    
    revealed.add(first_index)
    revealed.add(second_index)

def check_revealed():  
    
    for match in matches:
        if not set(match) - revealed:
            return match

def ai_first_choice():

    if len(unknown) > 0:
        return random.choice(tuple(unknown))
    else:
        return random.choice(tuple(available))

def remove_first_index():
    
    unknown.remove(first_index)
    available.remove(first_index)

def create_ai_lists():
    
    create_ai_revealed()
    create_ai_valid()

def create_ai_revealed():
    
    for x in revealed:
        if fu_c[x] == 'P1':
            pass
        elif fu_c[x] == 'AI':
            pass
        else:
            ai_revealed.append(x)

def create_ai_valid():
    
    for x in range(0,12):
        if fu_c[x] == 'AI':
            pass
        elif fu_c[x] == 'P1':
            pass
        else:
            ai_valid.append(x)

def ai_second_choice():
    
    if matching_index in revealed:
        return matching_index
    else:
        if len(unknown) > 0:
            return random.choice(tuple(unknown))
        else:
            return random.choice(tuple(available))

# this AI will have perfect memory
# have the AI randomly choose a card
# then run a func to find the index of it's matching value
# if that index is in ai_revealed, match them together

def find_match():

    for index, value in enumerate(fu_c):
        if index != first_index:
            if fu_c[index] == fu_c[first_index]:
                return index

def remove_from_set():
    
    if first_index in revealed:
        revealed.remove(first_index)
    if second_index in revealed:
        revealed.remove(second_index)
    
    if first_index in available:
        available.remove(first_index)
    if second_index in available:
        available.remove(second_index)

def create_matches():
    
    c=[]

    for x in range(0,11):
        for index, value in enumerate(fu_c):
            if value == fu_c[x]:
                c.append(index)

    d = c[::2]
    e = c[1::2]

    return tuple(zip(d,e))

def readd_first_index():
    
    available.add(first_index)

def continue_game():
    
    while True:

        x = input("Play again? Enter [y] or [n]: ")
            
        if x[0].lower()=='y' and len(x) == 1:
            return True
        elif x[0].lower()=='n' and len(x) == 1:
            print("Thanks for playing!")
            break
        else:
            continue

game_start = True

while game_start:
        
        # facedown_cards
        fd_c = ['  ']*12
        # faceup_cards
        fu_c = ['A ','2 ','3 ','4 ','5 ','6 ']*2
        # sets
        revealed = set()
        available = set([0,1,2,3,4,5,6,7,8,9,10,11])
        # shuffle cards
        random.shuffle(fu_c)
        matches = create_matches()
        # create players
        player_one = Player()
        player_ai = Player()
        
        clear_output()
        Intro()
        
        #game_start = False
        #win_scenarios = False
        player_turn = True
    
        ##################################################
        while player_turn:

            #reset facedown cards    
            clear_output()    
            reset_fd_c()
            facedown_cards()

            #first flip
            first_index = first_choice()
            clear_output() 
            first_faceup()

            #second flip
            second_index = second_choice()
            clear_output()     
            second_faceup()

            if fu_c[first_index] == fu_c[second_index]:
                #add a point for player_one
                player_one.add_point()
                fd_c[first_index] = 'P1'
                fd_c[second_index] = 'P1'
                print("You found a match!")
                i = input("Press Enter to continue: ")
                #remove indexes from available & revealed
                update_sets()
                if not available:
                    win_scenarios = True
                    break
                else:
                    continue

            elif fu_c[first_index] != fu_c[second_index]:
                #add indexes to revealed
                add_to_revealed()
                ai_turn = True  

            print("You didn't find a match.")
            print("AI goes next.")
            i = input("Press Enter to continue: ")

            #########################################################
            while ai_turn:

                #reset facedown cards    
                clear_output()    
                reset_fd_c()
                facedown_cards()

                if check_revealed():

                    #if a match is within revealed
                    z = check_revealed()
                    first_index = z[0]
                    second_index = z[1]

                    clear_output() 
                    first_faceup()

                    print("AI flipped a card.")
                    i = input("Press Enter to continue: ")

                    clear_output()
                    second_faceup()

                    print("AI found a match!")
                    i = input("Press Enter to continue: ") 

                    #add a point for player_ai
                    player_ai.add_point()
                    fd_c[first_index] = 'AI'
                    fd_c[second_index] = 'AI'
                    #remove indexes from available & revealed
                    update_sets()
                    reset_fd_c()
                    if not available:
                        player_turn = False
                        win_scenarios = True
                        break
                    else:
                        continue

                else:

                    clear_output() 
                    #create unknown 
                    unknown = set(available) - set(revealed)
                    #first flip
                    first_index = ai_first_choice()
                    clear_output()
                    first_faceup()

                    print("AI flipped a card.")
                    i = input("Press Enter to continue: ")

                    #remove first_index as an option from unknown & available
                    remove_first_index()
                    #find matching_index
                    matching_index = find_match()


                    #second flip
                    second_index = ai_second_choice()
                    clear_output()
                    second_faceup()

                if fu_c[first_index] == fu_c[second_index]:
                    print("AI found a match!")
                    i = input("Press Enter to continue: ") 
                    #add a point for player_one
                    player_ai.add_point()
                    fd_c[first_index] = 'AI'
                    fd_c[second_index] = 'AI'
                    #remove both indexes from available & revealed
                    update_sets()
                    if not available:
                        # declare False or it will continue to player_turn even if win_scenarios is True
                        player_turn = False
                        win_scenarios = True
                        break
                    else:
                        continue

                elif fu_c[first_index] != fu_c[second_index]:
                    print("AI did not find a match.")
                    print("Player goes next.")
                    i = input("Press Enter to continue: ") 
                    #add indexes to revealed
                    add_to_revealed()
                    #readd first_index to available
                    readd_first_index()
                    reset_fd_c()
                    #don't need player_turn = True
                    break

        while win_scenarios:

            if player_ai.points > player_one.points:
                #reset facedown cards    
                clear_output()    
                reset_fd_c()
                facedown_cards()
                print("AI won!")
                break
                
            elif player_one.points > player_ai.points:
                #reset facedown cards    
                clear_output()    
                reset_fd_c()
                facedown_cards()
                print("You won!")
                break

            elif player_one.points == player_ai.points:
                #reset facedown cards    
                clear_output()    
                reset_fd_c()
                facedown_cards()
                print("It was a tie!")
                break
        
        game_start = continue_game()