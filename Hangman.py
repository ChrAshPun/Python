import os
import random
from collections import OrderedDict 

def clear_output():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')  

# categories
cartoon_characters = ["Homer Simpson","Mickey Mouse","Tommy Pickles","Patrick Star","SpongeBob SquarePants","Bugs Bunny"]
tv_shows = ["The Office","The Sopranos","Jane The Virgin","Game of Thrones","Rick and Morty","Friends"]
video_games = ["Legend of Zelda","Call of Duty","Pokemon","Metal Gear Solid","The Last of Us","Minecraft","World of Warcraft"]

def choose_category():
    
    while True:

        # ask player to pick a category
        x = input("Enter v s or c: ")

        if x.lower() == 'v':
            return video_games[random.randrange(len(video_games))]
        elif x.lower() == 's':
            return tv_shows[random.randrange(len(tv_shows))]
        elif x.lower() == 'c':
            return cartoon_characters[random.randrange(len(cartoon_characters))]
        else:
            print("Please pick a category.")
            continue                
        break

def hangman_board(player_strikes):

    if player_strikes.total == 0:
        print("        ________       ")
        print("       |        |      ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("  _____|_____          ")
        
    elif player_strikes.total == 1:
        print("        ________       ")
        print("       |        |      ")
        print("       |       ( )     ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("  _____|_____          ")
        
    elif player_strikes.total == 2:
        print("        ________       ")
        print("       |        |      ")
        print("       |       ( )     ")
        print("       |        |      ")
        print("       |        |      ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("  _____|_____          ")
           
    elif player_strikes.total == 3:
        print("        ________       ")
        print("       |        |      ")
        print("       |       ( )     ")
        print("       |       /|      ")
        print("       |        |      ")
        print("       |               ")
        print("       |               ")
        print("       |               ")
        print("  _____|_____          ")
         
    elif player_strikes.total == 4:
        print("        ________       ")
        print("       |        |      ")
        print("       |       ( )     ")
        print("       |       /|      ")
        print("       |        |      ")
        print("       |       /       ")
        print("       |               ")
        print("       |               ")
        print("  _____|_____          ")
          
    elif player_strikes.total == 5:
        print("        ________       ")
        print("       |        |      ")
        print("       |       ( )     ")
        print("       |       /|\     ")
        print("       |        |      ")
        print("       |       /       ")
        print("       |               ")
        print("       |               ")
        print("  _____|_____          ")
          
    elif player_strikes.total == 6:
        print("        ________       ")
        print("       |        |      ")
        print("       |     (x___x)   ")
        print("       |       /|\     ")
        print("       |        |      ")
        print("       |       / \     ")
        print("       |               ")
        print("       |               ")
        print("  _____|_____          ")
         
# conceal the phrase
def hide_func(string):
      
    makelist = []
    
    for x in string:
        # change characters into "_"
        if x != ' ':
            makelist.append('_')
        # change everything else into " "
        else:
            makelist.append(' ')
    
    return ' '.join(makelist)

def display_phrase(phrase):
    print("\n\t\t" + phrase)

def display_win():
    hangman_board(player_strikes)
    display_phrase(open_phrase)

def guess_letter_or_word(before_phrase,open_phrase,original_phrase):
    
    while True:
        
        global used_letters
        after_phrase = list(before_phrase)
        guess = input("\nGuess a letter or the entire phrase: ")
        
        # if player guesses the entire phrase correctly, reveal the entire phrase
        if guess.lower() == original_phrase.lower():
            after_phrase = open_phrase
            
        # ignore these inputs
        elif guess == ' ' or guess == '_' or guess == '':
            clear_output()
            hangman_board(player_strikes)
            display_phrase(before_phrase)
            print("\nUsed letters: " + " ".join(OrderedDict.fromkeys(used_letters)))
            continue

        # add a strike for incorrectly guessing the entire phrase
        elif len(guess) > 1 and guess != original_phrase:
            print('Sorry, that is not the phrase.')
            
        # ignore if letter is already in used letters
        elif guess.lower() in used_letters or guess.upper() in used_letters:
            clear_output()
            hangman_board(player_strikes)
            display_phrase(before_phrase)
            print("\nUsed letters: " + " ".join(OrderedDict.fromkeys(used_letters)))
            continue

        # add a strike for incorrectly guessing a letter
        elif guess.lower() not in open_phrase.lower() or guess.upper() not in open_phrase.upper(): 
            used_letters += guess.lower()
            
        # if player correctly guesses a letter, reveal all instances of that letter in the phrase
        elif guess.lower() in open_phrase.lower() or guess.upper() in open_phrase.upper():

            for num in range(len(open_phrase)):
                if guess.lower() == open_phrase[num] or guess.upper() == open_phrase[num]:
                    after_phrase[num] = open_phrase[num]
                    used_letters += guess.lower()
                else:
                    clear_output()
                    hangman_board(player_strikes)
                    display_phrase(before_phrase)
                    print("\nUsed letters: " + " ".join(OrderedDict.fromkeys(used_letters)))
                    continue

        else:
            clear_output()
            hangman_board(player_strikes)
            display_phrase(before_phrase)
            print("\nUsed letters: " + " ".join(OrderedDict.fromkeys(used_letters)))
            continue
        break
    
    return after_phrase 

def continue_game():
    
    while True:

        x = input("Play again? Enter y or n: ")
            
        if x.lower()=='y':
            return True
        elif x.lower()=='n':
            print("Thanks for playing!")
            return False
        else:
            print("Please try again.")
            continue

class Strikes:
    
    def __init__(self,total=0):
        self.total = 0  # add by one when player guesses incorrectly
    
    def add_strike(self):
        self.total += 1

start = True
intro = True

while start:
    
    while intro:
        
        # intro
        clear_output()
        print("Welcome to Hangman!")

        # choose a category
        print("\nPick a category: \n\n\tVideo Games (v) \n\tTV Shows (s) \n\tCartoon Characters (c) \n")
        original_phrase = choose_category()

        #hide the phrase
        before_phrase = hide_func(original_phrase)
        open_phrase = ' '.join(original_phrase)

        player_strikes = Strikes()
        # reset used letters str
        used_letters = ""

        playing = True
        break
        
    while playing:

        clear_output()

        # show hangman board & hidden phrase
        hangman_board(player_strikes)
        display_phrase(before_phrase)
        print("\nUsed letters: " + " ".join(OrderedDict.fromkeys(used_letters)))

        # Ask player to pick a letter or guess the entire phrase
        after_phrase = "".join(guess_letter_or_word(before_phrase,open_phrase,original_phrase))
        
        # if the player wins, ask if they want to play again
        if after_phrase == open_phrase:
            clear_output()
            display_win()
            print("\nCongratulations! You won!")
            start = continue_game()
            break

        # if the hidden phrase hasn't changed after the user makes a guess, add a strike
        elif after_phrase == before_phrase:
            player_strikes.add_strike()
            if player_strikes.total < 6:
                before_phrase = after_phrase
                continue
            else:
                break

        # if the player guesses a letter correctly, turn the before phrase to the after phrase
        elif after_phrase != before_phrase and after_phrase != open_phrase:
            before_phrase = after_phrase
            continue
    
    # if the player loses, ask if the want to play again
    while player_strikes.total == 6:
        clear_output()
        hangman_board(player_strikes)
        display_phrase(open_phrase)
        print("\nGame Over!\n")
        start = continue_game()
        break