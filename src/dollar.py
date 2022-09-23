from src.money import Money


class Dollar(Money):
    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)
