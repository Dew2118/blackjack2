from blackjack2.src.card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = ['']*52

    def deal(self):
        return Card()