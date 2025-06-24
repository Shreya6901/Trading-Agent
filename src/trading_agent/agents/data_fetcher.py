import pandas as pd
import yfinance as yf

class DataFetcher:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def fetch(self, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
        df = yf.download(self.symbol, period=period, interval=interval, progress=False)
        df.dropna(inplace=True)
        return df