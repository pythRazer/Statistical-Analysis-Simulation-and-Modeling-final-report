import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as ss
from scipy.stats import lognorm

# Lognormal Distribution from scipy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html
# Wikipedia: https://en.wikipedia.org/wiki/Log-normal_distribution

mu1 = 5
mu2 = 5.5
sigma1 = 0.5
sigma2 = 1
sigma3 = 1.5

# show from 0 to 400
x = np.linspace(0,400, 1000)

# lognormal pdf function plot from scipy, assigning sigma and mu

# A common parametrization for a lognormal random variable Y is 
# in terms of the mean, mu, and standard deviation, sigma, of the
# unique normally distributed random variable X such that exp(X) = Y. 
# This parametrization corresponds to setting s = sigma and scale = exp(mu).
y1 = lognorm.pdf(x=x, s=sigma1, scale=np.exp(mu1))
y2 = lognorm.pdf(x=x, s=sigma2, scale=np.exp(mu1))
y3 = lognorm.pdf(x=x, s=sigma3, scale=np.exp(mu1))
y4 = lognorm.pdf(x=x, s=sigma3, scale=np.exp(mu2))

fig, ax = plt.subplots(1, 1)
ax.plot(x, y1, label = '1: $\mu$ = ' + str(mu1) + ", $\sigma$ = " + str(sigma1))
ax.plot(x, y2, label = '2: $\mu$ = ' + str(mu1) + ", $\sigma$ = " + str(sigma2))
ax.plot(x, y3, label = '3: $\mu$ = ' + str(mu1) + ", $\sigma$ = " + str(sigma3))
ax.plot(x, y4, label = '4: $\mu$ = ' + str(mu2) + ", $\sigma$ = " + str(sigma1))

ax.legend(loc='best', frameon=False)
plt.title("Lognormal Distribution PDF plot")
plt.show()

