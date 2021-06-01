from blackjack2.src.hand import Hand
from blackjack2.src.game import Game
from blackjack2.src.card import Card

def test_hand_init():
    assert Hand is not None

def test_draw():
    hand = Hand('player')
    game = Game()
    game.setup_deck()
    hand.draw(game, 1)
    assert len(hand.cards) == 1
    hand.draw(game, 2)
    assert len(hand.cards) == 3

def test_get_score():
    hand = Hand('player')
    hand.cards = [Card('2','S'), Card('3','C')]
    assert hand.get_score() == 5
    hand.cards = [Card('10','S'), Card('A','C')]
    assert hand.get_score() == 21
    hand.cards = [Card('10','S'), Card('10','S'), Card('A','C')]
    assert hand.get_score() == 21
    hand.cards = [Card('10','S'), Card('A','S'), Card('A','C')]
    assert hand.get_score() == 12
    hand.cards = [Card('A','S'), Card('A','C')]
    assert hand.get_score() == 12
    # TODO: add more test condisions when we have multiple ACE cards
    # and see whether the code correctly adjusts the score. 

def test_is_busted():
    hand = Hand('player')
    hand.cards = [Card('10','S'), Card('A','C')]
    assert hand.is_busted() == False
    hand.cards = [Card('10','S'), Card('10','C'), Card('2','C')]
    assert hand.is_busted() == True

def test_isascii():
    assert Hand('name').isascii('ยกหดฟก') == False
    assert Hand('name').isascii('s') == True

def test_is_blackjack():
    hand = Hand('player')
    hand.cards = [Card('10','S'), Card('A','C')]
    hand.is_blackjack() == True
    hand.cards = [Card('J','S'), Card('A','C')]
    hand.is_blackjack() == True
    hand.cards = [Card('Q','S'), Card('A','C')]
    hand.is_blackjack() == True
    hand.cards = [Card('K','S'), Card('A','C')]
    hand.is_blackjack() == True
    hand.cards = [Card('9','S'), Card('A','C')]
    hand.is_blackjack() == False

def test_is_splittable():
    hand = Hand('player')
    hand.cards = [Card('Q','S'), Card('K','C')]
    assert hand.is_splittable() == False
    hand.cards = [Card('K','S'), Card('K','C')]
    assert hand.is_splittable() == True
    hand.cards = [Card('K','S'), Card('K','C'), Card('K','D')]
    assert hand.is_splittable() == False

def test_split():
    hand = Hand('name', bet_amount = 100)
    hand.cards  = [Card('A','S')]
    assert hand.split(Game()) == 'rt'

    hand = Hand('name', bet_amount = 100)
    hand.cards  = [Card('A','S'), Card('A','C')]
    game = Game()
    br = game.bet.current_bankroll
    hand.split(game)
    assert hand.cards == [Card('A','S')]
    assert game.bet.current_bankroll == br - 100
    assert game.hand_stack[-1] == game.all_hands[-1]
    assert game.hand_stack[-1].bet_amount == 100