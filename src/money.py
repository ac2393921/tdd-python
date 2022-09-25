from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel, PrivateAttr

from src.exchanger import CurrencyExchanger


class Expression(BaseModel, ABC):
    @abstractmethod
    def plus(addend: Expression) -> Expression:
        pass

    @abstractmethod
    def reduce(self, bank: CurrencyExchanger, to: str) -> Money:
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

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        from .sum import Sum

        return Sum(self, addend)

    def reduce(self, bank: CurrencyExchanger, to: str) -> Money:
        rate = bank.rate(self.currency, to)
        return Money(self.amount // rate, to)

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
