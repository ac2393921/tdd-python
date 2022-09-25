from pydantic import PrivateAttr

from src.bank import Bank
from src.money import Money


class Sum(Money):
    _augend: Money = PrivateAttr()
    _addend: Money = PrivateAttr()

    def __init__(self, augend: Money, addend: Money) -> None:
        self._augend = augend
        self._addend = addend

    @property
    def augend(self) -> Money:
        return self._augend

    @property
    def addend(self) -> Money:
        return self._addend

    def reduce(self, bank: Bank, to: str) -> Money:
        amount = self._augend.amount + self._addend.amount
        return Money(amount, to)
