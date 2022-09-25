from src.bank import Bank
from src.money import Expression, Money
from src.sum import Sum


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


def test_simple_addition():
    five: Money = Money.dollar(5)
    sum: Expression = five.plus(Money.dollar(5))

    bank = Bank()
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced


def test_plus_return_sum():
    five: Money = Money.dollar(5)
    result: Expression = five.plus(five)
    sum: Sum = result
    assert five == sum.augend
    assert five == sum.addend


def test_reduce_sum():
    sum: Expression = Sum(augend=Money.dollar(3), addend=Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert Money.dollar(7) == result


def test_reduce_money():
    bank: Bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result


def test_reduce_money_different_currency():
    bank: Bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result: Money = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result


def test_identity_rate():
    assert 1 == Bank().rate("USD", "USD")


def test_mixed_addition():
    five_bucks: Expression = Money.dollar(5)
    ten_francs: Expression = Money.franc(10)
    bank: Bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result: Money = bank.reduce(five_bucks.plus(ten_francs), "USD")
    assert Money.dollar(10) == result


def test_sum_plus_money():
    five_bucks: Expression = Money.dollar(5)
    ten_francs: Expression = Money.franc(10)
    bank: Bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    sum: Expression = Sum(five_bucks, ten_francs).plus(five_bucks)
    result: Money = bank.reduce(sum, "USD")
    assert Money.dollar(15) == result


def test_sum_times():
    five_bucks: Expression = Money.dollar(5)
    ten_francs: Expression = Money.franc(10)
    bank: Bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    sum: Expression = Sum(five_bucks, ten_francs).times(2)
    result: Money = bank.reduce(sum, "USD")
    assert Money.dollar(20) == result
