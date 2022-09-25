from pydantic import PrivateAttr

from src.bank import Bank
from src.money import Expression, Money


class Sum(Money):
    _augend: Expression = PrivateAttr()
    _addend: Expression = PrivateAttr()

    def __init__(self, augend: Expression, addend: Expression) -> None:
        self._augend = augend
        self._addend = addend

    @property
    def augend(self) -> Expression:
        return self._augend

    @property
    def addend(self) -> Expression:
        return self._addend

    def times(self, multiplier: int) -> Expression:
        return Sum(self._augend.times(multiplier), self._addend.times(multiplier))

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> Money:
        amount = self._augend.reduce(bank, to).amount + self._addend.reduce(bank, to).amount
        return Money(amount, to)
