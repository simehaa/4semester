coor = []
print 'equally spaced points from (0,1) to'
n = raw_input("choose n: ")
n = int(n)
m = n + 1
for c in range(0, n, 1):
    coor.append(c)
    a = coor[-1]
    b = a**2 + 3*a
    print '(%i,%i)' % (a,b)
