from blackjack2.src.deck import Deck
from blackjack2.src.card import Card
import pytest

def test_deck():
    assert Deck() is not None

def test_deck_cards():
    assert len(Deck().cards) == 52

def test_deck_deal():
    # when dealing from a desk must return a card.
    # and the number of cards in the deck must be one less than earlier
    deck = Deck()
    # if no shuffle, the first card will be Ace of spade
    assert deck.deal() == Card('A','S')
    assert len(deck.cards) == 51
    # deal and throw away 50 cards
    for _ in range(50):
        deck.deal()
    # the last card must be King of clubs.
    assert deck.deal() == Card('K','C')
    assert len(deck.cards) == 0
    # if trying to deal from an empty deck, RuntimeError will be raised
    with pytest.raises(RuntimeError) as e_info:
        deck.deal()

def test_shuffle():
    deck = Deck()
    # if no shuffle, the first card will be Ace of spade
    init_card_list = deck.cards.copy()
    assert len(init_card_list) == 52
    deck.shuffle()
    # after shuffle, the card list should be different
    assert len(deck.cards) == 52
    cmp_result = ((a==b) for a,b in zip(deck.cards, init_card_list))
    assert all(cmp_result) == False