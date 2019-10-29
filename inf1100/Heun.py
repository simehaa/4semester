import numpy as np
from ODESolver import ODESolver

class Heun(ODESolver):
    def advance(self):
        u,f,k,t = self.u,self.f,self.k,self.t
        dt = t[k+1] - t[k]
        ustar = u[k] + dt*f(u[k],t[k])
        return (u[k] + 0.5*dt*f(u[k],t[k]) + 0.5*dt*f(ustar,t[k+1]))

class IteratedMidpointMethod(ODESolver):
    def __init__(self, f, N=2):
        ODESolver.ODESolver.__init__(self, f)
        self.N = N

    def advance(self):
        u,f,k,t,N = self.u,self.f,self.k,self.t,self.N
        dt = t[k+1] - t[k]
        v = u[k]
        for i in range(1, N + 1):
            v = u[k] + 0.5*dt*(f(v, t[k + 1]) + f(u[k], t[k]))
        return v

def flu(S0,I0,b,q,T):
    def f(u,t):
        S,I,R = u
        return [-b(t)*S*I,
                b(t)*S*I - q*I,
                q*I]
    solver = Heun(f)
    solver.set_initial_condition([S0,I0,0])
    u, t = solver.solve(np.linspace(0,T,5*T + 1))
    return t, u[:,0], u[:,1], u[:,2]

t, S, I, R = flu(100,1,lambda t:0.01 if t < 5 else 0.002,1./7,40)
import matplotlib.pyplot as plt
plt.plot(t,S,t,I,t,R)
plt.legend(['S','I','R'])
plt.show()
