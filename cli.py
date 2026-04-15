import argparse
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger
import logging
import sys

print("✅ Program started...")


setup_logger()

def main():
    try:
        parser = argparse.ArgumentParser(description="Simple Binance Futures Trading Bot")

        parser.add_argument("--symbol", help="Trading pair (e.g., BTCUSDT)")
        parser.add_argument("--side", help="BUY or SELL")
        parser.add_argument("--type", help="MARKET or LIMIT")
        parser.add_argument("--quantity", type=float, help="Order quantity")
        parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

        print("📌 Parsing arguments...")
        args = parser.parse_args()

        
        if len(sys.argv) == 1:
            print("\n⚠️ No arguments provided!")
            print("👉 Example usage:")
            print("python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001")
            return

        print("📌 Arguments received:", vars(args))

        
        print("📌 Validating input...")
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

       
        print("\n📌 Order Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price if args.price else 'N/A'}")

        
        print("\n🚀 Placing order on Binance Testnet...")
        order = place_order(args.symbol, args.side, args.type, args.quantity, args.price)

        print("📌 Response received from API")

        
        if not order or "error" in order:
            error_msg = order.get("error", "Unknown error occurred")
            print("❌ Order Failed:", error_msg)
            logging.error(error_msg)
        else:
            print("\n✅ Order Placed Successfully!")
            print(f"Order ID: {order.get('orderId')}")
            print(f"Status: {order.get('status')}")
            print(f"Executed Quantity: {order.get('executedQty')}")
            print(f"Average Price: {order.get('avgPrice', 'N/A')}")
            logging.info(order)

    except Exception as e:
        print("❌ Error:", str(e))
        logging.error(str(e))



if __name__ == "__main__":
    main()