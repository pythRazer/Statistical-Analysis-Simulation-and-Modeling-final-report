import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import weibull_min

# Weibull Distribution from scipy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weibull_min.html
# Wikipedia: https://en.wikipedia.org/wiki/Weibull_distribution

# show from 0 to 5
x = np.linspace(0, 5, 1000)

c1 = 0.8
c2 = 1.5
c3 = 5
b1 = 1
b2 = 2


y1 = weibull_min.pdf(x, c1, scale=b1)
y2 = weibull_min.pdf(x, c2, scale=b1)
y3 = weibull_min.pdf(x, c2, scale=b2)
y4 = weibull_min.pdf(x, c3, scale=b1)

fig, ax = plt.subplots(1, 1)

ax.plot(x, y1, label = '1: $c$ = ' + str(c1) + ", $b$ = " + str(b1))
ax.plot(x, y2, label = '2: $c$ = ' + str(c2) + ", $b$ = " + str(b1))
ax.plot(x, y3, label = '3: $c$ = ' + str(c2) + ", $b$ = " + str(b2))
ax.plot(x, y4, label = '4: $c$ = ' + str(c3) + ", $b$ = " + str(b1))


ax.legend(loc='best', frameon=False)
plt.title("Weibull Distribution PDF plot")


plt.show()