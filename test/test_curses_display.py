from blackjack2.src.curses_display import Display
from blackjack2.src.game import Game
from blackjack2.src.hand import Hand
from blackjack2.src.card import Card
from dataclasses import dataclass

@dataclass
class Addstr:
    y : int
    x : int
    text : str

@dataclass
class Getstr:
    y : int
    x : int

class Stdscr:
    def __init__(self) -> None:
        self.action = []
    def addstr(self, y, x, text):
        self.action.append(Addstr(y,x,text))

    def refresh(self):
        self.action.append('refresh')

    def clear(self):
        self.action.append('clear')

    def getstr(self, y, x):
        self.action.append(Getstr(y,x))
        return b''

def test_get_input():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.get_input()
    assert stdscr.action[0] == Addstr(35, 0, '                            ')
    assert stdscr.action[1] == Addstr(35, 0, 'Your decision is: ')
    assert stdscr.action[2] == 'refresh'
    assert stdscr.action[3] == Getstr(35, len('Your decision is: '))

def test_get_bet_amount():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.get_bet_amount()
    assert stdscr.action[0] == Addstr(35, 0, 'Your betting amount is: ')
    assert stdscr.action[1] == 'refresh'
    assert stdscr.action[2] == Getstr(35, len('Your betting amount is: '))

def test_display_bankroll():
    game = Game()
    stdscr = Stdscr()
    display = Display(stdscr)
    display.game = game
    display.display_bankroll()
    assert stdscr.action[0] == Addstr(38, 0, f'Your current bankroll is: {game.bet.current_bankroll}')

def test_display_bet():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.display_bet(Hand('player',100), 0)
    assert stdscr.action[0] == Addstr(1, 0, str(100))

def test_display_score():
    game = Game()
    stdscr = Stdscr()
    display = Display(stdscr)
    display.game = game
    hand = Hand('dealer',100)
    game.current_hand = hand
    hand.cards = [Card('A','S')]
    display.display_score(hand, 0)
    assert stdscr.action[0] == Addstr(6, 0, str(11))

    game = Game()
    stdscr = Stdscr()
    display = Display(stdscr)
    display.game = game
    hand = Hand('dealer',100)
    game.current_hand = Hand('player')
    hand.cards = [Card('A','S'), Card('2','C')]
    display.display_score(hand, 0)
    assert stdscr.action[0] == Addstr(6, 0, str(11))

def test_display_card():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.display_card(0, 0, '#')
    for a in range(6):
        assert stdscr.action[a * 2] == Addstr(0, 0 + a, '#')
        assert stdscr.action[a * 2 + 1] == Addstr(0 + 6, 0 + a, '#')
    for b in range(7):
        assert stdscr.action[b * 2 + 12] == Addstr(0 + b, 0, '#')
        assert stdscr.action[b * 2 + 13] == Addstr(0 + b, 0 + 6, '#')

def test_display_card_symbol():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.display_card_symbol(0, 0, 'A', 'S')
    assert stdscr.action[0] == Addstr(1, 1, 'A')
    assert stdscr.action[1] == Addstr(1, 1 + len(str('A')), '\u2660')
    assert stdscr.action[2] == Addstr(5, 5 - len(str('A')), 'A')
    assert stdscr.action[3] == Addstr(5, 5, '\u2660')

def test_display_arrow():
    game = Game()
    stdscr = Stdscr()
    display = Display(stdscr)
    display.game = game
    game.current_hand = Hand('player')
    display.display_arrow()
    assert stdscr.action[0] == Addstr(0 + 3, 0, '      ')
    assert stdscr.action[1] == Addstr(7 + 3, 0, '      ')
    assert stdscr.action[2] == Addstr(14 + 3, 0, '      ')
    assert stdscr.action[3] == Addstr(21 + 3, 0, '      ')
    assert stdscr.action[4] == Addstr(28 + 3, 0, '      ')
    assert stdscr.action[5] == Addstr(7 + 3, 0, '----->')

def test_display_name():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.display_name(Hand('player'))
    assert stdscr.action[0] == Addstr(7, 0, 'player')

def test_display_busted():
    stdscr = Stdscr()
    display = Display(stdscr)
    h = Hand('player')
    h.cards = [Card('10','S'), Card('10','C'), Card('2','S')]
    display.display_busted(h)
    assert stdscr.action[0] == Addstr(7 + 2, 0, 'Busted')

def test_display_blackjack():
    stdscr = Stdscr()
    display = Display(stdscr)
    h = Hand('player')
    h.cards = [Card('10','S'), Card('A','C')]
    display.display_blackjack(h)
    assert stdscr.action[0] == Addstr(7 + 4, 0, 'Black')
    assert stdscr.action[1] == Addstr(7 + 5, 0, 'jack!')

def test_display_decide():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.display_decide('player', 'player', 1)
    assert stdscr.action[0] == Addstr(36, 18, 'result for player')
    assert stdscr.action[1] == Addstr(37,18, 'player won!')

    stdscr = Stdscr()
    display = Display(stdscr)
    display.display_decide('player', 'player BJ', 1)
    assert stdscr.action[0] == Addstr(36, 18, 'result for player')
    assert stdscr.action[1] == Addstr(37,18, 'player won w/ BJ!')

def test_display_unknown_input():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.display_unknown_input()
    assert stdscr.action[0] == Addstr(34, 0, 'invalid input')
    assert stdscr.action[1] == 'refresh'
    assert stdscr.action[2] == Addstr(34, 0, '             ')
    assert stdscr.action[3] == 'refresh'

def test_clear():
    stdscr = Stdscr()
    display = Display(stdscr)
    display.clear()
    assert stdscr.action[0] == 'clear'
    assert stdscr.action[1] == 'refresh'

def test_display():
    stdscr = Stdscr()
    display = Display(stdscr)
    game = Game()
    h = Hand('player', 100)
    h.cards = [Card('A', 'S'), Card('10', 'S')]
    game.all_hands.append(h)
    game.current_hand = h
    game.running_count = 1
    game.setup_deck()
    display.display(game)
    
    assert stdscr.action[0] == Addstr(0 + 3, 0, '      ')
    assert stdscr.action[1] == Addstr(7 + 3, 0, '      ')
    assert stdscr.action[2] == Addstr(14 + 3, 0, '      ')
    assert stdscr.action[3] == Addstr(21 + 3, 0, '      ')
    assert stdscr.action[4] == Addstr(28 + 3, 0, '      ')
    assert stdscr.action[5] == Addstr(7 + 3, 0, '----->')
    
    assert stdscr.action[6] == Addstr(38, 0, f'Your current bankroll is: 10000')
    
    assert stdscr.action[7] == Addstr(40, 0, f'The running count is 1 and the True count is {"%.2f" % round(game.running_count / len(game.shoe.cards), 2)}')
    
    assert stdscr.action[8] == Addstr(7, 0, 'player')

    assert stdscr.action[9] == Addstr(7 + 4, 0, 'Black')
    assert stdscr.action[10] == Addstr(7 + 5, 0, 'jack!')

    assert stdscr.action[11] == Addstr(8, 0, str(100))

    assert stdscr.action[12] == Addstr(13, 0, str(21))

    for x in range(6):
        assert stdscr.action[x * 2 + 13] == Addstr(7, 7 + x, '#')
        assert stdscr.action[x * 2 + 14] == Addstr(7 + 6, 7 + x, '#')
    for b in range(7):
        assert stdscr.action[b * 2 + 25] == Addstr(7 + b, 7, '#')
        assert stdscr.action[b * 2 + 26] == Addstr(7 + b, 7 + 6, '#')
    assert stdscr.action[39] == Addstr(7 + 1, 7 + 1, 'A')
    assert stdscr.action[40] == Addstr(7 + 1, 7 + 1 + len(str('A')), '\u2660')
    assert stdscr.action[41] == Addstr(7 + 5, 7 + 5 - len(str('A')), 'A')
    assert stdscr.action[42] == Addstr(7 + 5, 7 + 5, '\u2660')
    for a in range(6):
        assert stdscr.action[a * 2 + 43] == Addstr(7, 14 + a, ' ')
        assert stdscr.action[a * 2 + 44] == Addstr(7 + 6, 14 + a, ' ')
    for b in range(7):
        assert stdscr.action[b * 2 + 12 + 43] == Addstr(7 + b, 14, ' ')
        assert stdscr.action[b * 2 + 12 + 44] == Addstr(7 + b, 14 + 6, ' ')
    assert stdscr.action[69] == Addstr(7 + 1, 14 + 1, '  ')
    assert stdscr.action[70] == Addstr(7 + 5, 14 + 4, '   ')
    
    for x in range(6):
        assert stdscr.action[x * 2 + 71] == Addstr(7, 14 + x, '#')
        assert stdscr.action[x * 2 + 72] == Addstr(7 + 6, 14 + x, '#')
    for b in range(7):
        assert stdscr.action[b * 2 + 12 + 71] == Addstr(7 + b, 14, '#')
        assert stdscr.action[b * 2 + 12 + 72] == Addstr(7 + b, 14 + 6, '#')
    assert stdscr.action[97] == Addstr(7 + 1, 14 + 1, '10')
    assert stdscr.action[98] == Addstr(7 + 1, 14 + 1 + len(str('10')), '\u2660')
    assert stdscr.action[99] == Addstr(7 + 5, 14 + 5 - len(str('10')), '10')
    assert stdscr.action[100] == Addstr(7 + 5, 14 + 5, '\u2660')
    for a in range(6):
        assert stdscr.action[a * 2 + 101] == Addstr(7, 21 + a, ' ')
        assert stdscr.action[a * 2 + 102] == Addstr(7 + 6, 21 + a, ' ')
    for b in range(7):
        assert stdscr.action[b * 2 + 12 + 101] == Addstr(7 + b, 21, ' ')
        assert stdscr.action[b * 2 + 12 + 102] == Addstr(7 + b, 21 + 6, ' ')
    assert stdscr.action[127] == Addstr(7 + 1, 21 + 1, '  ')
    assert stdscr.action[128] == Addstr(7 + 5, 21 + 4, '   ')
    assert stdscr.action[129] == 'refresh'