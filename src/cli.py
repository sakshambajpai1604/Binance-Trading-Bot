from dotenv import load_dotenv
import os
from bot import BasicBot

load_dotenv()

def main():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    base_url = os.getenv("BASE_URL")

    if not all([api_key, api_secret, base_url]):
        print("Error: Missing API credentials in .env")
        return

    bot = BasicBot(api_key, api_secret, base_url)

    print("Welcome to Binance Futures Testnet Bot")

    try:
        side = input("Order side (BUY/SELL): ").upper()
        symbol = input("Symbol (e.g., BTCUSDT): ").upper()
        quantity = float(input("Quantity: "))
        order_type = input("Order type (MARKET/LIMIT): ").upper()

        if order_type == "MARKET":
            res = bot.place_market_order(symbol, side, quantity)
        elif order_type == "LIMIT":
            price = float(input("Enter limit price: "))
            res = bot.place_limit_order(symbol, side, quantity, price)
        else:
            print("Invalid order type.")
            return

        print("Order Result:")
        print(res)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()