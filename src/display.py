class Display:
    """Display game using normal print."""
    # TODO: make class interface consistent between Display and Curses_display
    # __init__ should not take game as parameter
    # but game object will be passed when call display method.
    def __init__(self, game) -> None:
        self.game = game

    def display(self):
        for hand in self.game.all_hand:
            print(f'{hand.name} \n')
            if hand.name == 'dealer' and self.game.current_hand.name != 'dealer':
                print(hand.cards[0].value, hand.cards[1].suit, '\n')
            else:
                for c in hand.cards:
                    print(c.value, c.suit, '\n')
