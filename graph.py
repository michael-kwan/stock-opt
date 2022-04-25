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

import matplotlib.pyplot as plt
import copy
import numpy as np
import scipy.cluster.hierarchy as sch

df = pd.read_csv('sp500_data.csv', parse_dates=True, index_col="Date")
df = df.drop('CEG', 1) # Remove outlier
returns = df.pct_change().dropna()
mu = expected_returns.mean_historical_return(df)
S = risk_models.CovarianceShrinkage(df).ledoit_wolf()

print(S)

from pypfopt.efficient_frontier import EfficientFrontier

ef = EfficientFrontier(mu, S)

fig, ax = plt.subplots()
ef_max_sharpe = copy.deepcopy(ef)
plotting.plot_efficient_frontier(ef, ax=ax, show_assets=True)

# Find the tangency portfolio
ef_max_sharpe.max_sharpe()
ret_tangent, std_tangent, _ = ef_max_sharpe.portfolio_performance()
ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r", label="Max Sharpe")

# Generate random portfolios - TODO
n_samples = 1000
w = np.random.dirichlet(np.ones(ef.n_assets), n_samples)
rets = w.dot(ef.expected_returns)
stds = np.sqrt(np.diag(w @ ef.cov_matrix @ w.T))
sharpes = rets / stds
# ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")

# Output
ax.set_title("Efficient Frontier on SP500 Assets")
ax.legend()
plt.tight_layout()
plt.savefig("ef_scatter.png", dpi=200)
plt.show()