import ODESolver, numpy as np
import matplotlib.pyplot as plt

class ProblemSIR:
    def __init__(self, nu, beta, S0, I0, R0, T):
        self.beta = beta
        self.nu = nu
        if isinstance(nu, (float,int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu
        if isinstance(beta, (float,int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        self.S0, self.I0, self.R0, self.T = S0, I0, R0, T

    def __call__(self, u, t):
        S, I, R = u
        return [-self.beta(t)*S*I,
                self.beta(t)*S*I-self.nu(t)*I,
                self.nu(t)*I]

class SolverSIR:
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ODESolver.RungeKutta4):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0,self.problem.T,n + 1)
        u, self.t = self.solver.solve(t)
        self.S,self.I,self.R = u[:,0], u[:,1], u[:,2]

    def plot(self):
        plt.plot(self.t,self.S, 'b-', label='susceptibles')
        plt.plot(self.t,self.I, 'r-', label='infected')
        plt.plot(self.t,self.R, 'g-', label='recovered')
        plt.grid(True)
        plt.title('SIR model of a disease, with handwash campaign at the 12th day')
        plt.xlabel('days')
        plt.ylabel('people')
        plt.legend()
        plt.show()

    def maximum(self):
        return int(round(max(self.I)))

def handwash_effect():
    problem_handwash = ProblemSIR(beta=lambda t: 0.0005 if t <= 12 else 0.0001, # beta is 0.0005 until day 12, then 0.0001
                     nu=0.1, S0=1500, I0=1, R0=0, T=60)
    problem = ProblemSIR(beta=0.0005, nu=0.1, S0=1500, I0=1, R0=0, T=60)
    handwash = SolverSIR(problem_handwash, 0.5)
    disease = SolverSIR(problem, 0.5)
    handwash.solve()
    disease.solve()

    return 'when beta was 0.0005, at the most %i people were infected \
    \nwith the handwash campaign, there were %i people infected at the most ' % (disease.maximum(), handwash.maximum())

if __name__ == "__main__":
    print handwash_effect()
