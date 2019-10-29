def diff(f,x,h=1e-6):
    return (f(x+h)-f(x))/h

def f(x):
    return x**4

def g(x):
    return x**2 + 4*x

print diff(f,2,0)
print diff(g,5,5)
print diff(lambda x: x**4, 2.0)
