from src.game import Game
import src.game as _game
from src import game
from src.hand import Hand
from src.card import Card

game._called_from_test = True
def test_game_init():
    assert Game() is not None

#test_curses_display_class
class Display_test:
    def __init__(self):
        self.test = False
    
    def display(self, p):
        self.test = True

    def display_unknown_input(self):
        self.test = True

    def get_input(self):
        self.test = True

    def get_bet_amount(self):
        self.test = True

    def execute(self):
        pass



def test_hand_stack():
    game = Game()
    assert game.hand_stack == []
    hand = Hand('player')
    game.add_hand(hand)
    assert game.hand_stack[0] == hand

def test_next_hand():
    game = Game()
    assert game.hand_stack == []
    hand = Hand('player')
    hand2 = Hand('player')
    game.add_hand(hand)
    game.add_hand(hand2)
    assert game.next_hand() == hand2
    assert len(game.hand_stack) == 1
    hand3 = Hand('player')
    game.add_hand(hand3)
    assert game.next_hand() == hand3
    assert len(game.hand_stack) == 1
    assert game.next_hand() == hand
    assert len(game.hand_stack) == 0

#mocks
class Bet:
    def bet(self, amount):
        return amount

class Display:
    def get_bet_amount(self):
        return 100 

def test_setup_players():
    _game.display_object = Display()
    game = Game()
    game.setup_deck()
    game.bet = Bet()
    game.setup_players()
    dealers_hand = game.all_hands[0]
    players_hand = game.all_hands[1]
    assert type(dealers_hand) == Hand
    assert len(dealers_hand.cards) == 2
    assert type(players_hand) == Hand
    assert len(players_hand.cards) == 2

def test_update_running_count():
    game = Game()
    game.setup_deck()
    game.shoe.drawn = [Card('A','S')]
    game.current_hand = Hand('player')
    hand = Hand('test')
    hand.cards = [Card('8','C'), Card('10','C')]
    game.dealers_hand = hand
    game.update_running_count()
    assert game.running_count == 0
    game = Game()
    game.setup_deck()
    game.shoe.drawn = [Card('3','S')]
    game.current_hand = Hand('player')
    hand = Hand('test')
    hand.cards = [Card('10','C'), Card('3','C')]
    game.dealers_hand = hand
    game.update_running_count()
    assert game.running_count == 0

def test_display():
    _game.display_object = Display_test()
    assert _game.display_object.test == False
    Game().display()
    assert _game.display_object.test == True

def test_display_unknown_input():
    _game.display_object = Display_test()
    assert _game.display_object.test == False
    Game().display_unknown_input()
    assert _game.display_object.test == True

def test_get_input():
    _game.display_object = Display_test()
    assert _game.display_object.test == False
    Game().get_input()
    assert _game.display_object.test == True

def test_get_bet_amount():
    _game.display_object = Display_test()
    assert _game.display_object.test == False
    Game().get_bet_amount()
    assert _game.display_object.test == True

def test_no_hand_left():
    game = Game()
    assert game.hand_left() == False
    game.add_hand(Hand('player'))
    assert game.hand_left() == True
    game.next_hand()
    assert game.hand_left() == False

def test_decide():
    hand = Hand('player')
    other_hand = Hand('dealer')
    #check blackjack
    hand.cards = [Card('A','S'), Card('J','S')]
    other_hand.cards = [Card('A','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == 'Tie'
    hand.cards = [Card('A','S'), Card('J','S')]
    other_hand.cards = [Card('2','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == f'{hand.name} BJ'
    hand.cards = [Card('2','S'), Card('10','S')]
    other_hand.cards = [Card('A','S'), Card('J','S')]
    assert Game().decide(hand, other_hand) == f'{other_hand.name} BJ'
    #check busted
    hand.cards = [Card('J','C'), Card('J','S'), Card('2','S')]
    other_hand.cards = [Card('2','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == other_hand.name
    hand.cards = [Card('3','S'), Card('J','S')]
    other_hand.cards = [Card('2','S'), Card('10','S'), Card('5','S'), Card('7','S')]
    assert Game().decide(hand, other_hand) == hand.name
    #check for more score
    hand.cards = [Card('3','S'), Card('J','S')]
    other_hand.cards = [Card('2','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == hand.name
    hand.cards = [Card('2','S'), Card('10','S')]
    other_hand.cards = [Card('3','S'), Card('J','S')]
    assert Game().decide(hand, other_hand) == other_hand.name
    #tie
    hand.cards = [Card('5','D'), Card('J','S')]
    other_hand.cards = [Card('5','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == 'Tie'