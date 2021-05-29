from blackjack2.src.game import Game
from blackjack2.src.hand import Hand
from blackjack2.src.card import Card

def test_game_init():
    assert Game() is not None

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
    hand.cards = [Card('A','S'), Card('J','S')]
    other_hand.cards = [Card('A','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == 'Tie'
    hand.cards = [Card('A','S'), Card('J','S')]
    other_hand.cards = [Card('2','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == f'{hand.name} won'
    hand.cards = [Card('2','S'), Card('10','S')]
    other_hand.cards = [Card('A','S'), Card('J','S')]
    assert Game().decide(hand, other_hand) == f'{other_hand.name} won'
    hand.cards = [Card('3','S'), Card('J','S')]
    other_hand.cards = [Card('2','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == f'{hand.name} won'
    hand.cards = [Card('2','S'), Card('10','S')]
    other_hand.cards = [Card('3','S'), Card('J','S')]
    assert Game().decide(hand, other_hand) == f'{other_hand.name} won'
    hand.cards = [Card('5','D'), Card('J','S')]
    other_hand.cards = [Card('5','S'), Card('10','S')]
    assert Game().decide(hand, other_hand) == 'Tie'