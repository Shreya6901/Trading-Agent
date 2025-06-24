import pytest
from trading_agent.agents.data_fetcher import DataFetcher

def test_fetch_columns():
    df = DataFetcher("AAPL").fetch(period="1mo", interval="1d")
    assert "Close" in df.columns
    assert not df.empty