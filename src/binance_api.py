import requests
import json
import time
import hmac
import hashlib
from dotenv import load_dotenv
import os

BASE_URL = "https://testnet.binancefuture.com/api/v1"

load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")

def sign_params(params, secret_key):
    query_string = '&'.join([f"{key}={params[key]}" for key in sorted(params)])
    signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    params['signature'] = signature
    return params

def place_market_order(symbol, quantity, api_key, secret_key):
    url = f"{BASE_URL}/order"
    params = {
        "symbol": symbol,
        "side": "BUY",
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": int(time.time() * 1000)
    }
    params = sign_params(params, secret_key)
    headers = {"X-MBX-APIKEY": api_key}
    response = requests.post(url, params=params, headers=headers)
    return response.json()

def place_limit_order(symbol, quantity, price, api_key, secret_key):
    url = f"{BASE_URL}/order"
    params = {
        "symbol": symbol,
        "side": "BUY",
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC",
        "timestamp": int(time.time() * 1000)
    }
    params = sign_params(params, secret_key)
    headers = {"X-MBX-APIKEY": api_key}
    response = requests.post(url, params=params, headers=headers)
    return response.json()

def check_order_status(symbol, order_id, api_key, secret_key):
    url = f"{BASE_URL}/order"
    params = {
        "symbol": symbol,
        "orderId": order_id,
        "timestamp": int(time.time() * 1000)
    }
    params = sign_params(params, secret_key)
    headers = {"X-MBX-APIKEY": api_key}
    response = requests.get(url, params=params, headers=headers)
    return response.json()