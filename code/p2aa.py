import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as ss
import math

# Lognormal Distribution from scipy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html

def lognormal(x, mu, s):
    
    # return 1/(x*s*np.sqrt(2*math.pi)) * np.exp(-((math.log(x-mu))**2/(2*s**2)))
    return (1 / (x*s*np.sqrt(2*np.pi)) * np.exp(-(math.log(x)-mu)**2/(2*s**2)))
# mu1 = 5
# mu2 = 5.5
# sigma1 = 0.5
# sigma2 = 1.5

mu1 = 1
mu2 = 5.5
sigma1 = 0.5
sigma2 = 1.5

# show from 0 to 100
x = np.linspace(0,100, 1000)

# lognormal pdf function plot from scipy, assigning sigma and mu

# A common parametrization for a lognormal random variable Y is 
# in terms of the mean, mu, and standard deviation, sigma, of the
# unique normally distributed random variable X such that exp(X) = Y. 
# This parametrization corresponds to setting s = sigma and scale = exp(mu).
y1 = lognormal(x, mu1, sigma1)
y2 = lognormal(x, mu1, sigma2)
y3 = lognormal(x, mu2, sigma1)
y4 = lognormal(x, mu2, sigma2)
# lables
fig, ax = plt.subplots(1, 1)
ax.plot(x, y1, label = '1: mu = ' + str(mu1) + ", sigma = " + str(sigma1))
ax.plot(x, y2, label = '2: mu = ' + str(mu1) + ", sigma = " + str(sigma2))
ax.plot(x, y3, label = '3: mu = ' + str(mu2) + ", sigma = " + str(sigma1))
ax.plot(x, y4, label = '3: mu = ' + str(mu2) + ", sigma = " + str(sigma2))

ax.legend(loc='best', frameon=False)
plt.title("Lognormal Distribution PDF plot")
plt.show()

