# Finance Trading Bot

A modular, CrewAI-powered trading bot scaffold inspired by the [CrewAI stock_analysis example](https://github.com/crewAIInc/crewAI-examples/tree/main/stock_analysis).  
It fetches market data, engineers features, trains/predicts with a model, backtests, and (optionally) places paper trades via Alpaca.

> **For educational purposes only.**  
> This project is a demonstration of how to structure a modular, agent-based trading bot. It is **not** investment advice and comes with **no guarantees** of profitability.


##  Features

- **Agent-based pipeline**: DataFetcher → FeatureEngineer → Predictor → Backtester → Trader  
- **Easy to extend**: Swap in new agents or models  
- **Paper-trading ready**: Connects to Alpaca’s REST API  
- **Train & Inference modes**:  
  - `python main.py` → run analysis/prototype pipeline  
  - `python main.py <n_iterations>` → train the crew  


##  Prerequisites

- Python 3.11 or higher  
- [Alpaca paper-trading account](https://alpaca.markets/) (for live order execution)  
- OpenAI API key (if you’re using any LLM-based agents)  


##  Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/finance-trading-bot.git
   cd finance-trading-bot

2. **Create & activate a virtual environment**

   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate    # on macOS/Linux
   .venv\Scripts\activate       # on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Configure environment variables**
   Copy `.env.example` to `.env` and fill in your keys:

   ```dotenv
   # .env
   OPENAI_API_KEY=sk-…
   APCA_API_KEY_ID=your_alpaca_key
   APCA_API_SECRET_KEY=your_alpaca_secret
   APCA_API_BASE_URL=https://paper-api.alpaca.markets
   ```

##  Project Structure

```
finance-trading-agent/
├── .env.example           # example env vars
├── requirements.txt       # pip dependencies
├── setup.py               # package metadata
├── main.py                # CLI entrypoint (run/train)
├── crew.py                # defines StockAnalysisCrew
├── src/
│   └── trading_agent/
│       ├── agents/
│       │   ├── data_fetcher.py
│       │   ├── feature_engineer.py
│       │   ├── predictor.py
│       │   ├── backtester.py
│       │   └── trader.py
│       └── __init__.py
├── tests/                 
│   ├── test_data_fetcher.py
│   ├── test_data_fetcher.py
│   ├── test_feature_engineer.py
│   ├── test_predictor.py
│   ├── test_backtester.py
│   └── test_trader.py
├── docker/
|   └── Dockerfile
└── README.md
```


##  Usage

### Run analysis / live pipeline

```bash
python main.py
```

1. You’ll be prompted for a stock ticker (e.g. `AAPL`).
2. The crew will fetch data, compute features, train/predict, backtest, and (paper-)trade one share.

### Train the crew

```bash
python main.py 10
```

Runs `.train(n_iterations=10, inputs={…})` on the built-in sample prompt.

### Run tests

```bash
pytest --maxfail=1 --disable-warnings -q
```
