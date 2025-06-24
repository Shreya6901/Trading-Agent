import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

class Trader:
    def __init__(self):
        load_dotenv()
        self.api = tradeapi.REST(
            os.getenv("APCA_API_KEY_ID"),
            os.getenv("APCA_API_SECRET_KEY"),
            os.getenv("APCA_API_BASE_URL"),
        )

    def place_order(self, symbol: str, side: str, qty: int):
        return self.api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type="market",
            time_in_force="gtc",
        )