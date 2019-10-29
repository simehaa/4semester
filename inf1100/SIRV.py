import ODESolver, numpy as np
import matplotlib.pyplot as plt
from SIR_class import ProblemSIR, SolverSIR

class Problem(ProblemSIR):
    def __init__(self, nu, beta, S0, I0, R0, T, V0, p):
        ProblemSIR.__init__(self, nu, beta, S0, I0, R0, T)
        self.V0, self.p = V0, p

    def __call__(self, u, t):
        S, I, R, V = u
        return [-self.beta(t)*S*I-self.p*S,
                self.beta(t)*S*I-self.nu(t)*I,
                self.nu(t)*I,
                self.p*S]

class Solver(SolverSIR):
    def __init__(self, problem, dt):
        SolverSIR.__init__(self, problem, dt)

    def solve(self, method=ODESolver.RungeKutta4):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0,self.problem.T,n + 1)
        u, self.t = self.solver.solve(t)
        self.S,self.I,self.R,self.V= u[:,0], u[:,1], u[:,2], u[:,3]

    def plot(self):
        plt.plot(self.t,self.S, 'b-', label='susceptibles')
        plt.plot(self.t,self.I, 'r-', label='infected')
        plt.plot(self.t,self.R, 'g-', label='recovered')
        plt.plot(self.t,self.V, 'k-', label='vaccinated')
        plt.grid(True)
        plt.title('SIR model of a disease, with handwash campaign at the 12th day')
        plt.xlabel('days')
        plt.ylabel('people')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    problem = Problem(0.1,0.0005,1500,1,0,60,0,0.1)
    disease = Solver(problem, 0.5)
    disease.solve()
    disease.plot()

# The plot showed that the vaccination had a tremendous effect on the disease
# it was highly effective
"""
[Command: python -u /home/simen/python/uke12/SIRV.py]
[Finished in 3.028s]
"""
