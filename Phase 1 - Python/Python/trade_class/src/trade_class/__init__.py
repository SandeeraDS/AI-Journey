from dataclasses import dataclass

@dataclass
class Trade:
    symbol: str
    side: str
    quantity: float
    price: float

    def notional(self) -> float:
        return self.quantity * self.price

    def is_buy(self) -> bool:
        return self.side == "BUY"

trades = [
    Trade("AAPL", "BUY", 100, 190.5),
    Trade("MSFT", "SELL", 50, 410.0),
    Trade("AAPL", "SELL", 40, 192.0),
    Trade("TSLA", "BUY", 10, 250.0),
    Trade("MSFT", "BUY", 20, 405.0),
]


def main():
    t = trades[0]
    print(t)                         # dataclass auto-generates __repr__
    print(t.notional())
    print(t.is_buy())
    print(t == Trade("AAPL", "BUY", 100, 190.5))   # dataclass auto-generates __eq__

    buys = [t for t in trades if t.is_buy()]
    print([t.symbol for t in buys])

    total = sum(t.notional() for t in trades if t.is_buy())   # generator expression, no brackets
    print(total)

    # This "works" at runtime despite being wrong — proving hints aren't enforced:
    bad = Trade("AAPL", "BUY", "ten", 190.5)
    print(bad)

if __name__ == "__main__":
    main()