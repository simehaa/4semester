from project import differential

def diffEq(xNow,vNow,tNow):
    return - (b*vNow + k*xNow)/m

oppgave2 = differential(diffEq,r'$m\ddot{x}(t) + b\dot{x}(t) + kx(t) = 0$',dt=0.0001,x0=1.0)
m = 0.500
k = 1.0
b = 0.1
oppgave2.solve()
oppgave2.plot()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project2.py]
[Finished in 8.293s]
"""
