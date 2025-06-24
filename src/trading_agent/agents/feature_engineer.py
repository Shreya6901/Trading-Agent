import pandas as pd

class FeatureEngineer:
    @staticmethod
    def add_sma(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
        df[f"SMA_{window}"] = df["Close"].rolling(window).mean()
        return df

    @staticmethod
    def add_rsi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
        delta = df["Close"].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window).mean()
        avg_loss = loss.rolling(window).mean()
        rs = avg_gain / avg_loss
        df[f"RSI_{window}"] = 100 - (100 / (1 + rs))
        return df

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.add_sma(df, 20)
        df = self.add_rsi(df, 14)
        df.dropna(inplace=True)
        return df