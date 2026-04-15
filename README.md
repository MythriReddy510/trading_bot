# Trading Bot (Binance Futures Testnet)

## 📌 Description
This is a simple Python CLI-based trading bot that places MARKET and LIMIT orders.

## ⚙️ Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI input handling
- Input validation
- Logging system

## 🛠️ Setup

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt

## ▶️ Run

### MARKET Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000

## 📁 Project Structure
trading_bot/
│── bot/
│── cli.py
│── requirements.txt
│── README.md

## 📝 Note
Order execution is simulated for testing purposes.
The code structure supports real Binance API integration.