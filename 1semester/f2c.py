C = 0

def F(C):
    return (9./5)*C + 32

def C(F):
    return 9./5*C + 32

while C <= 40:
    F = F(C)
    print '%3.1f %3.1f' % (C, F)
    C += 10
