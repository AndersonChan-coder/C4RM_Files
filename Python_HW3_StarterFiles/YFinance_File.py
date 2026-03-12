import numpy as np
import pandas as pd

def YahooData2returns(YahooData=None, symbol='AAPL'):

    # Extract close prices
    prices = YahooData['Close'][symbol]

    # Calculate returns
    returns = prices.pct_change().dropna()

    # Convert to numpy array
    returns = returns.values

    return returns
