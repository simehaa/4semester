import numpy as np
import matplotlib.pyplot as plt

V_0 = 34. # MeV
dx = 14. # fm
m = 3727.379378 # MeV
hbar = 197.3 # MeV fm

def T(E):
    return 1./(1 + V_0**2/(4.*E*(V_0 - E))*np.sinh(dx*np.sqrt(2*m*(V_0 - E))/hbar)**2)

v = 0.1 # c
E_0 = 11.2#0.5*3727.379378*v**2
"""
E = np.linspace(0,34,1001)
plt.plot(E,T(E),label='T(E)')
E_1 = 4.08
E_2 = 9.85
plt.title('T(E) der $V_0 = 34$ MeV og $\Delta x = 17$ fm')
plt.plot(E_1,T(E_1),'ro',label='$E_{\\alpha}$ for $^{232}Th$, T = %1.1e' % T(E_1))
plt.plot(E_2,T(E_2),'go',label='$E_{\\alpha}$ for $^{218}Th$, T = %1.1e' % T(E_2))
plt.yscale('log')
plt.xlabel('E [MeV]')
plt.ylabel('T')
plt.grid()
plt.legend(loc='best')
# plt.show()"""
treff = 1/T(E_0)
treffrekv = v*299792458/(14.6e-15)

tid = treff/treffrekv
print T(E_0)
