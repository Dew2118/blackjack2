from blackjack2.src.deviation import Deviation

def test_deviation_init():
    assert Deviation(running_count = 0, true_count = 0) is not None

def test_norm():
    assert Deviation(running_count = 1, true_count = 4).norm(16,9) == 's'
    assert Deviation(running_count = 1, true_count = 3).norm(16,9) == 'h'
    assert Deviation(running_count = 1, true_count = 4).norm(16,10) == 's'
    assert Deviation(running_count = 0, true_count = 4).norm(16,10) == 'h'
    assert Deviation(true_count = 4).norm(15,10) == 's'
    assert Deviation(true_count = 3).norm(15,10) == 'h'
    assert Deviation(true_count = -1).norm(13,2) == 'd'
    assert Deviation(true_count = 2).norm(13,2) == 's'
    assert Deviation(true_count = 3).norm(12,2) == 's'
    assert Deviation(true_count = 2).norm(12,2) == 'h'
    assert Deviation(true_count = 2).norm(12,3) == 's'
    assert Deviation(true_count = 1).norm(12,3) == 'h'
    assert Deviation(running_count = -1).norm(12,4) == 'd'
    assert Deviation(running_count = 0).norm(12,4) == 's'
    assert Deviation(true_count = 4).norm(10,10) == 'd'
    assert Deviation(true_count = 3).norm(10,10) == 'h'
    assert Deviation(true_count = 3).norm(10,11) == 'd'
    assert Deviation(true_count = 2).norm(10,11) == 'h'
    assert Deviation(true_count = 1).norm(9,2) == 'd'
    assert Deviation(true_count = 0).norm(9,2) == 'h'
    assert Deviation(true_count = 3).norm(9,7) == 'd'
    assert Deviation(true_count = 2).norm(9,7) == 'h'
    assert Deviation(true_count = 2).norm(8,6) == 'd'
    assert Deviation(true_count = 1).norm(8,6) == 'h'

def test_ace():
    assert Deviation(true_count = 3).ace(19,4) == 'd'
    assert Deviation(true_count = 2).ace(19,4) == 's'
    assert Deviation(true_count = 1).ace(19,5) == 'd'
    assert Deviation(true_count = 0).ace(19,5) == 's'
    assert Deviation(running_count = -1).ace(19,6) == 's'
    assert Deviation(running_count = 1).ace(19,6) == 'd'
    assert Deviation(true_count = 1).ace(17,2) == 'd'
    assert Deviation(true_count = 0).ace(17,2) == 'h'

def test_split():
    assert Deviation(true_count = 6).split(20,4) == 'sp'
    assert Deviation(true_count = 5).split(20,4) == 's'
    assert Deviation(true_count = 5).split(20,5) == 'sp'
    assert Deviation(true_count = 4).split(20,5) == 's'
    assert Deviation(true_count = 4).split(20,6) == 'sp'
    assert Deviation(true_count = 3).split(20,6) == 's'
