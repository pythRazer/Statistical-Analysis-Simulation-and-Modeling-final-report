# https://medium.com/@rrfd/what-is-maximum-likelihood-estimation-examples-in-python-791153818030
# import libraries
import numpy as np
from matplotlib import pyplot as plt
import csv
from scipy.stats import lognorm, weibull_min, invgauss

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

plt.figure()
_ = plt.hist(data2,  bins=100)

# Parameter estimates for generic data
shape2, loc2, scale2= weibull_min.fit(data2, floc=0)
c = shape2
b = scale2
print("Estimated c = " + str(c))
print("Estimated b = " + str(b))
ci2 = weibull_min.interval(0.95, c, loc=loc2, scale=scale2)
print("Weibull CI = " + str(ci2))
print("----------------------")
# cnfidence interval left line
one_x12_, one_y12_ = [ci2[0],ci2[0]], [0, 20]
# cnfidence interval right line
two_x12_, two_y12_ = [ci2[1],ci2[1]], [0, 20]
plt.plot(one_x12_, one_y12_, two_x12_, two_y12_, marker = 'o')
plt.title("Weibull distribution confidence interval")

# Parameter estimates for generic data
# takes mu as a shape parameter, mu=shape 
shape3, loc3, scale3 = invgauss.fit(data2, floc=0)
mu3 = shape3
lambda3 = scale3
print(mu3,loc3, scale3)
print("Estimated mu = " + str(mu3))
print("Estimated lambda = " + str(lambda3))

ci3 = invgauss.interval(0.95, mu3, loc=loc3, scale=scale3)
print("Wald distribution CI = " + str(ci3))
print("Population mean = " + str(np.mean(data2)))
# cnfidence interval left line
one_x12__, one_y12__ = [ci3[0],ci3[0]], [0, 20]
# cnfidence interval right line
two_x12__, two_y12__ = [ci3[1],ci3[1]], [0, 20]
plt.plot(one_x12__, one_y12__, two_x12__, two_y12__, marker = 'o')
plt.title("Wald distribution confidence interval")
plt.show()
