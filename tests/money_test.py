from src.dollar import Dollar
from src.franc import Franc


def test_multiplication():
    five: Dollar = Dollar(amount=5)
    assert Dollar(amount=10) == five.times(2)
    assert Dollar(amount=15) == five.times(3)


def test_equality():
    assert Dollar(amount=5) == Dollar(amount=5)
    assert Dollar(amount=5) != Dollar(amount=6)
    assert Franc(amount=5) != Dollar(amount=5)


def testFrancMultiplication():
    five: Franc = Franc(amount=5)
    assert Franc(amount=10) == five.times(2)
    assert Franc(amount=15) == five.times(3)
