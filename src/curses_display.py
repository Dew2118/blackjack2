import curses
from time import sleep

class Display:
    SUIT_CHR = {'S': '\u2660', 'H': '\u2665', 'D': '\u2666', 'C': '\u2663'}
    y_dict = {'dealer':0,'player':7,'split_1':14,'split_2':21,'split_3':28}
    def __init__(self, game) -> None:
        self.game = game
        self.stdscr = curses.initscr()

    def display(self):
        self.display_arrow()
        self.display_busted()
        self.display_blackjack()
        for hand in self.game.all_hand:
            self.display_name(hand)
            y = self.y_dict[hand.name]
            x = 7
            symbol = '#'
            for c in hand.cards:
                self.display_card(x, y, c, hand, symbol)
                x += 7
        self.stdscr.refresh()

    def display_card(self, x, y, c, hand, symbol):
        value = c.value
        suit = c.suit
        for a in range(6):
            self.stdscr.addstr(y, x + a, symbol)
            self.stdscr.addstr(y + 6, x + a, symbol)
        for b in range(7):
            self.stdscr.addstr(y + b, x, symbol)
            self.stdscr.addstr(y + b, x + 6, symbol)
        if not (hand.name == 'dealer' and c == hand.cards[1] and self.game.current_hand.name != 'dealer'):
            self.stdscr.addstr(y + 1, x + 1, value)
            self.stdscr.addstr(y + 1, x + 1 + len(str(value)), self.SUIT_CHR[suit])
            self.stdscr.addstr(y + 5, x + 5 - len(str(value)), value)
            self.stdscr.addstr(y + 5, x + 5, self.SUIT_CHR[suit])

    def display_arrow(self):
        self.stdscr.addstr(self.y_dict[self.game.current_hand.name] + 3, 0, '----->')

    def display_name(self, hand):
        self.stdscr.addstr(self.y_dict[hand.name], 0, hand.name)

    def display_busted(self):
        if self.game.current_hand.is_busted() == True:
            self.stdscr.addstr(self.y_dict[self.game.current_hand.name] + 2, 0, 'Busted')

    def display_blackjack(self):
        if self.game.current_hand.is_blackjack() == True:
            self.stdscr.addstr(self.y_dict[self.game.current_hand.name] + 4, 0, 'Black')
            self.stdscr.addstr(self.y_dict[self.game.current_hand.name] + 5, 0, 'jack!')

    def get_input(self):
        self.stdscr.addstr(35, 0, 'Your decision is: ')
        self.stdscr.refresh()
        return self.stdscr.getstr(35, len('Your decision is: ')).decode('utf-8')

    def display_decide(self, hand_name, text, counter):
        self.stdscr.addstr(36, counter * 18, f'result for {hand_name}')
        self.stdscr.addstr(37, counter * 18, text)
        self.stdscr.refresh()
        sleep(2)
        curses.endwin()
                
