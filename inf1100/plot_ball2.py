from numpy import *
from matplotlib.pyplot import *
import sys

v0_lst = sys.argv[1:]
g = 9.81
for v0 in v0_lst:
    v0 = float(v0)
    t = linspace(0, 2*v0/g, 100)
    y = v0*t - 0.5*g*t**2
    plot(t,y,label='v0=%g' %v0)

xlabel('time (s)')
ylabel('position (m)')
title('Ball Table')
legend()
show()
