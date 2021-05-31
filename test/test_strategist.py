from blackjack2.src.strategist import Strategist

#test class
class Game:
    def get_input(self):
        return True
def test_Strategist_init():
    assert Strategist('game') is not None

def test_get_curses_decision():
    assert Strategist(Game()).get_curses_decision() == True


