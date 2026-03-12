import numpy as np

def ES(losses, confidence=.95, VaR=None):

    if VaR is None:
        VaR = np.percentile(losses, confidence*100)

    # losses exceeding VaR
    tail_losses = losses[losses >= VaR]

    # Expected Shortfall
    es_value = np.mean(tail_losses)

    return es_value
