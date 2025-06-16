# Value at Risk (VaR) Modeling

This project implements three standard methods for calculating Value at Risk (VaR) on a portfolio of equities using historical market data:

- Historical Simulation  
- Parametric VaR (Normal and Student's t-distribution)  
- Monte Carlo Simulation  

The code is structured to be modular and reproducible in **Google Colab**, with data retrieved live from the Tiingo API.

---

## Project Structure

- `main_colab.ipynb` – Notebook for running the full VaR analysis pipeline in Google Colab
- `utils.py` – Handles data retrieval from Tiingo and preprocessing
- `var_methods.py` – Implements core VaR calculations (historical, parametric, Monte Carlo)
- `var_visuals.py` – Functions to visualize return distributions and VaR levels
- `config_template.py` – Example config file where users can add their own Tiingo API key


---

## API Access: Tiingo Setup

This project fetches historical stock data using the [Tiingo API](https://www.tiingo.com/). To run the code:

1. Create a free account at [tiingo.com](https://www.tiingo.com/)
2. Copy your API key from your profile page
3. Create a file named `config.py` in the root directory with the following contents:
```python
config = {
    'api_key': 'your_actual_tiingo_api_key',
    'session': True
}

