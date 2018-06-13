n = raw_input("all odd numbers from 1 to ")
n = float(n)
x = 1; o = 1
if n > 2:
    while o <= n - 2:
        o = 2*x - 1
        print o
        x += 1
elif n > -2:
    print '1'
else:
    print 'Are you retarded?'
