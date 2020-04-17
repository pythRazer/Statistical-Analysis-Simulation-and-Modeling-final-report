import numpy as np, pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import invgauss
import csv

data2 = []
with open('datafile2.csv') as csvfile2:
    reader = csv.reader(csvfile2)
    for row in reader:
        data2.append(float(row[0]))
plt.figure()
_ = plt.hist(data2,  bins=100)

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

