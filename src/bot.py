from binance.client import Client
from binance.exceptions import BinanceAPIException
from logger import get_logger

logger = get_logger()

class BasicBot:
    def __init__(self, api_key, api_secret, base_url):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = base_url
        logger.info("Binance client initialized.")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"Market Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Market order failed: {e}")
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logger.info(f"Limit Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Limit order failed: {e}")
            return {"error": str(e)}