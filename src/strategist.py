from blackjack2.src.deviation import Deviation

class Strategist:
    def __init__(self, game) -> None:
        self.game = game

    def get_decision(self):
        return input('Your decision is: ')
    
    def get_curses_decision(self):
        return self.game.get_input()

    def make_decision(self, game):
        if game.current_hand.name != 'dealer':
            ace = False
            for card in game.current_hand.cards:
                if card.score == 11:
                    ace = True
            return Deviation(game).main(game.current_hand.get_score(), game.all_hands[0].cards[0].score, ace, game.current_hand.is_splittable())
        else:
            return self.get_curses_decision()




