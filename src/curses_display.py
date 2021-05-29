import curses
from time import sleep

class Display:
    SUIT_CHR = {'S': '\u2660', 'H': '\u2665', 'D': '\u2666', 'C': '\u2663'}
    y_dict = {'dealer':0,'player':7,'split_1':14,'split_2':21,'split_3':28}
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.game = None

    def display(self, game):
        self.game = game
        self.display_arrow()
        self.display_busted()
        self.display_blackjack()
        self.stdscr.addstr(40, 0, f'The running count is {game.running_count} and the True count is {"%.2f" % round(game.running_count / len(game.shoe.cards), 2)}')
        for hand in self.game.all_hand:
            self.display_name(hand)
            y = self.y_dict[hand.name]
            x = 7
            self.display_score(hand, y)
            for c in hand.cards:
                value = c.value
                suit = c.suit
                self.display_card(x, y, '#')
                if not (hand.name == 'dealer' and c == hand.cards[1] and self.game.current_hand.name != 'dealer'):
                    self.display_card_symbol(x, y, value, suit)
                x += 7
                self.display_card(x, y, ' ')
                self.stdscr.addstr(y + 1, x + 1, '  ')
                self.stdscr.addstr(y + 5, x + 4, '   ')
        self.stdscr.refresh()

    def display_score(self, hand, y):
        neg = 0
        if (hand.name == 'dealer' and self.game.current_hand.name != 'dealer'):
            neg = hand.cards[1].score
        self.stdscr.addstr(y + 5, 0, str(hand.get_score() - neg))
        self.stdscr.refresh()

    def display_card(self, x, y, symbol):
        for a in range(6):
            self.stdscr.addstr(y, x + a, symbol)
            self.stdscr.addstr(y + 6, x + a, symbol)
        for b in range(7):
            self.stdscr.addstr(y + b, x, symbol)
            self.stdscr.addstr(y + b, x + 6, symbol)
        
    def display_card_symbol(self, x, y, value, suit):
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

display = curses.wrapper(Display)
