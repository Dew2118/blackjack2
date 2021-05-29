from blackjack2.src.shoe import Shoe
from blackjack2.src.player import Player

# Constant values
NO_OF_DECKS = 1

class Game:
    def __init__(self):
        self.shoe = None
        self.hand_stack = []
        self.current_hand = None

    def setup_deck(self):
        self.shoe = Shoe(NO_OF_DECKS)
        self.shoe.shuffle()

    def setup_players(self):
        #create dealer
        dealer = Player('dealer', is_dealer = True)
        dealers_hand = dealer.create_hand()
        dealers_hand.draw(2)
        self.add_hand(dealers_hand)
        #create player
        player = Player('player')
        players_hand = player.create_hand()
        players_hand.draw(2)
        self.add_hand(players_hand)

    def setup_hand(self, hand):
        hand.draw(self.shoe)

    def add_hand(self, hand):
        self.hand_stack.append(hand)

    def next_hand(self):
        return self.hand_stack.pop()

    def hand_left(self):
        return (len(self.hand_stack) > 0)

    def play(self):
        self.setup_deck()
        self.setup_players()
        self.current_hand = self.next_hand()
        while self.hand_left():
            hand = self.next_hand()




        
        



        

