from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import EfficientFrontier
from pypfopt import objective_functions
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt import HRPOpt
from pypfopt import CLA
from pypfopt import black_litterman
from pypfopt import BlackLittermanModel
from pypfopt import plotting
import pandas as pd

df = pd.read_csv('sp500_data.csv', parse_dates=True, index_col="Date")
returns = df.pct_change().dropna()
mu = expected_returns.mean_historical_return(df)
S = risk_models.CovarianceShrinkage(df).ledoit_wolf()

from pypfopt.efficient_frontier import EfficientFrontier

ef = EfficientFrontier(mu, S)
weights = ef.min_volatility()

cleaned_weights = ef.clean_weights()
ef.save_weights_to_file("weights.txt")  # saves to file
# print(sorted(cleaned_weights.items(), key=lambda x: x[1], reverse=True))

hrp = HRPOpt(returns)
weights = hrp.optimize()
print("efficient frontier - minimize volatility")
ef.portfolio_performance(verbose=True)
print("hierarchical risk parity")
hrp.portfolio_performance(verbose=True)
# print(sorted(weights.items(), key=lambda x: x[1], reverse=True))