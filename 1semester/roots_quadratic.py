print 'Quadratic equations'

from math import sqrt as rsqrt
from cmath import sqrt as csqrt

real_ = []                          # I choose to append answers into lists
complex_ = []

def quad(a, b, c):
    t = b**2 - 4*a*c
    if t == 0:                      # equations with one solution
        x = -b/(2.0*a)
        x = '%2.f' % x
        real_.append(x)
        return real_
    elif t < 0:                     # equations with complex solutions
        y = (-b + csqrt(t))/(2.0*a)
        z = (-b - csqrt(t))/(2.0*a)
        complex_.append(y)
        complex_.append(z)
        return complex_
    else:                           # equations with real solutions
        y = (-b + rsqrt(t))/(2.0*a)
        z = (-b - rsqrt(t))/(2.0*a)
        real_.append(y)
        real_.append(z)
        return real_

print 'When a = 1, b = 2 and c = -15\n     x =',
print quad(1, 2, -15)
print 'When a = 1, b = 2 and c = -2\n     x =',
print quad(1, 2, 2)

# b) two test cases for the function with real and complex roots

def test_realroots(a, b, c):               # the test function for the real roots
    print 'real test function called'
    tol = 1e-10
    ex_y = 3                               # expected answers
    ex_z = -5
    success = abs(ex_y - real_[0]) < tol and abs(ex_z - real_[1]) < tol
    msg = "Real roots: wrong answer, expected: %1.f, % 1.f, got %1.f, %1.f" % (ex_y, real_[0], ex_z, real_[1])
    assert success, msg

test_realroots(1, 2, -15)

def test_complexroots(a, b, c):            # the test function for the complex roots
    print 'complex test function called'
    tol = 1e-10                            # this number also works if the imaginary part is wrong (tested)
    expected_y = -1 + 1j                   # expected answers
    expected_z = -1 - 1j
    computed_y = complex_[0]               # computed answers
    computed_z = complex_[1]
    success = abs(expected_y - computed_y) < tol and abs(expected_z - computed_z) < tol
    msg = "wrong answer"
    assert success, msg

print test_complexroots(1, 2, 2)

"""
simen@simen-VirtualBox:~/python/uke3$ python roots_quadratic.py
Quadratic equations
When a = 1, b = 2 and c = -15
     x = [3.0, -5.0]
When a = 1, b = 2 and c = -2
     x = [(-1+1j), (-1-1j)]
real test function called
complex test function called
None
"""
