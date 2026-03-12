import numpy as np
import pandas as pd

def YahooData2returns(YahooData=None, symbol='AAPL'):

    prices = YahooData['Close'][symbol]

    returns = prices.pct_change().dropna()

    returns = returns.values

    return returns
