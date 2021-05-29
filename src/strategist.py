class Strategist:
    def __init__(self, game) -> None:
        self.game = game

    def get_decision(self):
        return input('Your decision is: ')
    
    def get_curses_decision(self):
        return self.game.display.get_input()