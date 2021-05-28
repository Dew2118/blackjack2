class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
    
    def __eq__(self, o):
        return (self.value == o.value) and (self.suit == o.suit)