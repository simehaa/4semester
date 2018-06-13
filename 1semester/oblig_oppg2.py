import numpy as np
import matplotlib.pyplot as plt

def f(t, x): # dx/dt
    return (1 - x**2)

def f2(t): # exact
    return (np.exp(2*t) - 1)/(np.exp(2*t) + 1)

n = 5      # amount of steps for Euler's method and midpoint method
a = 0      # start
b = 2      # stop
N = 50     # amount of values for exact solution
h = (b - a)/float(n) # steplength
t = np.linspace(a, b, n + 1) # t values
texact = np.linspace(a, b, N + 1) # exact function t values
x = np.zeros(n + 1)  # Euler's method function values
xexact = np.zeros(N + 1) # exact function values

for i in range(n):
    x[i + 1] =  x[i] + h*f(t[i],x[i])   # Euler's method, using the slope in the same point

for i in range(N):
    xexact[i + 1] = f2(texact[i + 1])   # calling the exact function

plt.plot(t,x,'r-',label='Eulers method')
plt.plot(texact,xexact,'k-',label='exact')
plt.title('Eulers Method')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(loc='best')
plt.show()
