#TODO: Try using git branch to test whether we can remove class player
# But use only hand
# So in hand class, we must keep player name
# And also keep status whether this hand belongs to dealer or not
# To make it easier to code, we may set default value of this flag as False
# because most of the time, we'll create normal player
# if it's the same player name, it means that this hand belongs to the same player
# and we also keep track of player's name in game, so we can loop either by player or by hand.

#TODO: May consider adding a method for returning only exposed cards.
# So we can use it for any strategies.
# Normally, all hands will return all cards in hands as exposed cards
# except dealer that will have one card unexposed.

class Hand:
    """Represent a hand of a player"""
    def __init__(self, name) -> None:
        # Keep cards in hand
        self.cards = []
        # Name of this hand
        self.name = name

    def draw(self, game, no_of_cards):
        """draw cards as many as specified in no_of_cards from shoe"""
        for _ in range(no_of_cards):
            # TODO: make shoe keep track of drawn card
            # So if needed, we can go through the list of drawn card
            # and calculate running_count if we want
            c = game.shoe.deal()
            if c.score <= 6:
                game.running_count += 1
            if c.score >= 10:
                game.running_count += -1
            self.cards.append(c)

    def is_busted(self):
        return (self.get_score() > 21)

    def get_score(self):
        """Return score of this hand"""
        score = sum([c.score for c in self.cards])
        # deal with ACE card that can have 2 values of 1 or 11
        for c in self.cards:
            if score > 21 and c.value == 'A':
                score -= 10
        return score

    def is_blackjack(self):
        score = [c.score for c in self.cards]
        # TODO: test whether if we change condition to check score = 21
        # It is still correct.
        return (sorted(score) == [10,11]) and (len(self.cards == 2))

    # Papa's version to consider
    def play1(self, game):
        # If this hand is already blackjack, do nothing
        if self.is_blackjack():
            return

        stop_drawing = False
        while not stop_drawing:
            decision = game.strategist.make_decision(game)

            if decision == 'h': # hit a card
                self.draw(game, 1)
            elif decision == 's': # stand
                stop_drawing = True
            elif decision == 'd': # double the bet and draw 1 card
            # TODO: need to add double the bet and make test to make sure that it's correct
                self.draw(game, 1)
                stop_drawing = True
            elif decision == 'sp': # split
                self.split(game)
            else:
                # TODO: Display that it is unknown decision
                pass
            # update display
            game.display()

    def play(self, game):
        while not self.is_blackjack() and not self.is_busted():
            game.display()
            ace = False
            for card in self.cards:
                if card.score == 11:
                    ace = True
            # decision = game.strategist.get_decision()
            # decision = game.strategist.get_curses_decision()

            # TODO: 1. can we make the calling to strategist the same way (same parameter list)
            # 2. can we move the decision whether receiving manual input or autocalculate into strategist
            if self.name != 'dealer':
                decision = game.strategist.basic_strategy(self.get_score(), game.all_hand[0].cards[0].score, ace, self.is_splittable())
            else:
                decision = game.strategist.get_curses_decision()

            if decision == 'h': # hit a card
                self.draw(game, 1)
            elif decision == 's': # stand
                break
            elif decision == 'd': # double the bet and draw 1 card
            # TODO: need to add double the bet and make test to make sure that it's correct
                self.draw(game, 1)
                break
            elif decision == 'sp': # split
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