from src.basic_strategy import Basic_strategy
from src.deviation import Deviation

# basic strtegy test
def test_norm():
    basic_strategy = Basic_strategy()
    for i in [17,18,19,20,21]:
        for num in [1,2,3,4,5,6,7,8,9,10,11]:
            assert basic_strategy.norm(i, num) == 's'
    for i in [13, 14, 15, 16]:
        for num in [2,3,4,5,6]:
            assert basic_strategy.norm(i, num) == 's'
        for num in [7,8,9,10,11]:
            assert basic_strategy.norm(i, num) == 'h'
    for num in [2,3,7,8,9,10,11]:
        assert basic_strategy.norm(12, num) == 'h'
    for num in [4,5,6]:
        assert basic_strategy.norm(12, num) == 's'
    for num in [1,2,3,4,5,6,7,8,9,10,11]:
        assert basic_strategy.norm(11, num) == 'd'
    for num in [2,3,4,5,6,7,8,9]:
        assert basic_strategy.norm(10, num) == 'd'
    for num in [10, 11]:
        assert basic_strategy.norm(10, num) == 'h'
    for num in [2,7,8,9,10,11]:
        assert basic_strategy.norm(9, num) == 'h'
    for num in [3,4,5,6]:
        assert basic_strategy.norm(9, num) == 'd'
    for i in [2,3,4,5,6,7,8]:
        for num in [1,2,3,4,5,6,7,8,9,10,11]:
            assert basic_strategy.norm(i, num) == 'h'

def test_ace():
    basic_strategy = Basic_strategy()
    for up_card in [2,3,4,5,6,7,8,9,10,11]:
        assert basic_strategy.ace(9, up_card) == 's'
    for up_card in [2,3,4,5,7,8,9,10,11]:
        assert basic_strategy.ace(8, up_card) == 's'
    assert basic_strategy.ace(8, 6) == 'd'    
    for up_card in [2,3,4,5,6]:
        assert basic_strategy.ace(7, up_card) == 'd'
    for up_card in [7,8]:
        assert basic_strategy.ace(7, up_card) == 's'
    for up_card in [9,10,11]:
        assert basic_strategy.ace(7, up_card) == 'h'
    for up_card in [2,7,8,9,10,11]:
        assert basic_strategy.ace(6, up_card) == 'h'
    for up_card in [3,4,5,6]:
        assert basic_strategy.ace(6, up_card) == 'd'
    for sum in [4,5]:
        for up_card in [2,3,7,8,9,10,11]:
            assert basic_strategy.ace(sum, up_card) == 'h'
        for up_card in [4,5,6]:
            assert basic_strategy.ace(sum, up_card) == 'd'
    for sum in [2,3]:
        for up_card in [2,3,4,7,8,9,10,11]:
            assert basic_strategy.ace(sum, up_card) == 'h'
        for up_card in [5,6]:
            assert basic_strategy.ace(sum, up_card) == 'd'
    assert Basic_strategy().ace(16,9, Deviation(running_count = 1, true_count = 4)) == 's'

def test_split():
    basic_strategy = Basic_strategy()
    for sum in [12,16]:
        for dealer_up_card in [2,3,4,5,6,7,8,9,10,11]:
            assert basic_strategy.split(sum, dealer_up_card, ace = True) == 'sp'
    for dealer_up_card in [2,3,4,5,6,7,8,9,10, 11]:
        assert basic_strategy.split(20, dealer_up_card) == 's'
    for dealer_up_card in [2,3,4,5,6,8,9]:
        assert basic_strategy.split(18, dealer_up_card) == 'sp'
    for dealer_up_card in [7,10,11]:
        assert basic_strategy.split(18, dealer_up_card) == 's'
    for dealer_up_card in [2,3,4,5,6,7]:
        assert basic_strategy.split(14, dealer_up_card) == 'sp'
    for dealer_up_card in [8,9,10,11]:
        assert basic_strategy.split(14, dealer_up_card) == 'h'
    for dealer_up_card in [2,3,4,5,6]:
        assert basic_strategy.split(12, dealer_up_card) == 'sp'
    for dealer_up_card in [7,8,9,10,11]:
        assert basic_strategy.split(12, dealer_up_card) == 'h'
    for num in [2,3,4,5,6,7,8,9]:
        assert basic_strategy.split(10, num) == 'd'
    for num in [10, 11]:
        assert basic_strategy.split(10, num) == 'h'
    for num in [1,2,3,4,5,6,7,8,9,10,11]:
        assert basic_strategy.split(8, num) == 'h'
    for num in [4,6]:
        for dealer_up_card in [4,5,6,7]:
            assert basic_strategy.split(num, dealer_up_card) == 'sp'
        for dealer_up_card in [2,3,8,9,10,11]:
            assert basic_strategy.split(num, dealer_up_card) == 'h'
