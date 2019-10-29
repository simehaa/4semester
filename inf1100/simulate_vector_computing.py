from numpy import *

x = [0, 2]
t = [1, 1.5]

sinx = [sin(xi) for xi in x]
cos_sin = [cos(sx) for sx in sinx]

tinv = [1.0/ti for ti in t]
exp_inv = [exp(ti) for ti in tinv]

result = []
for xi, ti in zip(cos_sin, exp_inv):
    result.append(xi+ti)

print result

# Raskere og enklere kode med numpy #

x = array(x)
t = array(t)

result = cos(sin(x)) + exp(1.0/t)

print result
