import numpy as np

def VaR(r, confidence, principal=1):

    # Calculate percentile
    percentile = np.percentile(r, (1-confidence)*100)

    # VaR is positive loss value
    out = abs(percentile) * principal

    return out
