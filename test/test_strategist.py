from src.strategist import Strategist
from src.hand import Hand
from src.card import Card

#test class
class Game:
    def get_input(self):
        return True
def test_Strategist_init():
    assert Strategist('game') is not None

def test_get_curses_decision():
    assert Strategist(Game()).get_curses_decision() == True

def test_make_decision():
    game = Game()
    h = Hand('player')
    ha = Hand('dealer')
    ha.cards = [Card('3','D')]
    h.cards = [Card('2','C'), Card('7','C')]
    game.all_hands = [ha, h]
    game.current_hand = h
    sttg = Strategist(game)
    assert sttg.make_decision(game) == 'd'

    game = Game()
    h = Hand('player')
    ha = Hand('dealer')
    ha.cards = [Card('3','D')]
    h.cards = [Card('A','C'), Card('7','C')]
    game.all_hands = [ha, h]
    game.current_hand = h
    sttg = Strategist(game)
    assert sttg.make_decision(game) == 'd'

    game = Game()
    game.current_hand = Hand('dealer')
    sttg = Strategist(game)
    assert sttg.make_decision(game) == True




