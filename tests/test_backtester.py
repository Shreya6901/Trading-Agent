import pandas as pd
from trading_agent.agents.backtester import Backtester

def test_run_returns_series():
    df = pd.DataFrame({
        "Close": [100, 101, 102, 103, 104],
        "Position": [1, 0, 1, 0, 1]
    })
    res = Backtester().run(df, signal_col="Position")
    assert hasattr(res, 'iloc')
    assert len(res) == len(df)