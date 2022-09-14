from __future__ import annotations

from pydantic import BaseModel


class Dollar(BaseModel):
    amount: int

    def times(self, multiplier: int) -> Dollar:
        return Dollar(amount=self.amount * multiplier)
