from setuptools import setup, find_packages

setup(
    name="trading_agent",
    version="0.1.0",
    description="A modular trading bot using the CrewAI framework",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai>=0.1.0",
        "pandas>=1.5.0",
        "yfinance>=0.2.0",
        "scikit-learn>=1.2.0",
        "joblib>=1.2.0",
        "alpaca-trade-api>=2.0.0",
        "python-dotenv>=0.21.0"
    ],
    entry_points={
        "console_scripts": [
            "trading-agent=trading_agent.main:main"
        ]
    },
    python_requires=">=3.10,<3.14",
)