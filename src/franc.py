from src.money import Money


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Money.franc(amount=self._amount * multiplier)
