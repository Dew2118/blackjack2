#DONE: Try using git branch to test whether we can remove class player
# But use only hand
# So in hand class, we must keep player name
# And also keep status whether this hand belongs to dealer or not
# To make it easier to code, we may set default value of this flag as False
# because most of the time, we'll create normal player
# if it's the same player name, it means that this hand belongs to the same player
# and we also keep track of player's name in game, so we can loop either by player or by hand.

#DONE: May consider adding a method for returning only exposed cards.
# So we can use it for any strategies.
# Normally, all hands will return all cards in hands as exposed cards
# except dealer that will have one card unexposed.

class Hand:
    """Represent a hand of a player"""
    def __init__(self, name, bet_amount = 0) -> None:
        # Keep cards in hand
        self.cards = []
        # Name of this hand
        self.name = name
        self.bet_amount = bet_amount

    def draw(self, game, no_of_cards):
        """draw cards as many as specified in no_of_cards from shoe"""
        for _ in range(no_of_cards):
            # DONE: make shoe keep track of drawn card
            # So if needed, we can go through the list of drawn card
            # and calculate running_count if we want
            c = game.shoe.deal()
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
        # Done: test whether if we change condition to check score = 21
        # It is still correct.
        return (self.get_score() == 21) and (len(self.cards) == 2)

    # Papa's version to consider
    def play(self, game):
        # If this hand is already blackjack, do nothing
        if self.is_blackjack():
            return

        stop_drawing = False
        while not stop_drawing and not self.is_busted():
            game.update_running_count()
            # update display
            game.display()
            decision = game.strategist.make_decision(game)
            if decision == 'h': # hit a card
                self.draw(game, 1)
            elif decision == 's': # stand
                stop_drawing = True
            elif decision == 'd': # double the bet and draw 1 card
            # DONE: need to add double the bet and make test to make sure that it's correct
                self.draw(game, 1)
                game.bet.bet(self.bet_amount)
                self.bet_amount *= 2
                stop_drawing = True
            elif decision == 'sp': # split
                self.split(game)
            else:
                # DONE: Display that it is unknown decision
                game.display_unknown_input()

    def is_splittable(self):
        return (len(self.cards) == 2) and (self.cards[0].value == self.cards[1].value)

    def split(self, game):
        if self.is_splittable() is False:
            return 'rt'
        First_card, Second_card = self.cards.copy()
        new_hand = Hand(f'split_{game.split_counter}')
        game.split_counter += 1
        new_hand.cards = [Second_card]
        self.cards = [First_card]
        game.hand_stack.append(new_hand)
        game.bet.bet(self.bet_amount)
        new_hand.bet_amount = self.bet_amount
        game.all_hand.append(new_hand)