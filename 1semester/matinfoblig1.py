import numpy as np

def differens(x_0, x_1, N):
    x = np.zeros(N + 1, float)
    x[0] = x_0
    x[1] = x_1
    for n in range(2, N + 1):
        x[n] = 2*x[n - 1] + x[n - 2]
        print "%3i: %9.3g" % (n, float(x[n]))

differens(1,(1-np.sqrt(2)),100)

# terminalprint
"""
  2:     0.172
  3:   -0.0711
  4:    0.0294
  5:   -0.0122
  6:   0.00505
  7:  -0.00209
  8:  0.000867
 ...
 18:  1.29e-07
 19:  -5.4e-08
 20:  2.06e-08
 21: -1.29e-08
 22: -5.22e-09
 23: -2.33e-08
 24: -5.19e-08
 25: -1.27e-07
 ...
 98: -1.11e+21
 99: -2.68e+21
100: -6.48e+21
"""
