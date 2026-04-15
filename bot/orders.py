def place_order(symbol, side, order_type, quantity, price=None):
    print("🔄 Simulating order...")

    order = {
        "orderId": 123456,
        "status": "FILLED",
        "executedQty": quantity,
        "avgPrice": price if price else 65000,
        "symbol": symbol,
        "side": side,
        "type": order_type
    }

    return order