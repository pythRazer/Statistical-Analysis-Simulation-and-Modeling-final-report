# https://medium.com/@rrfd/what-is-maximum-likelihood-estimation-examples-in-python-791153818030
# import libraries
import numpy as np
from matplotlib import pyplot as plt
import csv
from scipy.stats import lognorm

data2 = []

with open('datafile2.csv') as csvfile2:
    reader = csv.reader(csvfile2)
    for row in reader:
        data2.append(float(row[0]))

plt.figure()
_ = plt.hist(data2,  bins=100)

# Parameter estimates for generic data
# the argument floc=0 to ensure that it does not treat the location as a free parameter
shape1, loc1, scale1 = lognorm.fit(data2, floc=0)
mu1 = np.log(scale1)
sigma1 = shape1
print("Estimated mu = " + str(mu1))
print("Estimated sigma = " + str(sigma1))
# 0.95 is the alpha value, which specifies a 95 percentile point, as the corresponding 1.96 standard deviations of the mean is given in the formula. 
ci1 = lognorm.interval(0.95, s=sigma1, loc=loc1, scale=scale1)
print("Lognorm function CI = " + str(ci1))
# confidence interval left line
one_x12, one_y12 = [ci1[0],ci1[0]], [0, 20]
# confidence interval right line
two_x12, two_y12 = [ci1[1],ci1[1]], [0, 20]

plt.plot(one_x12, one_y12, two_x12, two_y12, marker = 'o')
plt.title("Lognormal distribution confidence interval")
plt.show()
