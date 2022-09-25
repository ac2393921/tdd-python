from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel, PrivateAttr


class Expression(BaseModel, ABC):
    @abstractmethod
    def reduce(self, to: str) -> Money:
        pass


class Money(Expression):
    _amount: int = PrivateAttr()
    _currency: str = PrivateAttr()

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def amount(self) -> int:
        return self._amount

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Money) -> Expression:
        from .sum import Sum

        return Sum(self, addend)

    def reduce(self, to: str) -> Money:
        return self

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")

    def __eq__(self, other: Money) -> bool:
        return (self._amount == other._amount) and (self.currency == other.currency)

    def __str__(self) -> str:
        return f"{self._amount} {self.currency}"
