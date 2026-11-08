from tradelib.models import Trade


def symbols(trades: list[Trade]) -> set[str]:
    return {t.symbol for t in trades}


def buys_over(trades: list[Trade], min_notional: float = 1000.0) -> list[Trade]:
    return [t for t in trades if t.is_buy() and t.notional() > min_notional]


def net_position(trades: list[Trade]) -> dict[str, int]:
    net = {}
    for t in trades:
        net[t.symbol] = net.get(t.symbol, 0) + (t.qty if t.is_buy() else -t.qty)
    return net


def largest(trades: list[Trade]) -> str:
    return max(trades, key=lambda t: t.notional()).symbol