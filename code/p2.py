import csv
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as ss
import math

data1 = []
data2 = []
data3 = []
data4 = []

with open('datafile1.csv') as csvfile1:
    reader = csv.reader(csvfile1)
    for row in reader:
        data1.append(float(row[0]))

with open('datafile2.csv') as csvfile2:
    reader = csv.reader(csvfile2)
    for row in reader:
        data2.append(float(row[0]))

with open('datafile3.csv') as csvfile3:
    reader = csv.reader(csvfile3)
    for row in reader:
        data3.append(float(row[0]))

with open('datafile4.csv') as csvfile4:
    reader = csv.reader(csvfile4)
    for row in reader:
        data4.append(float(row[0])) 


data1 = np.sort(data1)
sigma1 = np.std(data1)
mu1 = np.mean(data1)

data2 = np.sort(data2)
sigma2 = np.std(data2)
mu2 = np.mean(data2)

data3 = np.sort(data3)
sigma3 = np.std(data3)
mu3 = np.mean(data3)

data4 = np.sort(data4)
sigma4 = np.std(data4)
mu4 = np.mean(data4)

print(sigma1)
print(mu1)

print(sigma2)
print(mu2)

print(sigma3)
print(mu3)

print(sigma4)
print(mu4)
# sigma = 0.1
# mu = 0.25
fig, ax = plt.subplots(1, 1)

# lognorm.pdf(x, s) = 1 / (s*x*sqrt(2*pi)) * exp(-1/2*(log(x)/s)**2)
# s = mu
# frozen_lognorm = ss.lognorm(data1, )
# y = ss.lognorm.pdf(data_to_use, sigma, 0, np.exp(mu))

# x = np.linspace(0,6,200)
x = np.linspace(0,4, 1000)
y1 = ss.lognorm.pdf(x=x, s=sigma1, scale=np.exp(mu1))
y2 = ss.lognorm.pdf(x=x, s=sigma2, scale=np.exp(mu2))
y3 = ss.lognorm.pdf(x=x, s=sigma3, scale=np.exp(mu3))
y4 = ss.lognorm.pdf(x=x, s=sigma4, scale=np.exp(mu4))

ax.plot(x, y1, label = '1: mu = ' + str(mu1) + ", sigma = " + str(sigma1))
ax.plot(x, y2, label = '2: mu = ' + str(mu2) + ", sigma = " + str(sigma2))
ax.plot(x, y3, label = '3: mu = ' + str(mu3) + ", sigma = " + str(sigma3))
ax.plot(x, y4, label = '4: mu = ' + str(mu4) + ", sigma = " + str(sigma4))

# x1 = np.linspace(ss.lognorm.ppf(0.01, sigma1),ss.lognorm.ppf(0.99, sigma1), 100)
# x2 = np.linspace(ss.lognorm.ppf(0.01, sigma2),ss.lognorm.ppf(0.99, sigma2), 100)
# x3 = np.linspace(ss.lognorm.ppf(0.01, sigma3),ss.lognorm.ppf(0.99, sigma3), 100)
# x4 = np.linspace(ss.lognorm.ppf(0.01, sigma4),ss.lognorm.ppf(0.99, sigma4), 100)
# y1 = ss.lognorm.pdf(x=x1, s=sigma1, scale=np.exp(mu1))
# y2 = ss.lognorm.pdf(x=x2, s=sigma2, scale=np.exp(mu2))
# y3 = ss.lognorm.pdf(x=x3, s=sigma3, scale=np.exp(mu3))
# y4 = ss.lognorm.pdf(x=x4, s=sigma4, scale=np.exp(mu4))
# ax.plot(x1, y1, label = '1: mu = ' + str(mu1) + ", sigma = " + str(sigma1))
# ax.plot(x2, y2, label = '2: mu = ' + str(mu2) + ", sigma = " + str(sigma2))
# ax.plot(x3, y3, label = '3: mu = ' + str(mu3) + ", sigma = " + str(sigma3))
# ax.plot(x4, y4, label = '4: mu = ' + str(mu4) + ", sigma = " + str(sigma4))
ax.legend(loc='best', frameon=False)

# r = ss.lognorm.rvs(sigma1, size=1000)
# ax.hist(data1)
# ax.hist(data2, bins=50)
# ax.hist(data3, bins=50)
# ax.hist(data4, bins=50)

plt.show()

# plt.title("Data1")
# plt.title("Data2")
# plt.title("Data3")
# plt.title("Data4")
# plt.show()

