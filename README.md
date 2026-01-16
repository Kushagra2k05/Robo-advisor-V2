# 🤖 Robo Advisor V2  
An AI-powered investment advisory engine built using Modern Portfolio Theory (MPT), Black–Litterman modeling, SIP goal planning, risk profiling, and Monte Carlo simulation.  
This backend replicates the core intelligence used by real robo-advisors like Wealthfront, Betterment, Vanguard Digital Advisor, and Groww.

---

## 🚀 Features

### 🧩 1. Risk Profiling Engine  
- Uses a weighted questionnaire  
- Classifies users into: Conservative, Balanced, Moderate, Growth, Aggressive  
- Drives asset allocation logic

### 📈 2. Market Data Integration  
Fetches 5-year historical price data using **Yahoo Finance (yfinance)**.  
Handles:  
- Multi-index data  
- Adjusted Close prices  
- Missing data cleaning

### 🧮 3. Portfolio Optimization  
#### ✔ Modern Portfolio Theory (MPT)  
- Computes expected returns  
- Ledoit–Wolf covariance shrinkage  
- Maximizes Sharpe Ratio  
- Outputs optimal allocation weights

#### ✔ Black–Litterman Model  
- Incorporates market cap weights  
- Generates equilibrium return estimates  
- Produces stable, institution-grade allocations

### 🎯 4. Goal-Based SIP Calculator  
Calculates monthly SIP amount using:  
- Expected return  
- Investment horizon  
- Inflation adjustment  
- Future target value  

### 🎲 5. Monte Carlo Simulation  
Simulates thousands of future market scenarios to estimate:  
- Portfolio variance  
- Probability distribution of outcomes  
- Worst-case & best-case projections  

### 🔄 6. Rebalancing Engine  
Given current portfolio holdings and optimal targets, it computes:  
- Buy/Sell quantities  
- Required adjustments to match efficient allocation  

---

## 🛠️ Tech Stack

- Python 3.10+  
- NumPy, Pandas  
- yfinance  
- PyPortfolioOpt  
- scikit-learn  
- SciPy  

---

## 📂 Project Structure
Robo-advisor-V2/
│── main.py
│── README.md
│── requirements.txt
│── config/
│ └── assets.py
└── services/
├── risk_profile.py
├── price_fetcher.py
├── mpt_optimizer.py
├── black_litterman.py
├── goals.py
├── monte_carlo.py
├── rebalance.py
├── backtest.py
└── health_score.py

