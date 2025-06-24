# src/trading_bot/main.py

import os
from dotenv import load_dotenv

from crewai import Crew, Task, Process
from trading_agent.agents.data_fetcher import DataFetcher
from trading_agent.agents.feature_engineer import FeatureEngineer
from trading_agent.agents.predictor import Predictor
from trading_agent.agents.backtester import Backtester
from trading_agent.agents.trader import Trader

def main():
    load_dotenv()  # loads APCA_* env vars

    symbol = "AAPL"
    fetcher    = DataFetcher(symbol)
    engineer   = FeatureEngineer()
    predictor  = Predictor()
    backtester = Backtester()
    trader     = Trader()

    # Define your pipeline tasks
    tasks = [
        Task(
            description=f"Fetch 1y daily OHLCV for {symbol}",
            agent=fetcher.fetch
        ),
        Task(
            description="Compute SMA (20) & RSI (14) indicators",
            agent=engineer.transform
        ),
        Task(
            description="Train RandomForest on features",
            agent=predictor.train
        ),
        Task(
            description="Generate buy (1) / sell (0) signal",
            agent=predictor.predict
        ),
        Task(
            description="Backtest strategy returns",
            agent=backtester.run
        ),
        Task(
            description="Place one-share market order based on signal",
            agent=lambda signal: trader.place_order(
                symbol,
                "buy" if signal else "sell",
                qty=1
            )
        ),
    ]

    # Assemble & run the crew
    crew = Crew(
        agents=[],                # no explicit Agent objects needed here
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    crew_output = crew.kickoff()
    print("Final output:", crew_output.raw)

if __name__ == "__main__":
    main()
