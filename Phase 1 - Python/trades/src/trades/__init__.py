trades = [
    {"symbol": "AAPL", "side": "BUY",  "qty": 100, "price": 190.5},
    {"symbol": "MSFT", "side": "SELL", "qty": 50,  "price": 410.0},
    {"symbol": "AAPL", "side": "SELL", "qty": 40,  "price": 192.0},
    {"symbol": "TSLA", "side": "BUY",  "qty": 10,  "price": 250.0},
    {"symbol": "MSFT", "side": "BUY",  "qty": 20,  "price": 405.0},
]

def notional(trade: dict) -> float:
    return trade["qty"] * trade["price"]
    ...

def symbols(trades: list[dict]) -> set[str]:
    # TODO: one-line set comprehension: {... for t in trades}
    return { t["symbol"] for t in trades }
    ...

def buys_over(trades: list[dict], min_notional: float = 1000.0) -> list[dict]:
    # TODO: one-line list comprehension, BUY trades with notional > min_notional
    return [t for t in trades if notional(t) >= min_notional and t["side"] == "BUY"]
    ...

def net_position(trades: list[dict]) -> dict[str, int]:
    # TODO: plain for-loop. BUY adds qty, SELL subtracts. Use dict.get(k, 0)
    dict_list = {}
    for t in trades:
        if t["side"] == "BUY":
            dict_list[t["symbol"]] = dict_list.get(t["symbol"], 0) + t["qty"]
        else:
            dict_list[t["symbol"]] = dict_list.get(t["symbol"], 0) - t["qty"]
    return dict_list
    ...

def largest(trades: list[dict]) -> str:
    # TODO: symbol of the trade with the biggest notional. Use max(..., key=notional)
    return max(trades, key=lambda t: notional(t))["symbol"]
    ...

def main():
    print(notional(trades[0]))
    print(sorted(symbols(trades)))
    print([t["symbol"] for t in buys_over(trades)])
    print([t["symbol"] for t in buys_over(trades, min_notional=5000)])
    print(net_position(trades))
    print(largest(trades))
    print([t["symbol"] for t in trades[-2:]])   # slicing: last two

if __name__ == "__main__":
    main()