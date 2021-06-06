from time import sleep
import sys
import curses
from dataclasses import dataclass

@dataclass
class Addstr:
    y : int
    x : int
    text : str


class Display:
    SUIT_CHR = {'S': '\u2660', 'H': '\u2665', 'D': '\u2666', 'C': '\u2663'}
    y_dict = {'dealer':0,'player':7,'split_1':14,'split_2':21,'split_3':28}
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.game = None
        self.action = []

    def display(self, game):
        self.game = game
        self.display_arrow()
        self.display_bankroll()
        self.action.append(Addstr(40, 0, f'The running count is {game.running_count} and the True count is {"%.2f" % round(game.running_count / len(game.shoe.cards), 2)}'))
        for hand in self.game.all_hands:
            self.display_name(hand)
            y = self.y_dict[hand.name]
            x = 7
            self.display_busted(hand)
            self.display_blackjack(hand)
            self.display_bet(hand, y)
            self.display_score(hand, y)
            for c in hand.cards:
                value = c.value
                suit = c.suit
                self.display_card(x, y, '#')
                if not (hand.name == 'dealer' and c == hand.cards[1] and self.game.current_hand.name != 'dealer'):
                    self.display_card_symbol(x, y, value, suit)
                x += 7
                self.display_card(x, y, ' ')
                self.action.append(Addstr(y + 1, x + 1, '  '))
                self.action.append(Addstr(y + 5, x + 4, '   '))
        self.action.append('refresh')

    def display_bankroll(self):
        self.action.append(Addstr(38, 0, f'Your current bankroll is: {self.game.bet.current_bankroll}'))

    def display_bet(self, hand, y):
        self.action.append(Addstr(y + 1, 0, str(hand.bet_amount)))

    def display_score(self, hand, y):
        neg = 0
        if (hand.name == 'dealer' and self.game.current_hand.name != 'dealer'):
            neg = hand.cards[1].score
        self.action.append(Addstr(y + 6, 0, str(hand.get_score() - neg)))

    def display_card(self, x, y, symbol):
        for a in range(6):
            self.action.append(Addstr(y, x + a, symbol))
            self.action.append(Addstr(y + 6, x + a, symbol))
        for b in range(7):
            self.action.append(Addstr(y + b, x, symbol))
            self.action.append(Addstr(y + b, x + 6, symbol))
        
    def display_card_symbol(self, x, y, value, suit):
        self.action.append(Addstr(y + 1, x + 1, value))
        self.action.append(Addstr(y + 1, x + 1 + len(str(value)), self.SUIT_CHR[suit]))
        self.action.append(Addstr(y + 5, x + 5 - len(str(value)), value))
        self.action.append(Addstr(y + 5, x + 5, self.SUIT_CHR[suit]))

    def display_arrow(self):
        #remove current arrow
        self.action.append(Addstr(0 + 3, 0, '      '))
        self.action.append(Addstr(7 + 3, 0, '      '))
        self.action.append(Addstr(14 + 3, 0, '      '))
        self.action.append(Addstr(21 + 3, 0, '      '))
        self.action.append(Addstr(28 + 3, 0, '      '))
        #create arrow
        self.action.append(Addstr(self.y_dict[self.game.current_hand.name] + 3, 0, '----->'))

    def display_name(self, hand):
        self.action.append(Addstr(self.y_dict[hand.name], 0, hand.name))

    def display_busted(self, hand):
        if hand.is_busted() == True:
            self.action.append(Addstr(self.y_dict[hand.name] + 2, 0, 'Busted'))

    def display_blackjack(self, hand):
        if hand.is_blackjack() == True:
            self.action.append(Addstr(self.y_dict[hand.name] + 4, 0, 'Black'))
            self.action.append(Addstr(self.y_dict[hand.name] + 5, 0, 'jack!'))

    def get_input(self):
        self.action.append(Addstr(35, 0, '                            '))
        self.action.append(Addstr(35, 0, 'Your decision is: '))
        self.action.append('refresh')
        self.execute()
        return self.stdscr.getstr(35, len('Your decision is: ')).decode('utf-8')

    def get_bet_amount(self):
        self.action.append(Addstr(35, 0, 'Your betting amount is: '))
        self.action.append('refresh')
        self.execute()
        a = ''
        while not a.isnumeric():
            a = self.stdscr.getstr(35, len('Your betting amount is: ')).decode('utf-8')
        return a

    def display_decide(self, hand_name, text, counter):
        self.action.append(Addstr(36, counter * 18, f'result for {hand_name}'))
        if text[-1] == 'J':
            self.action.append(Addstr(37, counter * 18, f'{text[:-3]} won w/ BJ!'))
        elif text in ['dealer', 'player', 'split_1', 'split_2', 'split_3']:
            self.action.append(Addstr(37, counter * 18, f'{text} won!'))
        else:
            self.action.append(Addstr(37, counter * 18, text))
        self.action.append('refresh')

    def display_unknown_input(self):
        self.action.append(Addstr(34, 0, 'invalid input'))
        self.action.append('refresh')
        if not "pytest" in sys.modules:
            sleep(2)
        self.action.append(Addstr(34, 0, '             '))
        self.action.append('refresh')

    def clear(self):
        if not "pytest" in sys.modules:
            sleep(4)
        self.action.append('clear')
        self.action.append('refresh')

    def execute(self):
        for action in self.action:
            if type(action) == Addstr:
                self.stdscr.addstr(action.y, action.x, action.text)
            if action == 'refresh':
                self.stdscr.refresh()
            if action == 'clear':
                self.stdscr.clear()
        self.action = []

if not "pytest" in sys.modules:
    display = curses.wrapper(Display)