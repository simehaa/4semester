import sys
"""
try:
    x = float(sys.argv[1])
    N = int(sys.argv[2])
except IndexError:
    print 'not enough information, please provide two values in the command line\n\
first a float, then an integer'
    sys.exit(1)
except ValueError:
    print 'you must provide a float and an integer, you typed', \
    type(eval(sys.argv[1])), 'and', type(eval(sys.argv[2]))
    sys.exit(1)

from math import pi, factorial

def K(x, N):
    s = 0
    for k in range(N + 1):
        s += (-1)**k*(x**(2*k + 1))/(factorial(2*k + 1))
    return s

from numpy import linspace
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt
import numpy as np

n = 100
x_min = 0
x_max = N

x = linspace(x_min, x_max, n+1)

plot (x, K(x, N))
show
plt.xlabel("N")
plt.ylabel("sum")
plt.title("Sum Function")
show()
"""
from math import sqrt
y = eval(raw_input(""))
G = (sqrt(5)/5)*(((1 + sqrt(5))/2)**y + ((1 - sqrt(5))/2)**y)
print G
