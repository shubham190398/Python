#Importing random and setting global variables
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

game_on = True

#Class Definition for a card
class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    #String implementation to print the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#Class definition for a deck
class Deck():
    
    def __init__(self):
        self.allcards = []
        
        #For loop to get all the cards
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit, rank))
                
    #Function to print all the cards of the deck
    def __str__(self):
        deck_contents = 'The deck contains:'
        for card in self.allcards:
            deck_contents += '\n' + card.__str__()
        return deck_contents
    
    def __len__(self):
        return len(self.allcards)
            
    #Function to shuffle
    def shuffle(self):
        random.shuffle(self.allcards)
        
    def deal(self):
        return self.allcards.pop()

#Class definition for a hand
class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    #Function to add cards to hand
    def add_to_hand(self, card):
        self.cards.append(card)
        self.value += card.value
        
        if card.rank == 'Ace':
            self.aces += 1
        
        
    #Function to adjust for number of aces
    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

#Class definition for the Chips in the Player's Hand
class Chips():
    
    def __init__(self, balance = 1000):
        self.balance = balance
        self.bet = 0
        
    def win_bet(self):
        self.balance += self.bet
    
    def lose_bet(self):
        self.balance -= self.bet

#Function to display player's and dealer's hand while hiding one card
def display_some(player, dealer):
    print(f"""
            The dealer's hand is:
            <card hidden> \t {dealer.cards[1].__str__()}
                """)
    print("""
            The player's hand is:\n
            """, *player.cards, sep = '\t')

#Function to display all the cards
def display_all(player, dealer):
    print(f"""
            The dealer's hand is:\n
            """, *dealer.cards, sep = '\t')
    print("\nThe value of dealer's hand is: ", dealer.value)
    print("""
            The player's hand is:\n
            """, *player.cards, sep = '\t')
    print("\nThe value of player's hand is: ", player.value)

#Function to take bets
def take_bet(chips):
    while True:
        #Check for input errors
        try:
            chips.bet = int(input("Please enter the bet amount: "))
        except ValueError:
            print("Sorry, please enter a whole number!")
        #Check for validity of bet
        else:
            if chips.bet > chips.balance:
                print("Your bet amount can't exceed your total balance! Try again.")
            else:
                break
   
#Function to hit
def hit(deck, hand):
    hand.add_to_hand(deck.deal())
    hand.adjust_for_aces() 

#Function to hit or stand
def hit_or_stand(deck, hand):
    #Declare game_on globally to control an upcoming while loop
    global game_on
    
    while True:
        decision = input("Do you want to Hit or stand: ")
        
        #Check for hit or stand
        if decision[0].upper() == 'H':
            hit(deck, hand)
        elif decision[0].upper() == 'S':
            print("The player chooses to stand. It is now the dealer's turn.")
            game_on = False
        else:
            print("Invalid Input. Please try again.")
            continue
        break

#Functions to decide who won
def player_busts(chips):
    print("\nPlayer Busts! Dealer wins!")
    chips.lose_bet()
    
def dealer_busts(chips):
    print("\nDealer Busts! Player wins")
    chips.win_bet()
    
def player_wins(chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_wins(chips):
    print("\nDealer wins!")
    chips.lose_bet()
    
def push():
    print("\nIts a tie!")

#Function to print instructions
def instructions():
    print("""
            Welcome to BlackJack! 
            Face cards are worth 10.
            Aces are worth 11 or 1.
            Ace and a Face card correspond to BlackJack.
            Try to get as close to 21 as possible.
            Dealer must hit below 18 and must stand at or above 18.
                """)

#Game logic

#Print instructions
instructions()

#Set up player's balance
while True:
    try:
        player_balance = int(input("Enter the amount you want to add to your chips: "))
    except ValueError:
        print("Invalid Input. Try again and enter a whole number")
    else:
        player_chips = Chips(player_balance)
        break
    
#Create a shuffled deck
deck = Deck()
deck.shuffle()
    
while True:
    
    #Create a new deck if less than 20 cards remain
    if len(deck) < 20:
        deck = Deck()
        deck.shuffle()
    
    #Setup player and dealer hands
    player_hand = Hand()
    player_hand.add_to_hand(deck.deal())
    player_hand.add_to_hand(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_to_hand(deck.deal())
    dealer_hand.add_to_hand(deck.deal())
    
    #Take a bet
    take_bet(player_chips)
    
    #Show half the hands
    display_some(player_hand, dealer_hand)
    
    while game_on:
        hit_or_stand(deck, player_hand)
        display_some(player_hand, dealer_hand)
        
        #Check if player has busted
        if player_hand.value > 21:
            player_busts(player_chips)
            break
    
    if player_hand.value <= 21:
        #Dealer must hit till 18 and stand above that
        while dealer_hand.value < 18:
            hit(deck, dealer_hand)

        #Display the entire table
        display_all(player_hand, dealer_hand)
        
        #Check for win conditions
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()
    
    #Show current balance
    print(f"\nYour current balance is: {player_chips.balance}")
    
    #Ask user if he wants to continue
    decide_newgame = input("Would you like to continue? Press Y to continue and any other key to exit.")
    
    if decide_newgame.upper() == 'Y':
        game_on = True
        continue
    else:
        print("Thank you for playing!")
        break
