class Hand:
    def __init__(self, name) -> None:
        self.cards = []
        self.name = name

    def draw(self, shoe, num_of_card):
        for _ in range(num_of_card):
            self.cards.append(shoe.deal())


    def is_busted(self):
        return (self.get_score() > 21)

    def get_score(self):
        score = 0
        for c in self.cards:
            score += c.score
        for c in self.cards:
            if score > 21 and c.value == 'A':
                score -= 10
        return score

    def is_blackjack(self):
        value = [c.value for c in self.cards]
        return (sorted(value) == [10,11])

    def play(self, game):
        while not self.is_blackjack() and not self.is_busted():
            game.display.display()
            decision = game.strategist.get_decision()
            if decision == 'h':
                self.draw(game.shoe, 1)
            elif decision == 's':
                break
            elif decision == 'd':
                self.draw(game.shoe, 1)
                break
            elif decision == 'sp':
                self.split(game)
        game.display.display()


    def is_splittable(self):
        return (len(self.cards) == 2) and (self.cards[0].value == self.cards[1].value)

    def split(self, game):
        if self.is_splittable() is False:
            return
        First_card, Second_card = self.cards.copy()
        new_hand = Hand('split_1')
        new_hand.cards = [Second_card]
        self.cards = [First_card]
        game.hand_stack.append(new_hand)
        game.all_hand.append(new_hand)