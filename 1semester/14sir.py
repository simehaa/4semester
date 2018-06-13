from RK2 import *
import numpy as np
import matplotlib.pyplot as plt

def flu(S0,I0,b,q,d,p,T):
    def f(u,t):
        S,I,R,V = u
        return [-b(t)*S*I - p(t)*S + d*R,
                b(t)*S*I - q*I,
                q*I - d*R,
                p(t)*S]
    solver = RK2(f)
    ic = [S0,I0,0,0]
    solver.set_initial_condition(ic)
    time_points = np.linspace(0,T,5*T + 1)
    u, t = solver.solve(time_points)
    return t, u[:,0], u[:,1], u[:,2], u[:,3]

t,S,I,R,V = flu(1000,2,lambda t: 0.001,1./7,0.01,\
                lambda t: 0 if t < 5 else 0.4,40)
plt.plot(t,S,t,I,t,R,t,V)
plt.legend(['S','I','R','V'])
plt.show()

def dump(filename, t, S, I, R, V):
    with open(filename,'w') as outfile:
        for i in range(len(t)):
            outfile.write('%9.4f %9.4f %9.4f %9.4f %9.4f \n' % (t[i],S[i],I[i],R[i],V[i]))
    outfile.close()

dump('data.dat', t, S, I, R, V)
