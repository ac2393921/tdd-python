from abc import ABC, abstractmethod

from pydantic import BaseModel


class CurrencyExchanger(BaseModel, ABC):
    @abstractmethod
    def rate(self, fromcurr: str, tocurr: str) -> int:
        pass
