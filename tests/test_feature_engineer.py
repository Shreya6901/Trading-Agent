import pandas as pd
from trading_agent.agents.feature_engineer import FeatureEngineer

def test_transform_adds_columns():
    df = pd.DataFrame({
        "Close": [100, 102, 101, 103, 105, 107, 106, 108, 110, 112, 114, 113, 115, 117, 119, 118, 120, 122, 124, 123, 125]
    })
    out = FeatureEngineer().transform(df)
    assert any(col.startswith("SMA_") for col in out.columns)
    assert any(col.startswith("RSI_") for col in out.columns)