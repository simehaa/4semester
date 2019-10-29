def trapezint(f, a, b):
    integral = (b - a)/2.0*(f(a) + f(b))
    return integral

print trapezint(x**2 + 3*x, 0, 2)
