class Hand:
    def __init__(self) -> None:
        self.cards = []

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
            decision = self.game.strategy.get_decision()
            if decision == 'h':
                self.draw(1)
            elif decision == 's':
                break
            elif decision == 'd':
                self.draw(1)
                break
            elif decision == 'sp':
                self.split()

    def split(self):
        pass

    

    


