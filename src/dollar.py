from src.money import Money


class Dollar(Money):
    def times(self, multiplier: int) -> Money:
        return Money.dollar(amount=self._amount * multiplier)
