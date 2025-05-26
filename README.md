# Trading Bot for Binance Futures Testnet

This project is a simplified trading bot that interacts with the Binance Futures Testnet. It allows users to place market and limit orders, log API interactions, and handle user input via a command-line interface.

## Features

- Place market and limit orders on the Binance Futures Testnet.
- Log all API interactions for review.
- Command-line interface for user input and order execution.

## Project Structure

```
trading-bot
├── src
│   ├── bot.py          # Contains the BasicBot class for Binance API interaction
│   ├── binance_api.py  # Functions for making REST API calls to Binance
│   ├── cli.py          # Command-line interface for user input
│   ├── logger.py       # Logging functionality for API requests and responses
│   └── utils.py        # Utility functions for input validation and output formatting
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/sakshambajpai1604/Binance-Trading-Bot.git
   cd trading-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your API credentials in `src/bot.py`.

## Usage

To start the trading bot, run the following command:
```
python src/cli.py
```

Follow the prompts to place orders and interact with the Binance Futures Testnet.

## Logging

All API requests and responses are logged in a file for later review. Check the logging configuration in `src/logger.py` for details.
