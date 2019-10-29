# bruke ODESolver til aa loese et sett med difflikninger
import ODESolver
import numpy as np
import matplotlib.pyplot as plt

class Problem:
    def __init__(self, r, m, a, b, x0, y0, T):
        if isinstance(r, (int,float)):
            self.r = lambda t: r
        elif callable(r):
            self.r = r
        self.m, self.a, self.b = m, a, b
        self.x0, self.y0, self.T = x0, y0, T

    def __call__(self, u, t):
        x, y = u
        return [self.r(t)*x - self.a*x*y,
                -self.m*y + self.b*x*y]

class Solver:
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def __call__(self, method=ODESolver.RungeKutta4):
        self.solver = method(self.problem)
        ic = [self.problem.x0, self.problem.y0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0,self.problem.T,n + 1)
        u, self.t = self.solver.solve(t)
        self.x, self.y = u[:,0], u[:,1]

    def plot(self):
        plt.plot(self.t,self.x)
        plt.plot(self.t,self.y)
        plt.show()

prob = Problem(lambda t: 2 if 3 <= t <= 10 else 0.1, 1, 0.3, 0.2, 1, 1, 20)
solv = Solver(prob, 0.1)
solv()
solv.plot()
