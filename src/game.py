from blackjack2.src.shoe import Shoe
from blackjack2.src.player import Player
from blackjack2.src.display import Display
from blackjack2.src.strategist import Strategist

# Constant values
NO_OF_DECKS = 1

class Game:
    def __init__(self):
        self.shoe = None
        self.hand_stack = []
        self.player_list = []
        self.current_hand = None
        self.all_hand = self.hand_stack.copy()
        self.display = Display(self)
        self.strategist = Strategist()

    def setup_deck(self):
        self.shoe = Shoe(NO_OF_DECKS)
        self.shoe.shuffle()

    def setup_players(self):
        #create dealer
        dealer = Player('dealer', is_dealer = True)
        dealers_hand = dealer.create_hand()
        dealers_hand.draw(self.shoe, 2)
        self.add_hand(dealers_hand)
        self.player_list.append(dealer)
        #create player
        player = Player('player')
        players_hand = player.create_hand()
        players_hand.draw(self.shoe, 2)
        self.add_hand(players_hand)
        self.player_list.append(player)
        self.all_hand = self.hand_stack.copy()

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
        while self.hand_left():
            self.current_hand = self.next_hand()
            self.current_hand.play(self)
        for hand in self.all_hand:
            if hand.name != 'dealer':
                print(self.decide(hand, self.all_hand[0]))
    
    def decide(self, hand, other_hand):
        """return name of winner or tie if scores are equal"""
        # check blackjack cases
        if (hand.is_blackjack() is True) and (other_hand.is_blackjack() is True):
            return 'Tie'
        if (hand.is_blackjack() is True) and (other_hand.is_blackjack() is False):
            return f'{hand.name} won'
        if (hand.is_blackjack() is False) and (other_hand.is_blackjack() is True):
            return f'{other_hand.name} won'
        # check score cases
        if hand.get_score() > other_hand.get_score():
            return f'{hand.name} won'
        elif hand.get_score() < other_hand.get_score():
            return f'{other_hand.name} won'
        else:
            return 'Tie'





        
        



        

