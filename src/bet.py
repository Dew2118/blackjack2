class Bet:
    def __init__(self, starting_bankroll) -> None:
        self.current_bankroll = starting_bankroll
    
    def bet(self, amount):
        self.current_bankroll -= amount
        return amount

    def win(self, amount):
        self.current_bankroll += (amount * 2)

    def blackjack(self, amount):
        self.current_bankroll += (amount * (3 / 2))