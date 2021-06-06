from src.custom_exception import BetError

class Bet:
    def __init__(self, starting_bankroll) -> None:
        self.current_bankroll = starting_bankroll
    
    def bet(self, amount):
        if self.current_bankroll <= 0:
            raise BetError('Bankrupted, consider starting a new game')
        if amount > self.current_bankroll:
            raise BetError('Too much bet')
        self.current_bankroll -= amount
        return amount

    def win(self, amount):
        self.current_bankroll += (amount * 2)

    def blackjack(self, amount):
        self.current_bankroll += (amount * (3 / 2))