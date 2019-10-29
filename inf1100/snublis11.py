import random

def play_game():
    die = random.randint(1,6)
    if die == 1 or die == 2:
        return True
    else:
        return False

def simulate(M):
    N = 0
    for i in range(M):
        success = play_game()
        if success:
            N += 1

    return float(N)/M

print simulate(1000)
print simulate(10000)
print simulate(100000)
print simulate(1000000)

b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
N = 10000
for i in range(N):
    a = random.randint(1,6)
    if a == 1:
        b += 1
    elif a == 2:
        c += 1
    elif a == 3:
        d += 1
    elif a == 4:
        e += 1
    elif a == 5:
        f += 1
    elif a == 6:
        g += 1

print '1: %.6f' % (b/float(N))
print '2: %.6f' % (c/float(N))
print '3: %.6f' % (d/float(N))
print '4: %.6f' % (e/float(N))
print '5: %.6f' % (f/float(N))
print '6: %.6f' % (g/float(N))
h = ((b + c + d + e + f + g)/(float(N)))
print 'total: %.6f' % h
