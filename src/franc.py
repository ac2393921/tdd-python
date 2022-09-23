from src.money import Money


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)
