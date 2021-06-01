class Display:
    """Display game using normal print."""
    # DONE: make class interface consistent between Display and Curses_display
    # __init__ should not take game as parameter
    # but game object will be passed when call display method.

    def display(self, game):
        for hand in game.all_hands:
            print(f'{hand.name} \n')
            if hand.name == 'dealer' and game.current_hand.name != 'dealer':
                print(hand.cards[0].value, hand.cards[1].suit, '\n')
            else:
                for c in hand.cards:
                    print(c.value, c.suit, '\n')
