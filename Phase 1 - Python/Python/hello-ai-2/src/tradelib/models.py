from dataclasses import dataclass
from dataclasses import asdict
import json




@dataclass
class Trade:
    symbol: str
    side: str
    qty: int
    price: float

    def notional(self) -> float:
        return self.qty * self.price

    def is_buy(self) -> bool:
        return self.side == "BUY"