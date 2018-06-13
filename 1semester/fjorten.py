def piecewise(x):
    if x < 5:
        return 0
    else:
        return 0.4

def test_piecewise():
    e0 = 0
    e1 = 0.4
    c0 = piecewise(4.9)
    c1 = piecewise(5.0)
    c2 = piecewise(5.1)
    tol = 1e-14
    success = abs(c0-e0) < tol and abs(c1-e1) < tol and abs(c2-e1) < tol
    assert success

test_piecewise()
# 3

def fac(N):
    from numpy import zeros
    y = zeros(N+1, int)
    y[0] = 1
    for i in range(1, N+1):
        y[i] = i*y[i-1]
    return y

def test_fac():
    expected0 = 1*2*3*4*5
    expected1 = 1*2*3*4*5*6*7
    a = fac(7)
    computed0 = a[5]
    computed1 = a[7]
    tol = 1e-14
    success = abs(expected0 - computed0) < tol and \
              abs(expected1 - computed1) < tol
    assert success

test_fac()

def polyeval(x, p):
    s = 0
    for key in p:
        s += p[key]*x**key
    return s

# print polyeval(2, {1:-1, 3:1})

def polyadd(p, q):
    r = p.copy()
    for key in q:
        if key in r:
            r[key] += q[key]
        else:
            r[key] = q[key]
    return r

# print polyadd({1:-1, 3:1}, {1:3, 2:2})

class Poly:
    def __init__(self,p):
        self.coeff = p

    def __call__(self,x):
        return sum(self.coeff[key]*x**key for key in self.coeff)

    def __add__(self, other):
        r = polyadd(self.coeff, other.coeff)
        return Poly(r)

    def diff(self):
        r = {}
        for key in self.coeff:
            if key != 0:
                r[key - 1] = key*self.coeff[key]
        return Poly(r)

p3 = Poly({1:2, 2:2, 3:1})
p4 = p3.diff()
print p4.__class__.__name__
print p4.coeff
