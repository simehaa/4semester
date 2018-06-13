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
y = h/2.   # half steplength for midpoint method
t = np.linspace(a, b, n + 1) # t values
texact = np.linspace(a, b, N + 1) # exact function t values
m = np.zeros(n + 1)  # Euler's midpoint method function values
xexact = np.zeros(N + 1) # exact function values

for i in range(n):
    m[i + 1] =  m[i] + h*f(t[i] + h,m[i] + y*f(t[i],m[i])) # founding the next point (explanation in comments under)
                                           # f(t[i],m[i]) = initial slope
                                         # y*f(t[i],m[i]) = delta m from midpoint
                                  # m[i] + y*f(t[i],m[i]) = m value at midpoint
                       # f(...) = slope at midpoint
                     # h*f(...) = delta m from next point (m[i + 1] = m[i] + dm)

for i in range(N):
    xexact[i + 1] = f2(texact[i + 1]) # calling the exact function

plt.plot(t,m,'b-',label='Eulers midpoint method')
plt.plot(texact,xexact,'k-',label='exact')
plt.title('Eulers midpoint method')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(loc='best')
plt.show()
