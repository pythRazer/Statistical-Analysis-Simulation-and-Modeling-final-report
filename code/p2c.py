import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import invgauss
# Wald Distribution from scipy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invgauss.html
# Wikipedia: https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution
mu1 = 1
mu2 = 3
l1 = 1
l2 = 3
l3 = 0.2

x = np.linspace(0, 5, 1000)

# scale = lambda
y1 = invgauss.pdf(x, mu1, scale=l1)
y2 = invgauss.pdf(x, mu1, scale=l2)
y3 = invgauss.pdf(x, mu1, scale=l3)
y4 = invgauss.pdf(x, mu2, scale=l1)
y5 = invgauss.pdf(x, mu2, scale=l3)

fig, ax = plt.subplots(1, 1)

ax.plot(x, y1, label = '1: $\mu$ = ' + str(mu1) + ", $\lambda$ = " + str(l1))
ax.plot(x, y2, label = '2: $\mu$ = ' + str(mu1) + ", $\lambda$ = " + str(l2))
ax.plot(x, y3, label = '3: $\mu$ = ' + str(mu1) + ", $\lambda$ = " + str(l3))
ax.plot(x, y4, label = '4: $\mu$ = ' + str(mu2) + ", $\lambda$ = " + str(l1))
ax.plot(x, y5, 'k', label = '5: $\mu$ = ' + str(mu2) + ", $\lambda$ = " + str(l3))

ax.legend(loc='best', frameon=False)
plt.title("Wald Distribution PDF plot")
plt.show()
