import numpy as np

x = np.zeros(100)
x[0] = 1
x[1] = 1/5.

for i in range(2,99):
    x[i] = 11*x[i-1] - 2*x[i-2]
    print i, x[i]
