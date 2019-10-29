import numpy as np
import matplotlib.pyplot as plt

def f(n, I, p, x_0, c_0):  # variables: n - years, I - inflation rate, p - interest rate, x_0 - start fortune, c_0 start consumption
    x = np.zeros(n + 1)    # empty arrays
    c = np.zeros(n + 1)
    x[0] = x_0
    c[0] = c_0
    for i in range(n):             # the difference equations
        c[i + 1] = c[i]*(1 + I/100.)
        x[i + 1] = x[i]*(1 + p/100.) - c[i]
    return x                       # x is now independent from c, only need to return x

n = 42                             # setting n to 42 years
y = f(n,0.7,3,5000000,25000)       # some values for the function
x_graph = np.linspace(0,n,n + 1)   # the x array for the graph (the x array from the function is called to the y array)

plt.plot(x_graph,y, 'k-') # plot
plt.title('interest with fortune, consumption and inflation')
plt.xlabel('years')
plt.ylabel('millions')
plt.axis([0,n,0,2e7])
plt.legend(['fortune'])
plt.show()

"""
simen@simen-VirtualBox:~/python/uke7$
"""
