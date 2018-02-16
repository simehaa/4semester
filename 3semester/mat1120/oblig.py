from numpy import *
from numpy import matrix
import matplotlib.pyplot as plt
from numpy.linalg import inv


x= array([0.08, 0.12, 0.20, 0.38])
y= array([4.05, 4.15, 3.85, -0.22])
yt= matrix(y).transpose()

A= matrix([[1.0, 0.08, 0.0064], [1.0, 0.12, 0.0144], [1.0, 0.20, 0.040], [1.0, 0.38, 0.1444]]) # [1, x, x**2], designmatrisen
At= A.transpose() #A transponert
As= (At*A)
Ainv = inv(As) #A inverters
Aty = matmul(At,yt)
beta =  Ainv*(Aty) #minste kvadraters metode
beta = beta.transpose()
t = linspace(0, 0.4, 100)
def f(t,beta):
    return beta[0] + beta[1]*t + beta[2]*(t**2)

plt.plot(x, y, "ro",t, f(t,beta), "b")
plt.title("Oppgave 4a)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
