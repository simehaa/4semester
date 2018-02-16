import numpy as np
import matplotlib.pyplot as plt

data1 = (1.51,1.57,1.59,1.58,1.55,1.58,1.52,1.6,1.59,1.62,1.5,1.86)
run1 = np.asarray(data1)
norm1 = run1/float(np.linalg.norm(run1))
# x = np.linspace(0,11,12)

mu = np.mean(norm1)
sigma = np.std(norm1)
mu = np.zeros(12).fill(mu)
x = mu + float(sigma)*(run1 - mu)
plt.hist(x,bins=12)
plt.show()
