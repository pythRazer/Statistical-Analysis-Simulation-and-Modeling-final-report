import numpy as np
from matplotlib import pyplot as plt
import csv
from scipy.stats import weibull_min, invgauss, lognorm
import statsmodels.api as sm

data2 = []
# reading the data and append it into the list
with open('datafile2.csv') as csvfile2:
    reader = csv.reader(csvfile2)
    for row in reader:
        data2.append(float(row[0]))

# sort the data
data2 = np.sort(data2)

# number for parameters in the distribution for k value for AIC, each one has two parameters need to be estimated
num_params = 2

# Parameter estimates for generic data
shape1, loc1, scale1 = lognorm.fit(data2, floc=0)
mu1 = np.log(scale1)
sigma1 = shape1
y1 = lognorm.pdf(data2, s=sigma1, scale=np.exp(mu1))
log_likelihood1 = np.sum(np.log(y1))
print("Lognorm loglikelihood = " + str(log_likelihood1))
aic1= -2 * log_likelihood1 + 2 * num_params
print("Lognorm AIC = " + str(aic1))

# https://stackoverflow.com/questions/33070724/determine-weibull-parameters-from-data
# Parameter estimates for generic data
shape2, loc2, scale2 = weibull_min.fit(data2, floc=0)
c = shape2
b = scale2
y2 = weibull_min.pdf(data2, c, scale=b)
log_likelihood2 = np.sum(np.log(y2))
print("Weibull loglikelihood = " + str(log_likelihood2))
aic2= -2 * log_likelihood2 + 2 * num_params
print("Weibull AIC = " + str(aic2))

# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.invgauss.html
# the argument floc=0 to ensure that it does not treat the location as a free parameter
# Parameter estimates for generic data
shape3, loc3, scale3 = invgauss.fit(data2, floc=0)
mu3 = shape3
lambda3 = scale3
# fitting the data with the estimated parameters
y3 = invgauss.pdf(data2, mu3, scale=lambda3)
# calculate the log_likelihood
log_likelihood3 = np.sum(np.log(y3))
print("Wald loglikelihood = " + str(log_likelihood3))
# calculate AIC
aic3= -2 * log_likelihood3 + 2 * num_params
print("Wald AIC = " + str(aic3))

# ploting qq plot with 3 distributions, fit the parameters by calling distribution.fit()
sm.qqplot(data2, lognorm, fit=True, loc=0, line='45')
plt.title('Lognorm distribution qq plot')
sm.qqplot(data2, weibull_min, fit=True, loc=0, line='45')
plt.title('Weibull distribution qq plot')
sm.qqplot(data2, invgauss, fit=True, loc=0, line='45')
plt.title('Wald distribution qq plot')
plt.show()