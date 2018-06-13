from math import factorial
n = 1000
i = 500
s = 1
for j in range(1,501):
    s *= float((n-i+j))/(j)
def f(n,i):
    n_over_i = 1
    for j in range(1, n - i + 1):
        n_over_i *= (i + j)/float(j)
    return ("%.16g" % n_over_i)

print abs(eval(f(1000,500))-s)
