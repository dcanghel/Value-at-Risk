import matplotlib.pyplot as plt
import numpy as np

def plot_vars(returns, hvar_95, hvar_99, norm_var_95, norm_var_99, tvar_95, tvar_99, mc_var_95, mc_var_99):
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.hist(returns, bins=50, alpha=0.7, color='blue', label='Returns')
    plt.axvline(-hvar_95, color='red', linestyle='--', label=f'95% VaR: {hvar_95:.4f}')
    plt.axvline(-hvar_99, color='orange', linestyle='--', label=f'99% VaR: {hvar_99:.4f}')
    plt.title('Historical VaR')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.hist(returns, bins=50, alpha=0.7, color='green', label='Returns')
    plt.axvline(-norm_var_95, color='red', linestyle='--', label=f'Normal 95% VaR: {norm_var_95:.4f}')
    plt.axvline(-norm_var_99, color='orange', linestyle='--', label=f'Normal 99% VaR: {norm_var_99:.4f}')
    plt.axvline(-tvar_95, color='purple', linestyle='--', label=f't-dist 95% VaR: {tvar_95:.4f}')
    plt.axvline(-tvar_99, color='yellow', linestyle='--', label=f't-dist 99% VaR: {tvar_99:.4f}')
    plt.title('Parametric VaR')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    sim_returns = np.random.normal(returns.mean(), returns.std(), 10000)
    plt.hist(sim_returns, bins=50, alpha=0.7, color='orange', label='Simulated Returns')
    plt.axvline(-mc_var_95, color='red', linestyle='--', label=f'95% VaR: {mc_var_95:.4f}')
    plt.axvline(-mc_var_99, color='orange', linestyle='--', label=f'99% VaR: {mc_var_99:.4f}')
    plt.title('Monte Carlo VaR')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('var_plots.png')
    plt.close()
