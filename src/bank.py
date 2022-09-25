from src.money import Expression


class Bank:
    def reduce(self, source: Expression, to: str):
        return source.reduce(to)
