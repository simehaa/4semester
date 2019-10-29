import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,90,10)
illuminans = np.array([156,153,141,121,97,70,45,23,8,3])
t = np.linspace(0,np.pi/2,300)
y = np.cos(t)**2
t *= 180/np.pi


plt.plot(theta,illuminans,'bo',label='data')
plt.plot(t,156*y)
plt.legend()
plt.grid()
plt.show()
