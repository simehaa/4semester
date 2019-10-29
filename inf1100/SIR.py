import ODESolver
import numpy as np
import matplotlib.pyplot as plt

# differnetial solving using RungeKutta4 from ODESolver
n = 121

def f(u,t,beta=0.0005,v=0.1):
    S, I, R = u
    return [-beta*S*I, beta*S*I- v*I, v*I]


def solve():
    RK4 = ODESolver.RungeKutta4(f)
    RK4.set_initial_condition([1500,1,0])

    time_points = np.linspace(0,60,n)
    u, t = RK4.solve(time_points)

    tol = 1e-10
    S = u[:,0]; I = u[:,1]; R = u[:,2]
    for i in range(n):
        if abs(S[i] + I[i] + R[i]) - 1501 > tol: # 1501 is the population size
            return # function will be terminated, and nothing will be plotted

    plt.plot(t,S,'b--', label='RK4: susceptibles')
    plt.plot(t,I,'r--', label='RK4: infected')
    plt.plot(t,R,'g--', label='RK4: recovered')

solve()

# plot of S(t), I(t) and R(t)

def S(i,s,dt,beta=0.0005):
    return s - beta*s*i*dt

def I(i,s,dt,beta=0.0005,v=0.1):
    return i + beta*s*i*dt - v*i*dt

def R(r,i,dt,v=0.1):
    return r + v*i*dt

def plot():
    dt = 0.5
    t = np.linspace(0,60,n)
    s = np.zeros(n); s[0] = 1500 # susceptible people
    i = np.zeros(n); i[0] = 1 # one infected person
    r = np.zeros(n) # r[0] = 0
    tol = 1e-10
    for k in range(n - 1):
        s[k + 1] = S(i[k],s[k],dt) # S(t + dt)
        i[k + 1] = I(i[k],s[k],dt) # I(t + dt)
        r[k + 1] = R(r[k],i[k],dt) # R(t + dt)

    plt.plot(t,s,'b-', label='S(t)')
    plt.plot(t,i,'r-', label='I(t)')
    plt.plot(t,r,'g-', label='R(t)')

plot()

plt.title('SIR model for a disease')
plt.legend(loc='best')
plt.xlabel('days')
plt.ylabel('people')
plt.grid(True)
plt.show()
