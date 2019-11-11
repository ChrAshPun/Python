import random
import os

# define clear function for Mac & Linux
def clear_output():

	os.system('clear')

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

values_visual = {'Two':'2 ', 'Three':'3 ', 'Four':'4 ', 'Five':'5 ', 'Six':'6 ', 'Seven':'7 ', 'Eight':'8 ', 
         'Nine':'9 ', 'Ten':'10', 'Jack':'J ', 'Queen':'Q ', 'King':'K ', 'Ace':'A '}

class Card:

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank,suit))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    # add an attribute to keep track of aces
        self.tens = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
        elif card.rank == 'Ten' or card.rank == 'Jack' or card.rank == 'Queen' or card.rank == 'King':
            self.tens += 1

    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

class Chips:
    
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_blackjack_bet(self):
        self.total += round(self.bet * 1.5)
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Please enter a whole number.')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed " + str(chips.total))
            elif chips.bet <= 0:
                print('Please place a bet.')
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        
        x = input("\nWould you like to Hit or Stand? Enter h or s: ")
            
        if x == 'h':
            hit(deck,hand)  # hit() function defined above
            clear_output()
            break
            
        elif x == 's':
            print("Player stands. Dealer is playing.")
            playing = False
            clear_output()
            break
            
        else:
            print("Sorry, please enter h or s.")
            continue

def check_for_blackjack(player):
        if len(player.cards) == 2:
            if player.tens == 1 and player.aces == 1:
                return True
            else:
                return False
        else:
            return False

def show_dealer_some(dealer):

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
    print("              {}           \n".format("?     of     ?"))

def show_dealer_all(dealer):

    if len(dealer.cards) == 2:

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
        print("              {}           \n".format(dealer.cards[0]))
        
    elif len(dealer.cards) == 3:

        print("\nDealer's Hand:")

        print("                    ------- ")
        print("                   | {}    |".format(values_visual[dealer.cards[2].rank]))
        print("                   |       |")
        print("                ---|       |")
        print("               | {}|       |".format(values_visual[dealer.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[dealer.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |    ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[dealer.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(dealer.cards[2]))
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           \n".format(dealer.cards[0]))

    elif len(dealer.cards) == 4:

        print("\nDealer's Hand:")

        print("                        ------- ")
        print("                       | {}    |".format(values_visual[dealer.cards[3].rank]))
        print("                       |       |")
        print("                    ---|       |")
        print("                   | {}|       |".format(values_visual[dealer.cards[2].rank]))
        print("                   |   |     {}|".format(values_visual[dealer.cards[3].rank]))
        print("                ---|    ------- ")
        print("               | {}|       |".format(values_visual[dealer.cards[1].rank]))
        print("               |   |     {}|".format(values_visual[dealer.cards[2].rank]))
        print("            ---|    ------- ")
        print("           | {}|       |    ".format(values_visual[dealer.cards[0].rank]))
        print("           |   |     {}|    ".format(values_visual[dealer.cards[1].rank]))
        print("           |    -------     ")
        print("           |       |        ")
        print("           |     {}|        ".format(values_visual[dealer.cards[0].rank]))
        print("            -------         ")
        print("              {}           ".format(dealer.cards[3]))        
        print("              {}           ".format(dealer.cards[2]))
        print("              {}           ".format(dealer.cards[1]))
        print("              {}           \n".format(dealer.cards[0]))
        
    else:
        print("\nDealer's Hand: \n")
        for card in dealer_hand.cards:
            print("           " + str(card))

def show_player_all(player):

    if len(player.cards) == 2:

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
        print("\n           Current Bet: {}".format(player_chips.bet))
        print("           Total Chips: {}".format(player_chips.total))
        print("\nPlayer's Hand:")
        
    else:
        print("\nPlayer's Hand: \n")
        for card in player_hand.cards:
            print("           " + str(card))

def player_busts(player,dealer,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins_blackjack(player,dealer,chips):
    print("\nPlayer wins Blackjack!")
    chips.win_blackjack_bet()

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

game_on = True
intro = True
deal_cards = False
playing = False

while game_on:

    while intro:
        clear_output()
        print("\nWelcome to Blackjack!") 
        print("\nThis version of Blackjack does not allow splits.")
        print("The Dealer hits until 17 or more.")
        print("A winning blackjack pays 3:2.")
        print("\nYour starting amount of chips is: 100")
        player_chips = Chips()
        deal_cards = True
        break

    while deal_cards:

        # create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
            
        # prompt the Player for their bet
        take_bet(player_chips)
        clear_output()

        # show cards (but keep one dealer card hidden)
        show_dealer_some(dealer_hand)
        show_player_all(player_hand)
        playing = True
        break

    while playing:  # recall this variable from our hit_or_stand function

        # prompt Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        clear_output()

        # show cards (but keep one dealer card hidden)
        show_dealer_some(dealer_hand)
        show_player_all(player_hand)

        # if player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            clear_output()
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # if player hasn't busted, play dealer's hand until dealer reaches 17             
    if player_hand.value <= 21:

        while dealer_hand.value < 17:

            hit(deck,dealer_hand)    
 
        # run different winning scenarios
        clear_output()
        # check if player got blackjack
        if check_for_blackjack(player_hand):
            if dealer_hand.value != 21:
                player_wins_blackjack(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand) 

        # dealer busts
        elif dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        # dealer wins
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        # player wins
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        # push
        else:
            push(player_hand,dealer_hand)        

    # show all hands & player's total chips
    show_dealer_all(dealer_hand)
    show_player_all(player_hand)

    # if player busts, ask if they want to play again
    if player_chips.total == 0:

        print("\nSorry, you ran out of chips!")
        print("Game Over!\n")

        # if player ran out of chips, ask if they want to play again
        while player_chips.total == 0:

            x = input("Play again? Enter y or n: ")
            if x == 'y' or x == 'n':
                break
            else:
                print("Please try again.")  

        # go back to the intro                             
        if x == 'y':
            intro = True
            continue
        # exit game
        else:
            print("Thanks for playing!")
            break   

    else:
        
        # if player still has chips, ask if they want to keep playing
        while player_chips.total > 0:

            x = input("Do you want to play another hand? Enter y or n: ")
            if x == 'y' or x == 'n':
                break
            else:
                print("Please try again.")

        # skip the intro & deal another hand
        if x == 'y':
            intro = False
            deal_cards = True
            continue
        #exit game
        else:
            print("Thanks for playing!")
            break