from pydantic import ValidationError
from trade_json.pmodels import Trade

# 1. Normal construction
t = Trade(symbol="AAPL", side="BUY", qty=100, price=190.5)
print(t)
print(t.notional())

# 2. Type coercion: numeric string -> int
t2 = Trade(symbol="AAPL", side="BUY", qty="100", price=190.5)
print(t2.qty, type(t2.qty))

# 3. Validation failure: wrong type
try:
    Trade(symbol="AAPL", side="BUY", qty="ten", price=190.5)
except ValidationError as e:
    print("caught:", e.error_count(), "error(s)")

# 4. Validation failure: constraint violated (qty must be > 0)
try:
    Trade(symbol="AAPL", side="BUY", qty=-5, price=190.5)
except ValidationError as e:
    print("caught:", e.error_count(), "error(s)")

# 5. Parse straight from JSON
json_str = '{"symbol": "MSFT", "side": "SELL", "qty": 50, "price": 410.0}'
t3 = Trade.model_validate_json(json_str)
print(t3)

# 6. Dump back to dict / JSON
print(t.model_dump())
print(t.model_dump_json())