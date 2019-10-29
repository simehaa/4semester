r = raw_input("")
r = float(r)
a = 1./r*r
b = 1
if a != b:
    print 'Wrong result!'
print '%.16f' % a
