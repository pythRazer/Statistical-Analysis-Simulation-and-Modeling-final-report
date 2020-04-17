# The “best” model produces the lowest IC 

# # calculate aic
# def calculate_aic(n, mse, num_params):
# 	aic = n * log(mse) + 2 * num_params
# 	return aic
# import libraries
import numpy as np, pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

# import scipy.stats as statsimport pymc3 as pm3
import numdifftools as ndt
import statsmodels.api as sm
from statsmodels.base.model import GenericLikelihoodModel
import csv
import statsmodels.api as sm
from matplotlib import pyplot as plt

data2 = []

with open('datafile2.csv') as csvfile2:
    reader = csv.reader(csvfile2)
    for row in reader:
        data2.append(float(row[0]))
data2 = np.sort(data2)
# sm.qqplot(data2, dist="lognorm")
sm.qqplot(data2, dist='lognorm')
plt.show()