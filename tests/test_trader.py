from trading_agent.agents.trader import Trader

def test_trader_init(monkeypatch):
    # ensure no exception on init (requires env vars or defaults)
    monkeypatch.setenv("APCA_API_KEY_ID", "test_key")
    monkeypatch.setenv("APCA_API_SECRET_KEY", "test_secret")
    monkeypatch.setenv("APCA_API_BASE_URL", "https://paper-api.alpaca.markets")
    trader = Trader()
    assert hasattr(trader, 'place_order')