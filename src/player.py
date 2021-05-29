from blackjack2.src.hand import Hand

class Player:
    def __init__(self, player_name, is_dealer = False):
        self.name = player_name
        self.hands = []

    def create_hand(self, name = None):
        hand = Hand(self.name)
        self.hands.append(hand)
        return hand
