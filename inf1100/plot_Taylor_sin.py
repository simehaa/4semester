import matplotlib.pyplot as plt
import math
import numpy as np

N = 100
x = np.linspace(0,4*np.pi,N) # x array
y = np.zeros(N)              # empty y array

def S(x, n): # Taylor function
    for k in range(N):
        m = 0
        for i in range(n + 1):  # the sum was from 0 up to and including n
            m += (-1)**i*float(x[k]**(2*i + 1))/(math.factorial(2*i + 1))
        y[k] = m  # filling y array with values from tha Taylor formula
    return y

plt.title('Taylor polynoms of sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,np.sin(x),label='sin(x)')   # all the plots
plt.plot(x, S(x, 1),label='S(x;1)')
plt.plot(x, S(x, 2),label='S(x;2)')
plt.plot(x, S(x, 3),label='S(x;3)')
plt.plot(x, S(x, 6),label='S(x;6)')
plt.plot(x, S(x, 12),label='S(x;12)')
plt.legend(loc='best')
plt.axis([0.0, 13, -3.5, 3.5])
plt.show()

"""
simen@simen-VirtualBox:~/python/uke7$ python plot_Taylor_sin.py

"""
