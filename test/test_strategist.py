from blackjack2.src.strategist import Strategist

# basic strtegy test
def test_norm():
    strategist = Strategist('game')
    for i in [17,18,19,20,21]:
        for num in [1,2,3,4,5,6,7,8,9,10,11]:
            assert strategist.basic_strategy(i, num) == 's'
    for i in [13, 14, 15, 16]:
        for num in [2,3,4,5,6]:
            assert strategist.basic_strategy(i, num) == 's'
        for num in [7,8,9,10,11]:
            assert strategist.basic_strategy(i, num) == 'h'
    for num in [2,3,7,8,9,10,11]:
        assert strategist.basic_strategy(12, num) == 'h'
    for num in [4,5,6]:
        assert strategist.basic_strategy(12, num) == 's'
    for num in [1,2,3,4,5,6,7,8,9,10,11]:
        assert strategist.basic_strategy(11, num) == 'd'
    for num in [2,3,4,5,6,7,8,9]:
        assert strategist.basic_strategy(10, num) == 'd'
    for num in [10, 11]:
        assert strategist.basic_strategy(10, num) == 'h'
    for num in [2,7,8,9,10,11]:
        assert strategist.basic_strategy(9, num) == 'h'
    for num in [3,4,5,6]:
        assert strategist.basic_strategy(9, num) == 'd'
    for i in [2,3,4,5,6,7,8]:
        for num in [1,2,3,4,5,6,7,8,9,10,11]:
            assert strategist.basic_strategy(i, num) == 'h'

def test_ace():
    strategist = Strategist('game')
    for up_card in [2,3,4,5,6,7,8,9,10,11]:
        assert strategist.basic_strategy(20, up_card, ace = True) == 's'
    for up_card in [2,3,4,5,7,8,9,10,11]:
        assert strategist.basic_strategy(19, up_card, ace = True) == 's'
    assert strategist.basic_strategy(19, 6, ace = True) == 'd'    
    for up_card in [2,3,4,5,6]:
        assert strategist.basic_strategy(18, up_card, ace = True) == 'd'
    for up_card in [7,8]:
        assert strategist.basic_strategy(18, up_card, ace = True) == 's'
    for up_card in [9,10,11]:
        assert strategist.basic_strategy(18, up_card, ace = True) == 'h'
    for up_card in [2,7,8,9,10,11]:
        assert strategist.basic_strategy(17, up_card, ace = True) == 'h'
    for up_card in [3,4,5,6]:
        assert strategist.basic_strategy(17, up_card, ace = True) == 'd'
    for sum in [15,16]:
        for up_card in [2,3,7,8,9,10,11]:
            assert strategist.basic_strategy(sum, up_card, ace = True) == 'h'
        for up_card in [4,5,6]:
            assert strategist.basic_strategy(sum, up_card, ace = True) == 'd'
    for sum in [13,14]:
        for up_card in [2,3,4,7,8,9,10,11]:
            assert strategist.basic_strategy(sum, up_card, ace = True) == 'h'
        for up_card in [5,6]:
            assert strategist.basic_strategy(sum, up_card, ace = True) == 'd'

def test_split():
    strategist = Strategist('game')
    for sum in [12,16]:
        for dealer_up_card in [2,3,4,5,6,7,8,9,10,11]:
            assert strategist.basic_strategy(sum, dealer_up_card, splittable = True, ace = True) == 'sp'
    for dealer_up_card in [2,3,4,5,6,7,8,9,10, 11]:
        assert strategist.basic_strategy(20, dealer_up_card, splittable = True) == 's'
    for dealer_up_card in [2,3,4,5,6,8,9]:
        assert strategist.basic_strategy(18, dealer_up_card, splittable = True) == 'sp'
    for dealer_up_card in [7,10,11]:
        assert strategist.basic_strategy(18, dealer_up_card, splittable = True) == 's'
    for dealer_up_card in [2,3,4,5,6,7]:
        assert strategist.basic_strategy(14, dealer_up_card, splittable = True) == 'sp'
    for dealer_up_card in [8,9,10,11]:
        assert strategist.basic_strategy(14, dealer_up_card, splittable = True) == 'h'
    for dealer_up_card in [2,3,4,5,6]:
        assert strategist.basic_strategy(12, dealer_up_card, splittable = True) == 'sp'
    for dealer_up_card in [7,8,9,10,11]:
        assert strategist.basic_strategy(12, dealer_up_card, splittable = True) == 'h'
    for num in [2,3,4,5,6,7,8,9]:
        assert strategist.basic_strategy(10, num, splittable = True) == 'd'
    for num in [10, 11]:
        assert strategist.basic_strategy(10, num, splittable = True) == 'h'
    for num in [1,2,3,4,5,6,7,8,9,10,11]:
        assert strategist.basic_strategy(8, num, splittable = True) == 'h'
    for num in [4,6]:
        for dealer_up_card in [4,5,6,7]:
            assert strategist.basic_strategy(num, dealer_up_card, splittable = True) == 'sp'
        for dealer_up_card in [2,3,8,9,10,11]:
            assert strategist.basic_strategy(num, dealer_up_card, splittable = True) == 'h'