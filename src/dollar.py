from pydantic import BaseModel


class Dollar(BaseModel):
    amount: int

    def times(self, multiplier: int):
        self.amount *= multiplier
