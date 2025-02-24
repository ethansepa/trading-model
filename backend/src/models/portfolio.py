# models/portfolio.py
from pydantic import BaseModel

class Portfolio(BaseModel):
    id: int
    name: str
    value: float
    assets: list[str]
