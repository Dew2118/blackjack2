from blackjack2.src.shoe import Shoe
from blackjack2.src.hand import Hand
from blackjack2.src.curses_display import Display
from blackjack2.src.strategist import Strategist

# Constant values
NO_OF_DECKS = 1

class Game:
    def __init__(self):
        self.shoe = None
        self.hand_stack = []
        self.current_hand = None
        self.all_hand = self.hand_stack.copy()
        self.display = Display(self)
        self.strategist = Strategist(self)

    def setup_deck(self):
        self.shoe = Shoe(NO_OF_DECKS)
        self.shoe.shuffle()

    def setup_players(self):
        #create dealer
        dealers_hand = Hand('dealer')
        dealers_hand.draw(self.shoe, 2)
        self.add_hand(dealers_hand)
        players_hand = Hand('player')
        players_hand.draw(self.shoe, 2)
        self.add_hand(players_hand)
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
        for count, hand in enumerate(self.all_hand):
            if hand.name != 'dealer':
                # print(self.decide(hand, self.all_hand[0]))
                self.display.display_decide(hand.name, self.decide(hand, self.all_hand[0]), count - 1)
    
    def decide(self, hand, other_hand):
        """return name of winner or tie if scores are equal"""
        # check blackjack cases
        if (hand.is_blackjack() is True) and (other_hand.is_blackjack() is False):
            return f'{hand.name} won'
        if (hand.is_blackjack() is False) and (other_hand.is_blackjack() is True):
            return f'{other_hand.name} won'
        # check busted cases
        if (hand.is_busted() is True) and (hand.is_busted() is False):
            return f'{hand.name} won'
        if (hand.is_busted() is False) and (hand.is_busted() is True):
            return f'{other_hand.name} won'
        # check score cases
        if hand.get_score() > other_hand.get_score():
            return f'{hand.name} won'
        elif hand.get_score() < other_hand.get_score():
            return f'{other_hand.name} won'
        else:
            return 'Tie'





        
        



        

