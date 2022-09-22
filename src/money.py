from abc import ABC, abstractmethod

from pydantic import BaseModel, PrivateAttr


class Money(BaseModel, ABC):
    _amount: int = PrivateAttr()
    _currency: str = PrivateAttr()

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: "Money") -> bool:
        return (self._amount == other._amount) and (
            self.__class__.__name__ == other.__class__.__name__
        )

    @property
    def currency(self) -> str:
        return self._currency

    @abstractmethod
    def times(self, multiplier: int) -> "Money":
        pass

    @staticmethod
    def dollar(amount: int) -> "Money":
        from .dollar import Dollar

        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> "Money":
        from .franc import Franc

        return Franc(amount, "CHF")
