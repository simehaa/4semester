import matplotlib.pyplot as plt
import math
import numpy as np

n = 100
x = np.linspace(0,2*np.pi,n)
y = np.zeros(n)
N = 3

# print x, y

def f(N):
    for k in range(n):
        m = 0
        for i in range(N + 1):
            m += (-1)**i*float(x[k]**(2*i + 1))/(math.factorial(2*i + 1))
        y[k] = m
    return y

plt.plot(x,f(N),x,np.sin(x))
plt.legend(['taylor','exact'],loc='best')
plt.title('Taylor function for sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
