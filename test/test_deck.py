from blackjack2.src.deck import Deck
from blackjack2.src.card import Card

def test_deck():
    assert Deck() is not None

def test_deck_cards():
    assert len(Deck().cards) == 52

def test_deck_deal():
    # when dealing from a desk must return a card.
    assert type(Deck().deal()) == Card