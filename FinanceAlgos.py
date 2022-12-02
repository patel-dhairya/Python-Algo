import numpy as np
import math


def bsm_mce_european(s0, k, t, r: float, sigma: float, i = 10000) -> float:
    """
    Black-Scholes-Merton model Monte Carlo valuation of European call option

    :param s0: initial index level
    :param k: strike price
    :param t: time-to-maturity
    :param r: riskless short rate
    :param sigma: volatility
    :param i: simulation number
    :return: European Call option
    """
    random_numbers = np.random.standard_normal(i)
    st = s0*np.exp((r-0.5*sigma**2)*t + math.sqrt(t)*sigma*random_numbers)      # index values at maturity
    ht = np.maximum(st-k, 0)        # all inner values of option at maturity level
    c0 = math.exp(-r*t)*np.mean(ht)     # monte carlo estimator

    return "%5.3f" % c0


