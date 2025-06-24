import pandas as pd
from trading_agent.agents.predictor import Predictor

def test_train_and_predict(tmp_path):
    # create dummy data
    df = pd.DataFrame({
        "Close": list(range(10))
    })
    model_path = tmp_path / "model.pkl"
    predictor = Predictor(str(model_path))
    predictor.train(df)
    signal = predictor.predict(df)
    assert signal in (0, 1)