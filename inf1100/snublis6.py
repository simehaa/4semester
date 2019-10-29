
import numpy as np

n = 50
x = np.zeros(n, dtype=int)        # array med kun flyttall
x[0] = 1
x[1] = 1

for i in range(n-2):
    x[i+2] = x[i+1] + x[i] + 1    # differenslikningen for Leonardo-tallene

print x

##########################
# Metode for aa finne det n-te tallet uten aa lagre alle
n = 1475 # hoyeste tallet uten inf

xpp = float(1)
xp = float(1)

for _ in range(n-2):             # _ brukes av og til for en ubrukt variabel i loopen
    x = 1.0 + xp + xpp
    xpp = xp
    xp = x
print x

###########################
