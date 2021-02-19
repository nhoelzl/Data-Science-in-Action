#!/usr/bin/env python3
"""
Univariate Linear Regression

"""

__author__ = "Nicole Hölzl"
__version__ = "0.1.0"
__license__ = "MIT"

# --- IMPORTS ---
import logging

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# set log level to DEBUG
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

# --- SAMPLE DATA ---
X = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# --- FIT MODEL ---
model = LinearRegression().fit(X, y)

# --- SCORE ---
r_sq = model.score(X, y)
logging.debug("%s: %f" % ('coefficient of determination: ', r_sq))

# --- INTERCEPT & COEF ---
logging.debug("%s: %f" % ('intercept: ', model.intercept_))
logging.debug("%s: %f" % ('slope: ', model.coef_))

y_pred = model.intercept_ + model.coef_ * X
print('predicted response:', y_pred, sep='\n')

