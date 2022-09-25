from typing import Dict, Optional, Tuple

from pydantic import PrivateAttr

from src.exchanger import CurrencyExchanger
from src.money import Expression


class Bank(CurrencyExchanger):
    _rates: Dict[
        Tuple[str, str],
        int,
    ] = PrivateAttr()

    def __init__(self):
        self._rates = dict()

    def reduce(self, source: Expression, to: str):
        return source.reduce(self, to)

    def add_rate(self, frm: str, to: str, rate: int) -> None:
        self._rates[(frm, to)] = rate

    def rate(self, frm: str, to: str) -> Optional[int]:
        if frm == to:
            return 1
        rate = self._rates.get((frm, to))
        if not rate:
            raise KeyError
        return rate
