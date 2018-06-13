from math import exp, sqrt

f = lambda x: exp(x)
a = 1
true_df = f(a)

for i in range(1,30):
    i = 8 + (i/200.)
    h = 10**(-i)
    newtons_df = (f(a + h) - f(a))/float(h)
    error = abs(true_df - newtons_df)
    print 'h= 10**(-%2i): approximation = %.16g - error = %.16g' % (i, newtons_df, error)
print ' \n \n \n '

h_best = 2*(sqrt(10**(-16)*f(a)))/float(sqrt(f(a)))
newtons_df = (f(a + h_best) - f(a))/float(h_best)
error = abs(true_df - newtons_df)
print 'h= 10**(-%2i): approximation = %.16g - error = %.16g' % (i, newtons_df, error)
