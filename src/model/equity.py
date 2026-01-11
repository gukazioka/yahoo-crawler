from dataclasses import dataclass

@dataclass
class Equity:
    name: str
    symbol: str
    price: float