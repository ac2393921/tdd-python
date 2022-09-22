from pydantic import BaseModel


class Money(BaseModel):
    amount: int

    def __eq__(self, other: "Money") -> bool:
        return (self.amount == other.amount) and (
            self.__class__.__name__ == other.__class__.__name__
        )
