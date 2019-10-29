def polydict(poly, x):
    s = 0
    for power in poly:
        s += poly[power]*x**power
    return s


def polylist(poly, x):
    s = 0
    for power in range(len(poly)):
        s += poly[power]*x**power
    return s


pdict = {0: -0.5, 100: 2}
plist = [0]*101
plist[0] = -0.5
plist[100] = 2


print pdict, plist, polydict(pdict, 1.05), polylist(plist, 1.05)
