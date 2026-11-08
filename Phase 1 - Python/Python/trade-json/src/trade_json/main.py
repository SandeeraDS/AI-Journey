import requests
from trade_json.models import Trade, save_trades, load_trades

trades = [
    Trade("AAPL", "BUY", 100, 190.5),
    Trade("MSFT", "SELL", 50, 410.0),
]


def main():
    # --- JSON file round-trip ---
    save_trades(trades, "trades.json")
    loaded = load_trades("trades.json")
    print(loaded)
    print(loaded == trades)

    # --- HTTP GET ---
    resp = requests.get("https://api.github.com/repos/python/cpython")
    resp.raise_for_status()  # like response.isSuccessful() check, but throws
    data = resp.json()  # parses JSON body straight into a dict
    print(data)
    print(data["full_name"], data["stargazers_count"])


if __name__ == "__main__":
    main()
