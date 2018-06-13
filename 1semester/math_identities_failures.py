import random
from math import exp, log

# a)

def power3_identity(A=-100, B=100, n=1000):
    s = 0
    for i in range(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        if (a*b)**3 != a**3*b**3:
            s += 1
    return 'Out of %i random calculations, %i fails was detected' % (n, s)

print power3_identity()

# b)

def equal(expr1, expr2, A=-100, B=100, n=1000):
    s = float(0)
    for i in range(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        try:
            rs0 = eval(expr1)
        except ValueError:
            rs0 = None
        try:
            rs1 = eval(expr2)
        except ValueError:
            rs1 = None
        if rs0 != rs1:
            s += 1
    frac = s/n*100
    return '%f percent of the calulations failed' % frac

def testfunc():
    print equal('a**3*b**3','(a*b)**3')
    print equal('exp(a+b)','exp(a)*exp(b)')
    print equal('log(a**b)','b*log(a)')

testfunc()
