import pandas as pd

class Backtester:
    def run(self, df: pd.DataFrame, signal_col: str = "Signal") -> pd.Series:
        df = df.copy()
        df["Position"] = df[signal_col].shift(1)
        df["Strategy_Return"] = df["Position"] * df["Close"].pct_change()
        return (1 + df["Strategy_Return"].fillna(0)).cumprod() - 1