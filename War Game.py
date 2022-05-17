#Dictionary of Values
#Tuples of Suits and Ranks
#Import shuffle

from random import shuffle

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Card Class
#Understands suit and rank

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    #Returns the card created
    def __str__(self):
        return self.rank + " of " + self.suit 

#Deck Class
#Will Create a Deck

class Deck:
    
    def __init__(self):        
        self.deck = []
        
    #Creating all the cards for the deck
        for suit in suits:            
            for rank in ranks:
                self.deck.append(Card(suit, rank)) 
                
    #Shuffling the Deck            
    def shuffle(self):
        shuffle(self.deck)  
        
    #Removing the top card of the deck
    def deal_top(self):
        return self.deck.pop()  
        

#Player Class

class Player:
    
    def __init__(self, name):
        
        self.name = name
        self.deck = []
    
    def __str__(self):
        
        return f"{self.name} has {len(self.deck)} cards"
    
    #Removing a card
    def remove_one(self):
        
        return self.deck.pop(0)
        
    #Adding cards
    def add_cards(self, new_cards): 
        
        if type(new_cards) == type([]):
            self.deck.extend(new_cards)
        else:
            self.deck.append(new_cards)

#Game Setup
player_one = Player("Player One")
player_two = Player("Player Two")

new_deck = Deck()
new_deck.shuffle()

#Distributing the Cards
for cards in range(26): 
    player_one.add_cards(new_deck.deal_top())
    player_two.add_cards(new_deck.deal_top())
    
#Initialising number of rounds
round_number = 0

#Initalising game status
game_status = True

while game_status: #While game is running
    
    #Putting a hard cap on the round limit
    if round_number >= 1000:
        print("Too many rounds! This game is declared to be a tie.")
        break
    
    #Check if a player has won
    if len(player_one.deck) == 0:
        print(f"{player_one.name} is out of cards. {player_two.name} Wins!")
        break
    
    if len(player_two.deck) == 0:
        print(f"{player_two.name} is out of cards. {player_one.name} Wins!")
        break
        
    #New Round
    
    round_number += 1
    print(f"Round {round_number}:")
    
    #Adding one card from player one's deck to the table
    player_one_table = []
    player_one_table.append(player_one.remove_one()) 
    
    #Adding one card from player two's deck to the table
    player_two_table = []
    player_two_table.append(player_two.remove_one()) 
    
    #Initialising parameter to check for war
    war = True
    
    while war:
                
        #Checking the last cards of both players
        if player_one_table[-1].value > player_two_table [-1].value:
            war = False
            
            player_one.add_cards(player_one_table)
            player_one.add_cards(player_two_table)
        
        elif player_two_table[-1].value > player_one_table [-1].value:
            war = False
            
            player_two.add_cards(player_one_table)
            player_two.add_cards(player_two_table)
         
        #If neither of the above is true, they are at war
        else:
            print("At War!")

            #Checking if enough cards available for war
            if len(player_one.deck) < 5:
                print(f"{player_one.name} is unable to continue. {player_two.name} wins!")
                game_status = False
                break
                
            elif len(player_two.deck) < 5:
                print(f"{player_two.name} is unable to continue. {player_one.name} wins!")
                game_status = False
                break
               
            #Remove enough cards for war
            else:
                for number in range(5):
                    player_one_table.append(player_one.remove_one())
                    player_two_table.append(player_two.remove_one())
                    

#Testing
if __name__ == '__main__':
    test = Deck()
    assert len(test.deck) == 52
