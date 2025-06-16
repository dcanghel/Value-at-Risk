import numpy as np
from scipy.stats import norm, t

def historical_var(returns, confidence_level):
    sorted_returns = np.sort(returns)
    index = int((1 - confidence_level) * len(sorted_returns))
    return -sorted_returns[index]

def parametric_var(returns, confidence_level, dist='normal'):
    mu, sigma = returns.mean(), returns.std()
    if dist == 'normal':
        z = norm.ppf(1 - confidence_level)
        return -(mu + z * sigma)
    else:
        df = len(returns) - 1
        t_val = t.ppf(1 - confidence_level, df)
        return -(mu + t_val * sigma)

def monte_carlo_var(returns, confidence_level, simulations=10000):
    mu, sigma = returns.mean(), returns.std()
    sim = np.random.normal(mu, sigma, simulations)
    sim_sorted = np.sort(sim)
    index = int((1 - confidence_level) * simulations)
    return -sim_sorted[index]
