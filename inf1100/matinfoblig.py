import numpy as np

def differens(x_0, x_1, N):
    x = np.zeros(N + 1, float)
    x[0] = x_0
    x[1] = x_1
    for n in range(2, N + 1):
        x[n] = 2*x[n - 1] + x[n - 2]
        print "%3i: %9.3g" % (n, float(x[n]))

differens(1,1,100)

# terminalprint
"""
  2:         3
  3:         7
  4:        17
  5:        41
  6:        99
  7:       239
  8:       577
 ...
 98:  1.63e+37
 99:  3.92e+37
100:  9.47e+37
"""
