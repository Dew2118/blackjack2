class Hand:
    def __init__(self, name) -> None:
        self.cards = []
        self.name = name

    def draw(self, game, num_of_card):
        for _ in range(num_of_card):
            c = game.shoe.deal()
            if c.score <= 6:
                game.running_count += 1
            if c.score >= 10:
                game.running_count += -1
            self.cards.append(c)



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
        score = [c.score for c in self.cards]
        return (sorted(score) == [10,11]) and (len(self.cards == 2))

    def play(self, game):
        while not self.is_blackjack() and not self.is_busted():
            game.display()
            ace = False
            for card in self.cards:
                if card.score == 11:
                    ace = True
            # decision = game.strategist.get_decision()
            # decision = game.strategist.get_curses_decision()
            if self.name != 'dealer':
                decision = game.strategist.basic_strategy(self.get_score(), game.all_hand[0].cards[0].score, ace, self.is_splittable())
            else:
                decision = game.strategist.get_curses_decision()
            if decision == 'h':
                self.draw(game, 1)
            elif decision == 's':
                break
            elif decision == 'd':
                self.draw(game, 1)
                break
            elif decision == 'sp':
                self.split(game)
                game.display()
        game.display()


    def is_splittable(self):
        return (len(self.cards) == 2) and (self.cards[0].value == self.cards[1].value)

    def split(self, game):
        if self.is_splittable() is False:
            return
        First_card, Second_card = self.cards.copy()
        new_hand = Hand(f'split_{game.split_counter}')
        game.split_counter += 1
        new_hand.cards = [Second_card]
        self.cards = [First_card]
        game.hand_stack.append(new_hand)
        game.all_hand.append(new_hand)