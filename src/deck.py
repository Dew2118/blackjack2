from blackjack2.src.card import Card
import random


class Deck:
    def __init__(self) -> None:
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suit = ['S','H','D','C']
        self.cards = [Card(v,s) for v in value for s in suit]

    def deal(self):
        if self.cards == []:
            raise RuntimeError
        result = self.cards.pop(0)
        return result
        
    def shuffle(self):
        random.shuffle(self.cards)