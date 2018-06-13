from math import cos
import numpy as np

def f(x):
    return x - cos(x)

a = f(0)
b = f(1)
n = 10
m = np.zeros(n)
for i in range(1, n + 1):
    m[i - 1] = f((b - a)/2.)
    if a*m[i - 1] < 0:
        b = m[i - 1]
    if b*m[i - 1] < 0:
        a = m[i - 1]
    print m[i - 1]
