from src.money import Money


class Franc(Money):
    def times(self, multiplier: int) -> "Franc":
        return Franc(amount=self.amount * multiplier)
