def sum_1k(M):
    k = 1
    s = 0
    for k in range(1,M+1,1):
        s += 1./k
    return s

print sum_1k(3)

def test_sum():
    hand = 1./1 + 1./2 + 1./3 + 1
    return hand

if sum_1k(3) == test_sum():
    print "correct answer! :-)"
else:
    print 'wrong'
