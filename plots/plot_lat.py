import numpy as np
import matplotlib.pyplot as plt
import csv

samples = []

with open('latency') as fin:
    csvReader = csv.reader(fin)
    for row in csvReader:
        samples.append(float(row[0])/1000)

#print(samples)
sorted_data = np.sort(samples)
print(sorted_data)
plt.plot(sorted_data, np.linspace(0,1,sorted_data.size))

plt.xlabel('Latency ms')
plt.ylabel('CDF')

plt.show()
