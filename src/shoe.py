from blackjack2.src.deck import Deck

class Shoe(Deck):
    def __init__(self, number_of_decks) -> None:
        # call Deck init first
        super().__init__()

        # initialize cards as specified in the number_of_decks
        self.cards = []
        for _ in range(number_of_decks):
            self.cards.extend(Deck().cards)
        