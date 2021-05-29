class Display:
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
