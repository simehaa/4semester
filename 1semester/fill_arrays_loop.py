import numpy as np

n = 41              # number of values
x = np.zeros(n)     # empty array
y = np.zeros(n)     # empty array

def h(x):
    return (1/(np.sqrt(2*np.pi))*np.exp((-1./2)*x**2))

dx = 8.0/(n - 1)   # n - 1, because i don't need dx for the first value (x = - 4.0)
for i in range(n):
    x_value = - 4.0 + (i*dx)   # each x value from - 4.0 to + 4.0
    x[i] = x_value             # filling the array x with values
    y[i] = h(x_value)          # filling the array y with function values
    print "%5.1f | %5.2e" % (x[i], y[i])  # nicely formated table print

# created a table to check that the data made sense
"""
simen@simen-VirtualBox:~/python/uke5$ python fill_arrays_loop.py
 -4.0 | 1.34e-04
 -3.8 | 2.92e-04
 -3.6 | 6.12e-04
 -3.4 | 1.23e-03
 -3.2 | 2.38e-03
 -3.0 | 4.43e-03
 -2.8 | 7.92e-03
 -2.6 | 1.36e-02
 -2.4 | 2.24e-02
 -2.2 | 3.55e-02
 -2.0 | 5.40e-02
 -1.8 | 7.90e-02
 -1.6 | 1.11e-01
 -1.4 | 1.50e-01
 -1.2 | 1.94e-01
 -1.0 | 2.42e-01
 -0.8 | 2.90e-01
 -0.6 | 3.33e-01
 -0.4 | 3.68e-01
 -0.2 | 3.91e-01
  0.0 | 3.99e-01
  0.2 | 3.91e-01
  0.4 | 3.68e-01
  0.6 | 3.33e-01
  0.8 | 2.90e-01
  1.0 | 2.42e-01
  1.2 | 1.94e-01
  1.4 | 1.50e-01
  1.6 | 1.11e-01
  1.8 | 7.90e-02
  2.0 | 5.40e-02
  2.2 | 3.55e-02
  2.4 | 2.24e-02
  2.6 | 1.36e-02
  2.8 | 7.92e-03
  3.0 | 4.43e-03
  3.2 | 2.38e-03
  3.4 | 1.23e-03
  3.6 | 6.12e-04
  3.8 | 2.92e-04
  4.0 | 1.34e-04
"""
