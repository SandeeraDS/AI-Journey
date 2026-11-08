import json
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class Trade:
    symbol: str
    side: str
    qty: int
    price: float

    def notional(self) -> float:
        return self.price * self.quantity

    def is_buy(self) -> bool:
        return self.side == "BUY"

def save_trades(trades: list[Trade], path: str) -> None:
    with open(path, "w") as f:
        json.dump([asdict(t) for t in trades], f, indent=2)


def load_trades(path: str) -> list[Trade]:
    with open(path) as f:
        data = json.load(f)
    return [Trade(**d) for d in data]