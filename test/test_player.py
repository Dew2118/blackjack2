from blackjack2.src.player import Player
from blackjack2.src.hand import Hand

def test_player_init():
    player = Player('name')
    assert player is not None
    assert player.name == 'name'

def test_create_hand():
    player = Player('name')
    # there is no hand in player at the beginning
    assert len(player.hands) == 0
    hand = player.create_hand()
    assert type(hand) is Hand

    # after create hand, the newly created hand must be added to player.hands
    assert len(player.hands) == 1
    hand2 = player.hands[0]
    assert hand == hand2
    hand3 = player.create_hand()
    assert player.hands[1] == hand3