from blackjack2.src.basic_strategy import Basic_strategy

class Deviation(Basic_strategy):
    # parameter running_count and true_count are for testing purposes
    def __init__(self, game = None, running_count = 0, true_count = 0) -> None:
        super().__init__()
        if __name__ == '__main__':
            self.true_count = "%.2f" % round(game.running_count / len(game.shoe.cards), 2)
            self.running_count = game.running_count
        else:
            #Also for testing purposes
            self.true_count = true_count
            self.running_count = running_count

    def main(self, sum, dealer_up_card, ace = False, splittable = False):
        if splittable == True:
            return self.split(sum, dealer_up_card, ace)
        elif ace == True:
            return self.ace(sum, dealer_up_card)
        return self.norm(sum, dealer_up_card)

    def norm(self, sum, dealer_up_card):
        if sum == 16:
            if dealer_up_card == 9:
                if self.true_count >= 4:
                    return 's'
                return 'h'
            elif dealer_up_card == 10:
                if self.running_count > 0:
                    return 's'
                return 'h'
        if sum == 15 and dealer_up_card == 10:
            if self.true_count >= 4:
                return 's'
            return 'h'
        if sum == 13 and dealer_up_card == 2:
            if self.true_count <= 1:
                return 'd'
            return 's'
        if sum == 12:
            if dealer_up_card == 2:
                if self.true_count >= 3:
                    return 's'
                return 'h'
            if dealer_up_card == 3:
                if self.true_count >= 2:
                    return 's'
                return 'h'
            if dealer_up_card == 4:
                if self.running_count < 0:
                    return 'd'
                return 's'
        if sum == 10:
            if dealer_up_card == 10:
                if self.true_count >= 4:
                    return 'd'
                return 'h'
            if dealer_up_card == 11:
                if self.true_count >= 3:
                    return 'd'
                return 'h'
        if sum == 9:
            if dealer_up_card == 2:
                if self.true_count >= 1:
                    return 'd'
                return 'h'
            elif dealer_up_card == 7:
                if self.true_count >= 3:
                    return 'd'
                return 'h'
        if sum == 8 and dealer_up_card == 6:
            if self.true_count >= 2:
                #test
                return 'd'
            return 'h'
        return Basic_strategy().norm(sum, dealer_up_card)

    def ace(self, sum, dealer_up_card):
        #test
        if (sum - 11) > 9:
            return self.norm(sum, dealer_up_card)
        else:
            sum -= 11
        if sum == 8:
            if dealer_up_card == 4:
                if self.true_count >= 3:
                    return 'd'
                return 's'
            if dealer_up_card == 5:
                if self.true_count >= 1:
                    return 'd'
                return 's'
            if dealer_up_card == 6:
                if self.running_count < 0:
                    return 's'
                return 'd'
        if sum == 6 and dealer_up_card == 2:
            #test
            if self.true_count >= 1:
                return 'd'
            return 'h'
        return Basic_strategy().ace(sum, dealer_up_card)
    
    def split(self, sum, dealer_up_card, ace = False):
        if sum == 20:
            if dealer_up_card == 4:
                if self.true_count >= 6:
                    return 'sp'
                return 's'
            if dealer_up_card == 5:
                if self.true_count >= 5:
                    return 'sp'
                return 's'
            # test
            if dealer_up_card == 6:
                if self.true_count >= 4:
                    return 'sp'
                return 's'
        return Basic_strategy().split(sum, dealer_up_card, ace)