from src.dollar import Dollar


def test_multiplication():
    five: Dollar = Dollar(amount=5)
    five.times(2)
    assert 10 == five.amount
