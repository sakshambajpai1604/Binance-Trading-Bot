def validate_order_side(side):
    return side.upper() in ["BUY", "SELL"]

def validate_order_type(order_type):
    return order_type.upper() in ["MARKET", "LIMIT"]
