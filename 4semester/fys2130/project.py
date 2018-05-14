import numpy as np
import matplotlib.pyplot as plt

class differential:
    """Solver of differential equations
    using RK4. diffEq should be a function with the
    differential equation that returns acceleration.
    All variables inside diffEq must be global"""
    def __init__(self, diffEq, plot_str, dt=0.01, T=20, x0=0, v0=0):
        if callable(diffEq):
            self.diffEq = diffEq
        else:
            raise TypeError('diffEq must be a callable function')
        self.dt = float(dt)
        self.T = T
        self.n = int(self.T/self.dt) + 1
        self.x = np.zeros(self.n)
        self.v = np.zeros(self.n)
        self.t = np.linspace(0,self.T,self.n)
        self.x[0] = x0
        self.v[0] = v0
        self.plot_str = plot_str

    def solve(self):
        """ method that uses RK4 and diffEq
        to solve the entire motion"""
        for i in range(self.n - 1):
            self.x[i + 1],self.v[i + 1] = self.RK4(self.x[i],self.v[i],self.t[i])
        return self.x, self.v, self.t

    def RK4(self,xStart,vStart,tStart):
        """ Runge-Kutta method of 4th order"""
        a1 = self.diffEq(xStart,vStart,tStart)
        v1 = vStart
        xHalf1 = xStart + v1 * self.dt/2.0
        vHalf1 = vStart + a1 * self.dt/2.0
        a2 = self.diffEq(xHalf1,vHalf1,tStart+self.dt/2.0)
        v2 = vHalf1
        xHalf2 = xStart + v2 * self.dt/2.0
        vHalf2 = vStart + a2 * self.dt/2.0
        a3 = self.diffEq(xHalf2,vHalf2,tStart+self.dt/2.0)
        v3 = vHalf2
        xEnd = xStart + v3 * self.dt
        vEnd = vStart + a3 * self.dt
        a4 = self.diffEq(xEnd,vEnd,tStart + self.dt)
        v4 = vEnd
        aMiddle = 1.0/6.0 * (a1 + 2*a2 + 2*a3 + a4)
        vMiddle = 1.0/6.0 * (v1 + 2*v2 + 2*v3 + v4)
        xEnd = xStart + vMiddle * self.dt
        vEnd = vStart + aMiddle * self.dt
        return xEnd, vEnd

    def plot(self):
        """ plots phase space of motion,
        after solve() method is used"""
        plt.title(self.plot_str)
        plt.plot(self.x,self.v)
        plt.xlabel('position [m]')
        plt.ylabel('velocity [m/s]')
        plt.grid()
        plt.show()


if __name__ == '__main__':
    def diffEq(xNow,vNow,tNow):
        return - k*xNow/m
    oppgave1 = differential(diffEq,r'$m\ddot{x}(t) + kx(t) = 0$',x0=1.0)
    m = 0.500
    k = 1.0
    oppgave1.solve()
    oppgave1.plot()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project.py]
[Finished in 2.405s]
"""
