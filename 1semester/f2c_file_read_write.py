F = []
C = []
with open('Fdeg.dat','r') as infile:
    for i in range(3):
        infile.readline()
    for line in infile:
        a = line.split()
        F.append(float(a[2]))


print '|_Fahrenheit_|_Celsius_|'
for i in range(len(F)):
    a = (float(F[i]) - 32)*5.0/9
    C.append(a)
    print '|%8.1f    | %6.1f  |' % (F[i], C[i])





# Generelt apning/lukking av filer, skriving, lesing osv
"""
outfile = open('filnavn.dat', 'w')
...
outfile.close()
"""



with open('F_C.dat','w') as outfile:
    for i in range(len(F)):
        outfile.write("%.2f, %.2f\n" % (F[i], C[i]))

"""
Dette over ble skrevet inn i den før tomme fila F_C.dat!
"""
