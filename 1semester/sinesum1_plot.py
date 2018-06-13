import numpy as np
import matplotlib.pyplot as plt

N = 500
T = 2*np.pi
x = np.linspace(0,T,N)             # x array with 500 points
y1 = np.zeros(N)                   # empty y arrays
y3 = np.zeros(N)
y20 = np.zeros(N)
y200 = np.zeros(N)
yexact = np.zeros(N)

def f(t):              # exact function
    if 0 < t < T/2.:   # avoiding integer division
        return 1
    elif abs(t - T/2.) < 1e-16:
        return 0
    elif T/2. < t < 1:
        return -1

def S(t, n):           # approximation function with Fourier series
    s = 0
    for i in range(1, n + 1):
        s += 1./(2*i - 1)*np.sin(2*(2*i - 1)*np.pi*t/T)
    s *= 4/np.pi
    return s

for i in range(N):
    yexact[i] = f(x[i])      # giving yexact values from exact function
    y200[i] = S(x[i],200)    # giving apporximation y's values from apporximation function
    y20[i] = S(x[i],20)
    y3[i] = S(x[i],3)
    y1[i] = S(x[i],1)

plt.plot(x,yexact, label='exact')    # all the plots with labels
plt.plot(x,y1, label='n = 1')
plt.plot(x,y3, label='n = 3')
plt.plot(x,y20, label='n = 20')
plt.plot(x,y200, label='n = 200')
plt.title('Approximation with Fourier series')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-0.03, 6.3, -1.5, 1.5])    # appropriate axis ranges
plt.legend(loc='best')               # legend box to show which graph is which
plt.show()
