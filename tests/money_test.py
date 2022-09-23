from src.money import Money


def test_multiplication():
    five: Money = Money.dollar(amount=5)
    assert Money.dollar(amount=10) == five.times(2)
    assert Money.dollar(amount=15) == five.times(3)


def test_equality():
    assert Money.dollar(amount=5) == Money.dollar(amount=5)
    assert Money.dollar(amount=5) != Money.dollar(amount=6)
    assert Money.franc(amount=5) != Money.dollar(amount=5)


def test_currency():
    assert "USD" == Money.dollar(1).currency
    assert "CHF" == Money.franc(1).currency
