class Basic_strategy:
    def norm(self, sum, dealer_up_card):
        if sum >= 17:
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

    def ace(self, sum, dealer_up_card, deviation = None):
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
        return deviation.norm(sum + 11, dealer_up_card)
        

    def split(self, sum, dealer_up_card, ace = False):
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