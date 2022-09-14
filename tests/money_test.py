from src.dollar import Dollar


def test_multiplication():
    five: Dollar = Dollar(amount=5)
    product: Dollar = five.times(2)
    assert 10 == product.amount

    product: Dollar = five.times(3)
    five.times(3)
    assert 15 == product.amount
