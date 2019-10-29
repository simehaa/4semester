def f(n,i):
    n_over_i = 1
    for j in range(1, n - i + 1):
        n_over_i *= (i + j)/float(j)
    return ("%.16g" % n_over_i)

print f(9998,4)
print f(100000,70)
print f(1000,500)

# terminalprint
"""
416083629102530.9
8.14900007813806e+249
2.702882409454366e+299
"""
