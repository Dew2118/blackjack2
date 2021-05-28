from blackjack2.src.shoe import Shoe

def test_parameter():
    assert Shoe(4) is not None

def test_Shoe_init():
    assert len(Shoe(1).cards) == 52