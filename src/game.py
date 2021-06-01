from blackjack2.src.shoe import Shoe
from blackjack2.src.hand import Hand
from blackjack2.src.strategist import Strategist
from blackjack2.src.bet import Bet
import time
import sys
if not "pytest" in sys.modules:
    from blackjack2.src.curses_display import display as display_object
else:
    display_object = None
# Constant values
NO_OF_DECKS = 1

class Game:
    def __init__(self):
        self.shoe = None
        self.hand_stack = []
        self.split_counter = 1
        self.bet = Bet(10000)
        self.current_hand = None
        self.all_hands = self.hand_stack.copy()
        self.strategist = Strategist(self)
        self.running_count = 0

    

    def display(self):
        display_object.display(self)

    def display_unknown_input(self):
        display_object.display_unknown_input()

    def get_input(self):
        return display_object.get_input()

    def get_bet_amount(self):
        return display_object.get_bet_amount()

    def setup_deck(self):
        self.shoe = Shoe(NO_OF_DECKS)
        self.shoe.shuffle()

    def setup_players(self):
        #create dealer
        dealers_hand = Hand('dealer')
        dealers_hand.draw(self, 2)
        self.add_hand(dealers_hand)
        if not "pytest" in sys.modules:
            players_hand = Hand('player', self.bet.bet(int(self.get_bet_amount())))
        else:
            players_hand = Hand('player')
        #remove bet from bankroll
        players_hand.draw(self, 2)
        self.add_hand(players_hand)
        self.all_hands = self.hand_stack.copy()

    def add_hand(self, hand):
        self.hand_stack.append(hand)

    def next_hand(self):
        return self.hand_stack.pop()

    def hand_left(self):
        return (len(self.hand_stack) > 0)

    #test
    def update_running_count(self):
        result = 0
        drawn = self.shoe.drawn
        for c in drawn:
            if c.score <= 6:
                result += 1
            if c.score >= 10:
                result += -1
        if self.current_hand.name != 'dealer':
            if self.all_hands[0].cards[1].score <= 6:
                result -= 1
            elif self.all_hands[0].cards[1].score >= 10:
                result += 1
        self.running_count = result

    def play(self):
        self.setup_deck()
        while self.shoe.cards:
            self.setup_players()
            while self.hand_left():
                self.current_hand = self.next_hand()
                self.current_hand.play(self)
            display_object.display(self)
            # decide the game
            for count, hand in enumerate(self.all_hands):
                if hand.name != 'dealer':
                    result = self.decide(hand, self.all_hands[0])
                    if result == f'{hand.name} won':
                        self.bet.win(hand.bet_amount)
                    elif result == f'{hand.name} won w BJ!':
                        self.bet.blackjack(hand.bet_amount)
                    display_object.display_decide(hand.name, result, count - 1)
            display_object.clear()

    
    def decide(self, hand, other_hand):
        """return name of winner or tie if scores are equal"""
        # check blackjack cases
        if (hand.is_blackjack() is True) and (other_hand.is_blackjack() is False):
            return f'{hand.name} won w BJ!'
        if (hand.is_blackjack() is False) and (other_hand.is_blackjack() is True):
            return f'{other_hand.name} won w BJ!'
        # check busted cases
        if (hand.is_busted() is True) and (other_hand.is_busted() is False):
            return f'{other_hand.name} won'
        if (hand.is_busted() is False) and (other_hand.is_busted() is True):
            return f'{hand.name} won'
        # check score cases
        if hand.get_score() > other_hand.get_score():
            return f'{hand.name} won'
        elif hand.get_score() < other_hand.get_score():
            return f'{other_hand.name} won'
        else:
            return 'Tie'