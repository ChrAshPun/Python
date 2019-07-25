import random
import os

# define clear_output() for Mac
def clear_output():

	os.system('clear')

'''
# define clear_output() for PC
def clear_output():

	os.system('cls')
'''

def welcome():
    
    print("Welcome to Hangman!")

cartoon_characters = ["Homer Simpson","Mickey Mouse","Tommy Pickles"]
tv_shows = ["The Office","Archer","Jane The Virgin","Game of Thrones"]
random_words = ["flapjack","microwave","tripod","zombie","monkey",]

def choose_category():
    
    while True:

        x = input("\nPick a category: \n\n\tRandom Words (r) \n\tTV Shows (s) \n\tCartoon Characters (c) \n\n")

        if x.lower() == 'r':
            return random_words[random.randrange(len(random_words))]
        elif x.lower() == 's':
            return tv_shows[random.randrange(len(tv_shows))]
        elif x.lower() == 'c':
            return cartoon_characters[random.randrange(len(cartoon_characters))]
        else:
            clear_output()
            print("Sorry, please try again.")
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

def hide_func(string):
      
    makelist = []
    
    for x in string:
        
        if x != ' ':
            makelist.append('_')
        else:
            makelist.append(' ')
    
    return ' '.join(makelist)

def display_phrase(phrase):
    print("\n                    " + phrase)

def display_win():
    hangman_board(player_strikes)
    display_phrase(open_phrase)

def guess_letter_or_word(before_phrase,open_phrase,original_phrase):
    
    while True:
        
        after_phrase = list(before_phrase)
        guess = input("Please guess a letter or the entire phrase: ")
        
        # if player guesses the entire phrase correctly, reveal the entire phrase
        if guess.lower() == original_phrase.lower():
            after_phrase = open_phrase
        # ignore these inputs
        elif guess == ' ' or guess == '_' or guess == '':
            continue
        # add a strike for incorrectly guessing the entire phrase
        elif len(guess) > 1 and guess != original_phrase:
            print('Sorry, that is not the phrase.')
        # ignore if letter is already revealed in the phrase
        elif guess.lower() in after_phrase or guess.upper() in after_phrase:
            print('Sorry, you used that letter already.')
            continue
        # add a strike for incorrectly guessing a letter
        elif guess.lower() not in open_phrase.lower() or guess.upper() not in open_phrase.upper(): 
            
        # if player correctly guesses a letter, reveal all instances of that letter in the phrase
        elif guess.lower() in open_phrase.lower() or guess.upper() in open_phrase.upper():

            for num in range(len(open_phrase)):
                if guess[0].lower() == open_phrase[num] or guess[0].upper() == open_phrase[num]:
                    after_phrase[num] = open_phrase[num]
                else:
                    continue
        else:
            print('Sorry, please try again.')
            continue
        
        break
    
    return after_phrase 

def continue_game():
    
    while True:

        x = input("Play again? Enter 'y' or 'n': ")
            
        if x.lower()=='y' and len(x) == 1:
            return 'y'
        elif x.lower()=='n' and len(x) == 1:
            return 'n'
            
        else:
            print("Sorry, please try again.")
            continue

class Strikes:
    
    def __init__(self,total=0):
        self.total = 0  # add by one when player guesses incorrectly
    
    def add_strike(self):
        self.total += 1

game = 'y'

while True:
    
    if game == 'y':
        
        clear_output()
    
        welcome()

        #choose a phrase

        original_phrase = choose_category()

        #AI hides phrase

        before_phrase = hide_func(original_phrase)

        open_phrase = ' '.join(original_phrase)

        player_strikes = Strikes()

        playing = True
    
    elif game == 'n':
        print("Thanks for playing!")
        break
    
    elif game == 'Game Over':
        clear_output()
        hangman_board(player_strikes)
        display_phrase(open_phrase)
        print("Game Over!")
        game = continue_game()
        continue
        
    while playing:

        clear_output()

        #show hangman board & phrase

        hangman_board(player_strikes)
        display_phrase(before_phrase)

        #Ask player to pick a letter or guess the entire phrase

        after_phrase = "".join(guess_letter_or_word(before_phrase,open_phrase,original_phrase))

        if after_phrase == open_phrase:
            clear_output()
            display_win()
            print("Congratulations! You won!")
            play_again = continue_game()
            break

        elif after_phrase == before_phrase:
            player_strikes.add_strike()
            if player_strikes.total < 6:
                before_phrase = after_phrase
                continue
            else:
                game = "Game Over"
                break

        elif after_phrase != before_phrase and after_phrase != open_phrase:
            before_phrase = after_phrase
            continue