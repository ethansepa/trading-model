# main.py
from fastapi import FastAPI
from backend.src.api.portfolio import router as portfolio_router

app = FastAPI()

# Include the portfolio routes
app.include_router(portfolio_router)
