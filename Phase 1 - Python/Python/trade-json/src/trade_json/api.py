from fastapi import FastAPI, HTTPException
from trade_json.pmodels import Trade

app = FastAPI()

# in-memory "database" — a dict keyed by an auto-incrementing id
db: dict[int, Trade] = {}
next_id = 1


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/trades")
def list_trades():
    return db


@app.post("/trades", status_code=201)
def create_trade(trade: Trade):
    global next_id
    trade_id = next_id
    db[trade_id] = trade
    next_id += 1
    return {"id": trade_id, **trade.model_dump()}


@app.get("/trades/{trade_id}")
def get_trade(trade_id: int):
    if trade_id not in db:
        raise HTTPException(status_code=404, detail="Trade not found")
    return db[trade_id]


@app.delete("/trades/{trade_id}", status_code=204)
def delete_trade(trade_id: int):
    if trade_id not in db:
        raise HTTPException(status_code=404, detail="Trade not found")
    del db[trade_id]