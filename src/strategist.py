class Strategist:
    def __init__(self, game) -> None:
        self.game = game

    def get_decision(self):
        return input('Your decision is: ')
    
    def get_curses_decision(self):
        return self.game.get_input()

    def basic_strategy(self, sum, dealer_up_card, ace = False, splittable = False):
        if splittable == True:
            return self.split(sum, dealer_up_card, ace)
        elif ace  == True:
            return self.ace(sum, dealer_up_card)
        return self.norm(sum, dealer_up_card)

    def norm(self, sum, dealer_up_card):
        if sum in [17,18,19,20,21]:
            return 's'
        if sum in [13, 14, 15, 16]:
            if dealer_up_card in [2,3,4,5,6]:
                return 's'
            for dealer_up_card in [7,8,9,10,11]:
                return 'h'
        if sum == 12:
            if dealer_up_card in [2,3,7,8,9,10,11]:
                return 'h'
            if dealer_up_card in [4,5,6]:
                return 's'
        if sum == 11:
            return 'd'
        if sum == 10:
            if dealer_up_card in [2,3,4,5,6,7,8,9]:
                return 'd'
            if dealer_up_card in [10, 11]:
                return 'h'
        if sum == 9:
            if dealer_up_card in [2,7,8,9,10,11]:
                return 'h'
            if dealer_up_card in [3,4,5,6]:
                return 'd'
        if sum in [2,3,4,5,6,7,8]:
            return 'h'

    def ace(self, sum, dealer_up_card):
        if (sum - 11) > 9:
            return self.norm(sum, dealer_up_card)
        else:
            sum -= 11
        if sum == 9:
            return 's'
        if sum == 8:
            if dealer_up_card == 6:
                return 'd'
            if dealer_up_card in [2,3,4,5,7,8,9,10,11]:
                return 's'
        if sum == 7:
            if dealer_up_card in [2,3,4,5,6]:
                return 'd'
            if dealer_up_card in [7,8]:
                return 's'
            if dealer_up_card in [9,10,11]:
                return 'h'
        if sum == 6:
            if dealer_up_card in [2,7,8,9,10,11]:
                return 'h'
            if dealer_up_card in [3,4,5,6]:
                return 'd'
        if sum in [4,5]:
            if dealer_up_card in [2,3,7,8,9,10,11]:
                return 'h'
            if dealer_up_card in [4,5,6]:
                return 'd'
        if sum in [2,3]:
            if dealer_up_card in [2,3,4,7,8,9,10,11]:
                return 'h'
            if dealer_up_card in [5,6]:
                return 'd'

    def split(self, sum, dealer_up_card, ace):
        if sum == 16 or ace == True:
            return 'sp'
        if sum == 20:
            return 's'
        if sum == 18:
            if dealer_up_card in [2,3,4,5,6,8,9]:
                return 'sp'
            if dealer_up_card in [7,10,11]:
                return 's'
        if sum == 14:
            if dealer_up_card in [2,3,4,5,6,7]:
                return 'sp'
            if dealer_up_card in [8,9,10,11]:
                return 'h'
        if sum == 12:
            if dealer_up_card in [2,3,4,5,6]:
                return 'sp'
            if dealer_up_card in [7,8,9,10,11]:
                return 'h'
        if sum == 10:
            if dealer_up_card in [2,3,4,5,6,7,8,9]:
                return 'd'
            if dealer_up_card in [10, 11]:
                return 'h'
        if sum == 8:
            return 'h'
        if sum in [4,6]:
            if dealer_up_card in [4,5,6,7]:
                return 'sp'
            if dealer_up_card in [2,3,8,9,10,11]:
                return 'h'
