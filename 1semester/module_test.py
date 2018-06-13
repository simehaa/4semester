from math import pi, factorial
import numpy as np
import matplotlib.pyplot as plt
import sys

try:
    x = float(sys.argv[1])
    N = int(sys.argv[2])
except IndexError:
    print 'two numbers, where the last is and integer must be provided in the command line'
    sys.exit(1)
except ValueError:
    print 'could not convert command line arguments to float and int'
    sys.exit(1)

def K(x,N):
    s = 0
    for k in range(N + 1):
        s += (-1)**k*x**(2*k + 1)/factorial(2*k + 1)
    return s

x = np.linspace(0,2*pi,100)
y = np.zeros(100)

for i in range(100):
    y[i] = K(x[i],N)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('K')
plt.legend(['Approximation function of sin(x) with N = %i' % N], loc=2)
#plt.savefig('plot_of_K.png')
plt.show()
