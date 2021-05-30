from blackjack2.src.bet import Bet

def test_bet_init():
    assert Bet(10000) is not None

def test_bet():
    bet = Bet(10000)
    bet.bet(1000)
    assert bet.current_bankroll == 9000

def test_win():
    bet = Bet(10000)
    bet.bet(1000)
    bet.win(1000)
    assert bet.current_bankroll == 11000

def test_blackjack():
    bet = Bet(10000)
    bet.bet(1000)
    bet.blackjack(1000)
    assert bet.current_bankroll == 10500.0