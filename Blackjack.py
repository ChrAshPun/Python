import random
import os

def clear_output():

	os.system('clear')

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

values_visual = {'Two':'2 ', 'Three':'3 ', 'Four':'4 ', 'Five':'5 ', 'Six':'6 ', 'Seven':'7 ', 'Eight':'8 ', 
         'Nine':'9 ', 'Ten':'10', 'Jack':'J ', 'Queen':'Q ', 'King':'K ', 'Ace':'A '}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
            clear_output()
        except ValueError:
            print('Please enter a number.')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
            
        if x[0].lower() == 'h' and len(x) == 1:
            hit(deck,hand)  # hit() function defined above
            clear_output()
            break
            
        elif x[0].lower() == 's' and len(x) == 1:
            print("Player stands. Dealer is playing.")
            playing = False
            clear_output()
            break
            
        else:
            print("\nSorry, please try again.")
            continue

def show_some(player,dealer):
    
    if len(player.cards) == 2:
        
        print("\nDealer's Hand:")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[dealer.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | ? |       |   ")
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     ? |      ")
        print("            -------       ")
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format("?     of     ?"))

        print("\n \n")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[player.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | {}|       |   ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[player.cards[1].rank]))
        print("           |    ------    ")
        print("           |       |     ")
        print("           |     {}|      ".format(values_visual[player.cards[0].rank]))
        print("            -------      ")
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("\n           Current Bet: {}".format(player_chips.bet))
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")
    
    elif len(player.cards) == 3:

        print("\nDealer's Hand:")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[dealer.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | ? |       |   ")
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     ? |      ")
        print("            -------       ")
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format("?     of     ?"))

        print("\n \n")
 
        print("                    ------- ")
        print("                   | {}    |".format(values_visual[player.cards[2].rank]))
        print("                   |       |")
        print("                ---|       |")
        print("               | {}|       |".format(values_visual[player.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[player.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |    ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[player.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[player.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(player.cards[2]))
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("\n           Current Bet: {}".format(player_chips.bet))
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")

              
    elif len(player.cards) == 4:

        print("\nDealer's Hand:")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[dealer.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | ? |       |   ")
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     ? |      ")
        print("            -------       ")
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format("?     of     ?"))

        print("\n \n")
 
        print("                        ------- ")
        print("                       | {}    |".format(values_visual[player.cards[3].rank]))
        print("                       |       |")
        print("                    ---|       |")
        print("                   | {}|       |".format(values_visual[player.cards[2].rank]))
        print("                   |   |     {}|".format(values_visual[player.cards[3].rank]))
        print("                ---|    ------- ")
        print("               | {}|       |".format(values_visual[player.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[player.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |    ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[player.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[player.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(player.cards[3]))        
        print("              {}           ".format(player.cards[2]))
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("\n           Current Bet: {}".format(player_chips.bet))
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")

    def show_all(player,dealer):
    
    if len(player.cards) == 2 and len(dealer.cards) == 2:
        
        print("\nDealer's Hand:")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[dealer.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | {}|       |   ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     {}|      ".format(values_visual[dealer.cards[0].rank]))
        print("            -------       ")
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format(dealer.cards[0]))

        print("\n \n")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[player.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | {}|       |   ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[player.cards[1].rank]))
        print("           |    ------    ")
        print("           |       |     ")
        print("           |     {}|      ".format(values_visual[player.cards[0].rank]))
        print("            -------      ")
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("")
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")
        
    elif len(player.cards) == 3 and len(dealer.cards) == 2:

        print("\nDealer's Hand:")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[dealer.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | {}|       |   ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     {}|      ".format(values_visual[dealer.cards[0].rank]))
        print("            -------       ")
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format(dealer.cards[0]))

        print("\n \n")
 
        print("                    ------- ")
        print("                   | {}    |".format(values_visual[player.cards[2].rank]))
        print("                   |       |")
        print("                ---|       |")
        print("               | {}|       |".format(values_visual[player.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[player.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |    ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[player.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[player.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(player.cards[2]))
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("")
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")
        
    elif len(player.cards) == 2 and len(dealer.cards) == 3:

        print("\nDealer's Hand:")

        print("                    ------- ")
        print("                   | {}    |".format(values_visual[dealer.cards[2].rank]))
        print("                   |       |")
        print("                ---|       |")
        print("               | {}|       |".format(values_visual[dealer.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[dealer.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |   ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     {}|      ".format(values_visual[dealer.cards[0].rank]))
        print("            -------       ")
        print("              {}           ".format(dealer.cards[2]))
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format(dealer.cards[0]))

        print("\n \n")
        
        print("                -------    ")
        print("               | {}    |   ".format(values_visual[player.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | {}|       |   ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[player.cards[1].rank]))
        print("           |    ------    ")
        print("           |       |     ")
        print("           |     {}|      ".format(values_visual[player.cards[0].rank]))
        print("            -------      ")
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("")
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")
    
    elif len(player.cards) == 3 and len(dealer.cards) == 3:

        print("\nDealer's Hand:")

        print("                    ------- ")
        print("                   | {}    |".format(values_visual[dealer.cards[2].rank]))
        print("                   |       |")
        print("                ---|       |")
        print("               | {}|       |".format(values_visual[dealer.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[dealer.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |   ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     {}|      ".format(values_visual[dealer.cards[0].rank]))
        print("            -------       ")
        print("              {}           ".format(dealer.cards[2]))
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format(dealer.cards[0]))

        print("\n \n")
 
        print("                    ------- ")
        print("                   | {}    |".format(values_visual[player.cards[2].rank]))
        print("                   |       |")
        print("                ---|       |")
        print("               | {}|       |".format(values_visual[player.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[player.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |    ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[player.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[player.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(player.cards[2]))
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("")
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")
        
    elif len(player.cards) == 4 and len(dealer.cards) == 2:

        print("\nDealer's Hand:")

        print("                -------    ")
        print("               | {}    |   ".format(values_visual[dealer.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | {}|       |   ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------   ")
        print("           |       |      ")
        print("           |     {}|      ".format(values_visual[dealer.cards[0].rank]))
        print("            -------       ")
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format(dealer.cards[0]))

        print("\n \n")

        print("                        -------  ")
        print("                       | {}    | ".format(values_visual[player.cards[3].rank]))
        print("                       |       | ")
        print("                    ---|       | ")
        print("                   | {}|       | ".format(values_visual[player.cards[2].rank]))
        print("                   |   |     {}| ".format(values_visual[player.cards[3].rank]))
        print("                ---|    -------  ")
        print("               | {}|       |     ".format(values_visual[player.cards[1].rank]))
        print("               |   |     {}|     ".format(values_visual[player.cards[2].rank]))
        print("            ---|    -------      ")
        print("           | {}|       |    ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[player.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[player.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(player.cards[3]))       
        print("              {}           ".format(player.cards[2]))
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("")
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")

        
    elif len(player.cards) == 2 and len(dealer.cards) == 4:
        
        print("                        -------  ")
        print("                       | {}    | ".format(values_visual[dealer.cards[3].rank]))
        print("                       |       | ")
        print("                    ---|       | ")
        print("                   | {}|       | ".format(values_visual[dealer.cards[2].rank]))
        print("                   |   |     {}| ".format(values_visual[dealer.cards[3].rank]))
        print("                ---|    -------  ")
        print("               | {}|       |     ".format(values_visual[dealer.cards[1].rank]))
        print("               |   |     {}|     ".format(values_visual[dealer.cards[2].rank]))
        print("            ---|    -------      ")
        print("           | {}|       |    ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[dealer.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(dealer.cards[3]))
        print("              {}           ".format(dealer.cards[2]))
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           ".format(dealer.cards[0]))
        
        print("\n \n")
        
        print("                -------    ")
        print("               | {}    |   ".format(values_visual[player.cards[1].rank]))
        print("               |       |   ")
        print("            ---|       |   ")
        print("           | {}|       |   ".format(values_visual[player.cards[0].rank]))
        print("           |   |     {}|   ".format(values_visual[player.cards[1].rank]))
        print("           |    ------    ")
        print("           |       |     ")
        print("           |     {}|      ".format(values_visual[player.cards[0].rank]))
        print("            -------      ")
        print("              {}           ".format(player.cards[1]))
        print("              {}           ".format(player.cards[0]))
        print("")
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")
        
    else:
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =",dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("\nDealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("\nDealer and Player tie! It's a push.")

def continue_game():
    
    while True:
        
        try:
            x = input("Would you like to play another hand? Enter 'y' or 'n': ")
            
            if continue_game[0].lower()=='y':
                playing=True
                continue
            elif continue_game[0].lower()=='n':
                print("Thanks for playing!")
                break
        except:
            print("Sorry, please try again.")
            continue
        else:
            continue

print("WELCOME TO BLACKJACK") 
print("\nThis version of Blackjack does not allow splits.")
print("The Dealer hits until 17 or more.")
print("\nYour starting amount of chips is: 100")
player_chips = Chips()

playing = True

while True:

        # Print an opening statement
        

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        
        '''
        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100    
        '''
    
        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck,player_hand) 

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand,dealer_hand)  

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                show_some(player_hand,dealer_hand)
                clear_output()
                player_busts(player_hand,dealer_hand,player_chips)
                break        


        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
        
        clear_output()
        
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck,dealer_hand)    
            '''
            # Show all cards
            show_all(player_hand,dealer_hand)
            '''
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)        

        # Inform Player of their chips total 
        show_all(player_hand,dealer_hand)
        print("\nTotal Chips: {}".format(player_chips.total))
        
        if player_chips.total == 0:
            print("Sorry, you ran out of chips!")
            print("Game Over!")
            break
            
        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break