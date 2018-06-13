from SIZR import *
from scitools.std import PiecewiseConstant # using this to shorten
                                           # implementation of E, alpha and beta
problem = ProblemSIZR(S0=60,I0=0,Z0=1,R0=0,
                      E     = PiecewiseConstant(domain=[0,33],
                              data=[(0, 20), (4, 2), (28, 0)]),T=33,
                      alpha = PiecewiseConstant(domain=[0,33],
                              data=[(0, 0), (4, 0.0016), (28, 0.0006)]),
                      beta  = PiecewiseConstant(domain=[0,33],
                              data=[(0, 0.03), (4, 0.0012), (28, 0)]),
                      dS = lambda t: 0 if t < 28 else 0.0067,
                      dI = lambda t: 0.014 if 4 <= t <= 28 else 0,p=1)

solver = SolverSIZR(problem,0.1) # SIZR file is used to solve this task, as it accepts parameters as functions
solver.solve()
solver.plot()

"""
[Command: python -u /home/simen/python/Project/Night_of_the_Living_Dead.py]
[Finished in 2.313s]
"""
