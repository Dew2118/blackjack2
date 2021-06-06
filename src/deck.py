from src.card import Card
import random
from src.custom_exception import DeckError

class Deck:
    def __init__(self) -> None:
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suit = ['S','H','D','C']
        self.cards = [Card(v,s) for v in value for s in suit]
        self.drawn = []

    def deal(self, game):
        """return a Card. Raise Deckerror if there is no card left."""
        if len(self.cards) - 1 < 0:
            # raise DeckError('Run out of deck, consider starting a new game')
            game.setup_deck()
            return
        result = self.cards.pop(0)
        self.drawn.append(result)
        return result
        
    def shuffle(self):
        """Shuffle deck in place"""
        random.shuffle(self.cards)