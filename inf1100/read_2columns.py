# my version of reading two columns

x = []
y = []
with open('xy.dat','r') as infile:
    for line in infile:
        a = line.split()
        for i in range(len(a)):
            x.append(a[0])
            y.append(a[1])
import matplotlib.pyplot as plt

# two dimensional array plot: (can read n columns)

import numpy as np

data = np.loadtxt('xy.dat', dtype=np.float)
x_ = data[:,0]
y_ = data[:,1]

plt.plot(x_,y_,'ro')
plt.plot(x,y)
plt.show()
