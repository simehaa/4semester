import numpy as np
import matplotlib.pyplot as plt

N = 500                       # enough for a smooth graph
time = np.linspace(-4,4,N)    # vectorized time array from -4 to 4
y = np.zeros(N)               # empty y array

def f(x,t):                   # the function
    return (np.exp(- (x - 3*t)**2)*np.sin(3*np.pi*(x - t))) # still generalized for t values

for i in range(len(time)):
    y[i] = f(time[i],0)       # calling the function with x-values, and t = 0

plt.plot(time,y,'k-')         # plot
plt.xlabel('x')
plt.ylabel('t')
plt.legend(['f(x,t)'],loc='best')
plt.title('plot of a wave packet')
plt.show()
