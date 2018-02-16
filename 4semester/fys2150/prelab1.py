import numpy as np
import matplotlib.pyplot as plt


n = 250
A = 0.02
b = 5
fr = 1000.
w = 2*np.pi*fr
x = np.linspace(0,0.004,n)
noise = np.random.normal(0,0.2*A,n)
y = x*b + A*np.sin(x*w) + noise
plt.plot(x,y,'.')
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Volt [V]')
plt.show()


plt.hist(noise)
plt.title("Histogram")
plt.show()
