from src.shoe import Shoe
from src.hand import Hand
from src.strategist import Strategist
from src.bet import Bet
import sys
if not "pytest" in sys.modules:
    from src.curses_display import display as display_object
else:
    display_object = None
# Constant values
NO_OF_DECKS = 1
BANKROLL_AMOUNT = 10000

class Game:
    def __init__(self):
        self.shoe = None
        self.hand_stack = []
        self.split_counter = 1
        self.bet = Bet(BANKROLL_AMOUNT)
        self.current_hand = None
        self.all_hands = self.hand_stack.copy()
        self.strategist = Strategist(self)
        self.running_count = 0
        self.dealers_hand = None

    def display(self):
        display_object.display(self)
        display_object.execute()

    def display_unknown_input(self):
        display_object.display_unknown_input()
        display_object.execute()

    def get_input(self):
        return display_object.get_input()

    def get_bet_amount(self):
        return display_object.get_bet_amount()

    def setup_deck(self):
        self.shoe = Shoe(NO_OF_DECKS)
        self.shoe.shuffle()

    def setup_players(self):
        #create dealer
        self.dealers_hand = Hand('dealer')
        self.dealers_hand.draw(self, 2)
        self.add_hand(self.dealers_hand)
        players_hand = Hand('player', self.bet.bet(int(self.get_bet_amount())))
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
            if self.dealers_hand.cards[1].score <= 6:
                result -= 1
            elif self.dealers_hand.cards[1].score >= 10:
                result += 1
        self.running_count = result

    def play(self):
        self.setup_deck()
        while self.shoe.cards:
            self.setup_players()
            while self.hand_left():
                self.current_hand = self.next_hand()
                self.current_hand.play(self)
            self.split_counter = 1
            display_object.display(self)
            display_object.execute()
            # decide the game
            for count, hand in enumerate(self.all_hands):
                if hand.name != 'dealer':
                    result = self.decide(hand, self.dealers_hand)
                    if result == {hand.name}:
                        self.bet.win(hand.bet_amount)
                    elif result == f'{hand.name} BJ':
                        self.bet.blackjack(hand.bet_amount)
                    display_object.display_decide(hand.name, result, count - 1)
                    display_object.execute()
            display_object.clear()
            display_object.execute()

    
    def decide(self, hand, other_hand):
        """return name of winner or tie if scores are equal"""
        # check blackjack cases
        if (hand.is_blackjack() is True) and (other_hand.is_blackjack() is False):
            return f'{hand.name} BJ'
        if (hand.is_blackjack() is False) and (other_hand.is_blackjack() is True):
            return f'{other_hand.name} BJ'
        # check busted cases
        if (hand.is_busted() is True) and (other_hand.is_busted() is False):
            return other_hand.name
        if (hand.is_busted() is False) and (other_hand.is_busted() is True):
            return hand.name
        # check score cases
        if hand.get_score() > other_hand.get_score():
            return hand.name
        elif hand.get_score() < other_hand.get_score():
            return other_hand.name
        else:
            return 'Tie'