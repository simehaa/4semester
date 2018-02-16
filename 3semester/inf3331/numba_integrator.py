from numba import jit
from time import clock
from integrator import integrate, f

t0 = clock()
integrate(f,0,1,1e7)
time0 = clock() - t0

@jit
def numba_integrate(f,a,b,N):
    dx = (b-a)/float(N)
    s = 0
    for i in range(int(N)):
        s += f(i*dx)
    return s*dx

t1 = clock()
numba_integrate(f,0,1,1e7)
time1 = clock() - t1

print(time0)
print(time1)

"""
runfile('C:/Users/simen/INF3331-Simehaa/assignment4/numba_integrator.py', wdir='C:/Users/simen/INF3331-Simehaa/assignment4')
Reloaded modules: integrator
2.9856839809117446
3.8899518532693946
"""