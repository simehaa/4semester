import numpy as np
import matplotlib.pyplot as plt
p = 5
N = 4
index_set = range(50+1)
x = np.zeros(len(index_set))

x[0] = 100
for n in index_set[1:]:
    x[n] = x[n-1]*(1.0+p/100.0)

plt.plot(index_set, x)
plt.show()
