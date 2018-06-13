import numpy as np
import matplotlib.pyplot as plt
import ODESolver

def SIR(S0,I0,sigma,mu,b,q,d,T):
    time_points = np.linspace(0,T,10*T + 1)
    def f(u,t):
        S,I,R = u
        return [sigma(t) - b(t)*S*I + d*R - mu*S,
                b(t)*S*I - q*I - mu*I,
                q*I - d*R - mu*R]
    solver = ODESolver.RungeKutta4(f)
    ic = [S0,I0,0]
    solver.set_initial_condition(ic)
    u, t = solver.solve(time_points)
    return t, u[:,0], u[:,1], u[:,2]

t, S, I, R = SIR(1000,2,lambda t: 10,1./100,lambda t: 1./1000,1./7,1./100,40)
plt.plot(t,S,t,I,t,R)
plt.legend(['S','I','R'])
plt.show()
