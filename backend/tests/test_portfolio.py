from fastapi.testclient import TestClient
from backend.src.main import app

client = TestClient(app)

def test_get_portfolio_existing():
    # Test with a valid portfolio id
    response = client.get("/portfolio/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Tech Portfolio",
        "value": 100000.0,
        "assets": ["AAPL", "GOOG", "AMZN"]
    }

def test_get_portfolio_non_existing():
    # Test with a non-existent portfolio id
    response = client.get("/portfolio/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Portfolio not found"}
