from src.money import Money


class Dollar(Money):
    def times(self, multiplier: int) -> "Dollar":
        return Dollar(amount=self.amount * multiplier)
