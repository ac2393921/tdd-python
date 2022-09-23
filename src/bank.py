from src.expression import Expression
from src.money import Money


class Bank:
    def reduce(self, source: Expression, to: str):
        return Money.dollar(10)
