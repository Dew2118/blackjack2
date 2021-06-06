from src.shoe import Shoe
from src.card import Card

def test_parameter():
    assert Shoe(4) is not None

def test_Shoe_init():
    assert len(Shoe(1).cards) == 52
    assert len(Shoe(2).cards) == 52 * 2

def test_shoe_deal():
    # when dealing from a desk must return a card.
    # and the number of cards in the deck must be one less than earlier
    shoe = Shoe(2)
    no_of_cards = len(shoe.cards)
    # if no shuffle, the first card will be Ace of spade
    assert shoe.deal('game') == Card('A','S')
    assert len(shoe.cards) == no_of_cards-1