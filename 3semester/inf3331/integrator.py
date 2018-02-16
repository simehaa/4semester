import matplotlib.pyplot as plt
from time import clock

def f(x):
    return x**2

def integrate(f,a,b,N):
    dx = (b-a)/float(N)
    s = 0
    for i in range(int(N)):
        s += f(i*dx)
    return s*dx


if __name__ == '__main__':
    x = []
    y = []
    for i in range(1,51):
        N = i*200 + 1
        err = abs(1/3. - integrate(f,0,1,N))
        x.append(N)
        y.append(err)
    
    plt.plot(x,y)
    plt.xlabel('N values')
    plt.ylabel('error')
    plt.savefig('quadratic_error.png')
    t0 = clock()
    integrate(f,0,1,1e7)
    print(clock()-t0)
    
"""
runfile('C:/Users/simen/INF3331-Simehaa/assignment4/integrator.py', wdir='C:/Users/simen/INF3331-Simehaa/assignment4')
2.9270959027944627
"""
