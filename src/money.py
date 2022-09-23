from pydantic import BaseModel, PrivateAttr


class Money(BaseModel):
    _amount: int = PrivateAttr()
    _currency: str = PrivateAttr()

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: "Money") -> bool:
        return (self._amount == other._amount) and (self.currency == other.currency)

    def __str__(self) -> str:
        return f"{self._amount} {self.currency}"

    @property
    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> "Money":
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int) -> "Money":
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> "Money":
        return Money(amount, "CHF")
