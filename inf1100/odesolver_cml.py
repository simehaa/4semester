import ODESolver, sys
import numpy as np, matplotlib.pyplot as plt
from scitools.std import StringFunction

try:
    f = StringFunction(sys.argv[1])
    U0 = float(sys.argv[2])
    dt = float(sys.argv[3])
    T = float(sys.argv[4])
except ValueError:
    print 'cml should contain str(f), float(U0), float(dt) and float(T)'
    sys.exit(1)
except IndexError:
    print 'cml should contain 4 arguments'
    sys.exit(1)

def f(u, t):
    return f

n = int(T/dt + 1)
FE = ODESolver.ForwardEuler(f)
FE.set_initial_condition(U0)
u, t = FE.solve(time_points = np.linspace(0,T,n))
plt.plot(t,u)
plt.show()
