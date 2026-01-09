import uuid
from datetime import datetime
from storage import instruments, orders, trades, portfolio
from models import OrderStatus

def fetch_instruments():
    return instruments

def create_order(order):
    validate_order(order)

    order_id = str(uuid.uuid4())

    execution_price = (
        order.price if order.orderStyle == "LIMIT"
        else get_market_price(order.symbol)
    )

    order_record = {
        "orderId": order_id,
        "symbol": order.symbol,
        "quantity": order.quantity,
        "orderType": order.orderType,
        "orderStyle": order.orderStyle,
        "price": execution_price,
        "status": OrderStatus.EXECUTED,
        "timestamp": datetime.utcnow()
    }

    orders[order_id] = order_record
    create_trade(order_record)
    update_portfolio(order_record)

    return order_record

def fetch_order(order_id):
    return orders.get(order_id)

def fetch_trades():
    return trades

def fetch_portfolio():
    return portfolio

def validate_order(order):
    if order.quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if order.orderStyle == "LIMIT" and order.price is None:
        raise ValueError("Price is mandatory for LIMIT orders")

    if not instrument_exists(order.symbol):
        raise ValueError("Invalid instrument symbol")

def instrument_exists(symbol):
    return any(inst["symbol"] == symbol for inst in instruments)

def get_market_price(symbol):
    for inst in instruments:
        if inst["symbol"] == symbol:
            return inst["lastTradedPrice"]
    return 0.0

def create_trade(order):
    trade = {
        "tradeId": str(uuid.uuid4()),
        "orderId": order["orderId"],
        "symbol": order["symbol"],
        "quantity": order["quantity"],
        "price": order["price"],
        "timestamp": datetime.utcnow()
    }
    trades.append(trade)

def update_portfolio(order):
    symbol = order["symbol"]
    qty = order["quantity"]
    price = order["price"]

    if symbol not in portfolio:
        portfolio[symbol] = {
            "symbol": symbol,
            "quantity": qty,
            "averagePrice": price,
            "currentValue": qty * price
        }
        return

    existing = portfolio[symbol]
    
    total_qty = existing["quantity"] + qty
    avg_price = (
        (existing["quantity"] * existing["averagePrice"]) +
        (qty * price)
    ) / total_qty

    existing["quantity"] = total_qty
    existing["averagePrice"] = avg_price
    existing["currentValue"] = total_qty * price
