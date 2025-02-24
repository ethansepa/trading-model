# api/tmp_db.py
from backend.src.models.portfolio import Portfolio

# Mock data
fake_portfolios = [
    Portfolio(id=1, name="Tech Portfolio", value=100000.00, assets=["AAPL", "GOOG", "AMZN"]),
    Portfolio(id=2, name="Crypto Portfolio", value=50000.00, assets=["BTC", "ETH", "ADA"]),
]