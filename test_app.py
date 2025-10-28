from app import add

def test_add_two_positive_numbers():
    assert add(2, 3) == 5

def test_add_with_zero():
    assert add(4, 0) == 4
