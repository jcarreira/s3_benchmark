import numpy as np
import matplotlib.pyplot as plt
import csv

plt.figure(figsize=(3,4))

samples = []

with open('bandwidth') as fin:
    csvReader = csv.reader(fin)
    for row in csvReader:
        samples.append(float(row[0]))

sorted_data = np.sort(samples)
print(sorted_data)
plt.plot(sorted_data, np.linspace(0,1,sorted_data.size))

plt.xlabel('Bandwidth MB/s')
plt.ylabel('CDF')

plt.show()

plt.savefig("bw_graph.png")
