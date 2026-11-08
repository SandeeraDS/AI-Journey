from tradelib.models import Trade
from tradelib.analysis import symbols, buys_over, net_position, largest

trades = [
    Trade("AAPL", "BUY", 100, 190.5),
    Trade("MSFT", "SELL", 50, 410.0),
    Trade("AAPL", "SELL", 40, 192.0),
    Trade("TSLA", "BUY", 10, 250.0),
    Trade("MSFT", "BUY", 20, 405.0),
]


def main():
    print(sorted(symbols(trades)))
    print([t.symbol for t in buys_over(trades, min_notional=5000)])
    print(net_position(trades))
    print(largest(trades))


if __name__ == "__main__":
    main()