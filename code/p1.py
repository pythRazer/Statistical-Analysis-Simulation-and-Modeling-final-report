import csv
from matplotlib import pyplot as plt

data1 = []
data2 = []
data3 = []
data4 = []

# Read the number in every row and add it into the list 
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

# building histogram with 100 bins
# hist1 = plt.hist(data1, bins=100)
# hist2 = plt.hist(data2, bins=100)
# hist3 = plt.hist(data3, bins=100)
hist4 = plt.hist(data4, bins=100)

# plt.title("Data1")
# plt.title("Data2")
# plt.title("Data3")
plt.title("Data4")
plt.show()

