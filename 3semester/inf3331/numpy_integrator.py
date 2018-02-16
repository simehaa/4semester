import numpy as np
from time import clock

def numpy_integrator(f,a,b,N):
    x = np.linspace(a,b,int(N))
    return np.sum(f(x))*(b-a)/float(N)

def f(x):
    return x**2

if __name__ == '__main__':
    t0 = clock()
    numpy_integrator(f,0,1,1e7)
    print(clock()-t0)

"""
runfile('C:/Users/simen/INF3331-Simehaa/assignment4/numpy_integrator.py', wdir='C:/Users/simen/INF3331-Simehaa/assignment4')
0.11925615900827324
"""