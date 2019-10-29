#                    u' = f(u,t)

#                u'(tk) = f(u(tk),tk)           (find right side for tangent, use tangent to get next point: repeat)

#         u'(tk) approx = (u(tk+1)-u(tk)) / dt

#  (u(tk+1)-u(tk)) / dt = f(u(tk),tk)




# u[k+1] = u[k] + dt*f(uk,tk)       # regular difference equation with Euler's method

# algorithm

import numpy as np
import matplotlib.pyplot as plt

def f(u,t):
    return u # u'

n = 50                   # number of values
T = 1                    # stop on x-axis
dt = (T/float(n))        # steplength
t = np.zeros(n + 1)
u = np.zeros(n + 1)
u[0] = 1
t[0] = 0

for k in range(n):
    t[k + 1] = t[k] + dt
    u[k + 1] = u[k] + dt*f(u[k], t[k])

plt.plot(t, u)
plt.show()


# Euler's method class

class ForwardEuler_v1:
