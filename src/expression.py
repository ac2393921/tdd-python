from abc import ABC

from pydantic import BaseModel


class Expression(BaseModel, ABC):
    pass
