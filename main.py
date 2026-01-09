from fastapi import FastAPI, HTTPException
from schemas import OrderRequest
from services import (
    fetch_instruments,
    create_order,
    fetch_order,
    fetch_trades,
    fetch_portfolio
)

app = FastAPI(title="Bajaj Broking Trading API")

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.get("/api/v1/instruments")
def get_instruments():
    return fetch_instruments()

@app.post("/api/v1/orders")
def place_order(order: OrderRequest):
    return create_order(order)

@app.get("/api/v1/orders/{order_id}")
def get_order(order_id: str):
    order = fetch_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/api/v1/trades")
def get_trades():
    return fetch_trades()

@app.get("/api/v1/portfolio")
def get_portfolio():
    return fetch_portfolio()
