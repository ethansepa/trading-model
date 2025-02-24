# api/portfolio.py
from fastapi import APIRouter, HTTPException
from backend.src.api.tmp_db import fake_portfolios
from backend.src.models.portfolio import Portfolio

router = APIRouter()

@router.get("/portfolio/{id}", response_model=Portfolio)
async def get_portfolio(id: int):
    for portfolio in fake_portfolios:
        if portfolio.id == id:
            return portfolio
    else:
        raise HTTPException(status_code=404, detail="Portfolio not found")