import random

def intro():   
   
    print("Welcome to Blackjack!") 
    print("\nThis version of Blackjack does not allow splits.")
    print("The Dealer hits until 17 or more.")
    print("\nYour starting amount of chips is: 100")

intro()

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
        
testdeck = Deck()

print(testdeck)