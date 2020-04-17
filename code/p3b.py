# import libraries
import numpy as np, pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import weibull_min
import csv

data2 = []

with open('datafile2.csv') as csvfile2:
    reader = csv.reader(csvfile2)
    for row in reader:
        data2.append(float(row[0]))
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
plt.show()