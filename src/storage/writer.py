from abc import ABC, abstractmethod
from src.model.equity import Equity

class Writer(ABC):
    @classmethod 
    @abstractmethod
    def save_equities(cls, equities: list[Equity]):
        pass