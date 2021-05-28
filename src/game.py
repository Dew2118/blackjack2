from blackjack2.src.shoe import Shoe

# Constant values
NO_OF_DECKS = 1

class Game:
    def __init__(self):
        self.shoe = None

    def setup_deck(self):
        self.shoe = Shoe(NO_OF_DECKS)
        self.shoe.shuffle()

    def setup_player(self, player_name):
        player = Player(player_name)
        players_hand = player.create_hand()
        return player, players_hand

