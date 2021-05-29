class Card:
    SCORE = {'A':11,'J':10,'Q':10,'K':10,}
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
        if self.value in self.SCORE:
            self.score = self.SCORE[self.value]
        else:
            self.score = int(self.value)

    
    def __eq__(self, o):
        return (self.value == o.value) and (self.suit == o.suit)