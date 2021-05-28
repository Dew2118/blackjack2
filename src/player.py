from blackjack2.src.hand import Hand

class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.hands = []

    def create_hand(self):
        hand = Hand()
        self.hands.append(hand)
        return hand