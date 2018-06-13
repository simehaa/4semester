print """The growth of money in a bank
A = Initial amount
p = interest rate
n = years
The total amount of money (m) in a bank after
n years, is given by the formula:
m = A*(1 + p/100)**n
"""
A = 1000.0 # euros
p = 5.0 # rate
n = float(3) # years
m = A*(1 + (p + 1.0)/100)**n
print 'with %.1f euros as the initial amount' % (A)
print 'and with an interest rate at %.1f percent,' % (p)
print 'the final amount after %.1f years' % (n)
print 'is %.3f euros' % (m)
