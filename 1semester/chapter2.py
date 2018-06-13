print '--Celsius-to-Fahrenheit--'
C = 10
while C <= 16:
    F = C*9./5 + 32
    print '%9.1f %8.1f' % (C, F)
    C += 2

x = 1.2
N = 100
k = 1
s = x
sign = 1.0
import math
while k < N:
    sign = - sign
    k = k + 2
    term = sign*x**k/math.factorial(k)
    s = s + term
print 'sin(%g) = %g' % (x, s)

degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print 'list element:', C
print 'The degrees list has', len(degrees), 'elements'

index = 0
while index < len(degrees):
    C = degrees[index]
    F = 9.*C/5 + 32
    print '%5d %5.1f' % (C, F)
    index += 1

Cdegrees = range(-20, 41, 5)
Fdegrees = [(9./5)*C + 32 for C in Cdegrees]
table = []
for C, F in zip(Cdegrees, Fdegrees):
    table.append([C,F])
print table
table = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
print table
import pprint
pprint.pprint(table)
for C, F in table:
    print '   [%1.f, %5.1f]' % (C, F)

for C, F in table[Cdegrees.index(10):Cdegrees.index(35)]:
    print '%5.0f %5.1f' % (C, F)

for C, F in table[6:11]:
    print '%5.0f %5.1f' % (C, F)

scores = []
scores.append([12, 16, 11, 12])
scores.append([9])
scores.append([6, 9, 11, 14, 17, 15, 14, 20])
for p in range(len(scores)):
    for g in range(len(scores[p])):
        score = scores[p][g]
        print '%4d' % score,
    print
for player in scores:
    for game in player:
        print '%4d' % game,
    print
