from pydantic import BaseModel, Field


class Trade(BaseModel):
    symbol: str
    side: str
    qty: int = Field(gt=0)
    price: float = Field(gt=0)

    def notional(self) -> float:
        return self.qty * self.price

    def is_buy(self) -> bool:
        return self.side == "BUY"